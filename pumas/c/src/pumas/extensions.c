#include <float.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#include "pumas/extensions.h"

#ifdef PUMAS_USE_EARTH_GEOMETRY
#include "gull.h"
#include "turtle.h"
#endif


/* Forward error messages to a buffer */
#define ERROR_SIZE 2048
static char last_error[ERROR_SIZE] = {0x0};

static void forward_error(int rc, void (*caller)(void), const char * message)
{
        strncpy(last_error, message, ERROR_SIZE);
}
#undef ERROR_SIZE

static void forward_error_pumas(
    enum pumas_return rc, pumas_function_t * caller, const char * message)
{
        forward_error(rc, caller, message);
}

#ifdef PUMAS_USE_EARTH_GEOMETRY
static void forward_error_gull(
    enum gull_return rc, gull_function_t * caller, const char * message)
{
        forward_error(rc, caller, message);
}

static void forward_error_turtle(
    enum turtle_return rc, turtle_function_t * caller, const char * message)
{
        forward_error(rc, caller, message);
}
#endif


void pumas_error_initialise(void)
{
    pumas_error_handler_set(forward_error_pumas);

#ifdef PUMAS_USE_EARTH_GEOMETRY
    gull_error_handler_set(forward_error_gull);
    turtle_error_handler_set(forward_error_turtle);
#endif
}


/* Manage the last error message */
void pumas_error_clear(void)
{
        last_error[0] = 0x0;
}

const char * pumas_error_get(void)
{
        return (last_error[0] == 0x0) ? NULL : last_error;
}


void pumas_state_extended_reset(struct pumas_state_extended * state,
    struct pumas_context * context)
{
        state->context = context;
        state->geodetic.computed = 0;
        state->vertical.distance = -1;
}


/* Setters and getters for the geometry */
struct pumas_geometry * pumas_geometry_get(struct pumas_context * context)
{
        struct pumas_user_data * user_data = context->user_data;
        return user_data->top;
}


void pumas_geometry_set(
    struct pumas_context * context, struct pumas_geometry * geometry)
{
        struct pumas_user_data * user_data = context->user_data;
        user_data->top = geometry;
}


static void geometry_reset(struct pumas_geometry * geometry)
{
        if (geometry->reset != NULL) geometry->reset(geometry);

        struct pumas_geometry * g;
        for (g = geometry->daughters; g != NULL; g = g->next)
                geometry_reset(g);
}


void pumas_geometry_reset(struct pumas_context * context)
{
        struct pumas_user_data * user_data = context->user_data;
        user_data->current = user_data->top;
        if (user_data->top != NULL)
                geometry_reset(user_data->top);
}


static void geometry_destroy(struct pumas_geometry * geometry)
{
        struct pumas_geometry * g;
        for (g = geometry->daughters; g != NULL; g = g->next)
                geometry_destroy(g);
        if (geometry->destroy != NULL) geometry->destroy(geometry);
}


void pumas_geometry_destroy(struct pumas_context * context)
{
        struct pumas_user_data * user_data = context->user_data;
        if (user_data->top != NULL) {
                geometry_destroy(user_data->top);
                user_data->top = NULL;
        }
        user_data->current = NULL;
}


void pumas_geometry_push(struct pumas_geometry * geometry,
    struct pumas_geometry * daughter)
{
        daughter->mother = geometry;

        if (geometry->daughters == NULL) {
                geometry->daughters = daughter;
        } else {
                struct pumas_geometry * last = geometry->daughters;
                while (last->next != NULL) last = last->next;
                last->next = daughter;
        }
}


/* The transparent medium, e.g. for bounding boxes */
static struct pumas_medium transparent_medium = { -1, NULL };
struct pumas_medium * PUMAS_MEDIUM_TRANSPARENT = &transparent_medium;


/* Recursive geometry navigation */
static void geometry_navigate(struct pumas_geometry * geometry,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p, struct pumas_geometry * exclude,
    struct pumas_geometry ** current_p)
{
        if (geometry == NULL) return;

        geometry->get(geometry, state, medium_p, step_p);
        *current_p = geometry;

        struct pumas_state_extended * extended = (void *)state;
        struct pumas_user_data * user_data =
            (void *)extended->context->user_data;
        if (user_data->callback != NULL) {
                user_data->callback(geometry, state, *medium_p,
                    (step_p == NULL) ? -1 : *step_p);
        }

        if ((*medium_p != NULL) && (geometry->daughters != NULL)) {
                double step;
                struct pumas_medium * medium = *medium_p;
                if (step_p != NULL) step = *step_p;

                *medium_p = NULL;
                struct pumas_geometry * daughter;
                for (daughter = geometry->daughters; daughter != NULL;
                     daughter = daughter->next) {
                        if (daughter == exclude) continue;

                        geometry_navigate(daughter, state, medium_p, step_p,
                                          geometry, current_p);
                        if (*medium_p != NULL) break;
                        else if (step_p != NULL) {
                                if ((*step_p > 0) && (*step_p < step))
                                        step = *step_p;
                        }
                }
                if (*medium_p == NULL) {
                        *current_p = geometry;
                        *medium_p = medium;
                        if (step_p != NULL) *step_p = step;
                }
        }

        if (*medium_p == PUMAS_MEDIUM_TRANSPARENT) *medium_p = NULL;

        if ((*medium_p == NULL) && (geometry->mother != NULL) &&
            (geometry->mother != exclude)) {
                        geometry_navigate(geometry->mother, state, medium_p,
                                          step_p, geometry, current_p);
        }
}


/* Generic geometry callback */
enum pumas_step pumas_geometry_medium(struct pumas_context * context,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p)
{
        struct pumas_user_data * user_data = context->user_data;
        struct pumas_geometry * geometry = user_data->current;
        if (geometry == NULL) geometry = user_data->top;

        struct pumas_state_extended * extended = (void *)state;
        extended->geodetic.computed = 0;

        struct pumas_medium * tmp;
        geometry_navigate(geometry, state, &tmp, step_p, NULL,
                          &user_data->current);
        if (medium_p != NULL) *medium_p = tmp;

        return PUMAS_STEP_CHECK;
}


static double add_global_magnet(struct pumas_state * state,
    struct pumas_locals * locals)
{
        struct pumas_state_extended * extended = (void *)state;
        struct pumas_context * context = extended->context;
        struct pumas_user_data * user_data = context->user_data;
        struct pumas_geometry * geometry = user_data->current;
        if (geometry->magnet == NULL)
                return 0;

        double magnet[3];
        const double s = geometry->magnet(geometry, state, magnet);

        int i;
        for (i = 0; i < 3; i++)
                locals->magnet[i] += magnet[i];

        return s;
}


/* Uniform medium */
static double uniform_locals(struct pumas_medium * medium,
    struct pumas_state * state, struct pumas_locals * locals)
{
        struct pumas_medium_uniform * uniform =
            (struct pumas_medium_uniform *)medium;
        memcpy(locals, &uniform->locals, sizeof *locals);

        /* Look for a global magnetic field */
        return add_global_magnet(state, locals);
}


void pumas_medium_uniform_initialise(struct pumas_medium_uniform * uniform,
    int material, double density, const double * magnet)
{
        uniform->medium.material = material;
        uniform->medium.locals = &uniform_locals;
        uniform->locals.density = density;
        if (magnet != NULL) {
                memcpy(uniform->locals.magnet, magnet,
                    sizeof uniform->locals.magnet);
        } else {
                memset(uniform->locals.magnet, 0x0,
                    sizeof uniform->locals.magnet);
        }
}


/* Medium with a density gradient */
double pumas_medium_gradient_density(
    struct pumas_medium_gradient * medium, struct pumas_state_extended * state)
{
        /* Project onto the gradient axis */
        const double * const u = medium->gradient.axis;
        double z;
        if (medium->gradient.project != NULL) {
                z = medium->gradient.project(medium, state);
        } else {
                const double * const r = state->base.position;
                z = r[0] * u[0] + r[1] * u[1] + r[2] * u[2];
        }

        /* Compute the density */
        if (medium->gradient.type == PUMAS_MEDIUM_GRADIENT_LINEAR) {
                return (1. + (z - medium->gradient.z0) /
                    medium->gradient.lambda) * medium->gradient.rho0;
        } else {
                return medium->gradient.rho0 *
                    exp((z - medium->gradient.z0) / medium->gradient.lambda);
        }
}


static double gradient_locals(struct pumas_medium * medium_,
    struct pumas_state * state, struct pumas_locals * locals)
{
#define GRADIENT_MIN_PROJECTION 5E-02

        /* Set the magnetic field */
        struct pumas_medium_gradient * medium = (void *)medium_;
        memcpy(locals->magnet, medium->magnet, sizeof locals->magnet);
        double step = add_global_magnet(state, locals);

        /* Compute the density and the gradient length */
        locals->density = pumas_medium_gradient_density(medium, (void *)state);

        /* Compute the gradient length */
        const double * const u = medium->gradient.axis;
        const double * const v = state->direction;
        double d = fabs(u[0] * v[0] + u[1] * v[1] + u[2] * v[2]);
        if (d < GRADIENT_MIN_PROJECTION)
                d = GRADIENT_MIN_PROJECTION;

        const double step2 =
            fabs(medium->gradient.lambda / d);
        if (step <= 0) return step2;
        else return (step < step2) ? step: step2;
#undef GRADIENT_MIN_PROJECTION
}


void pumas_medium_gradient_initialise(
    struct pumas_medium_gradient * medium, int material,
    enum pumas_medium_gradient_type type, double lambda, double z0,
    double rho0, const double * magnet)
{
        medium->medium.material = material;
        medium->medium.locals = &gradient_locals;

        medium->gradient.type = type;
        medium->gradient.lambda = lambda;
        medium->gradient.z0 = z0;
        medium->gradient.rho0 = rho0;

        medium->gradient.project = NULL;
        memset(medium->gradient.axis, 0x0,
            sizeof medium->gradient.axis);

        if (magnet != NULL)
                memcpy(medium->magnet, magnet, sizeof medium->magnet);
        else
                memset(medium->magnet, 0x0, sizeof medium->magnet);
}


static void geometry_infinite_get(struct pumas_geometry * base_geometry,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p)
{
        if (medium_p != NULL) {
                struct pumas_geometry_infinite * geometry =
                    (void *)base_geometry;
                *medium_p = geometry->medium;
        }

        if (step_p != NULL) *step_p = 0;
}


static void geometry_infinite_destroy(struct pumas_geometry * geometry)
{
        free(geometry);
}


struct pumas_geometry_infinite * pumas_geometry_infinite_create(
    struct pumas_medium * medium)
{
        struct pumas_geometry_infinite * geometry = calloc(1, sizeof *geometry);
        if (geometry == NULL) return NULL;

        geometry->base.get = &geometry_infinite_get;
        geometry->base.destroy = &geometry_infinite_destroy;
        geometry->medium = medium;

        return geometry;
}


struct pumas_geometry_polyhedron * pumas_geometry_polyhedron_create(
    struct pumas_medium * medium, int n_faces)
{
        struct pumas_geometry_polyhedron * geometry = calloc(1,
            sizeof(*geometry) +
            n_faces * sizeof(struct pumas_polyhedron_face));
        geometry->base.get = pumas_geometry_polyhedron_get;
        geometry->base.destroy = pumas_geometry_polyhedron_destroy;
        geometry->medium = medium;
        geometry->n_faces = n_faces;

        return geometry;
}


void pumas_geometry_polyhedron_destroy(struct pumas_geometry * geometry)
{
        struct pumas_geometry * g;
        for (g = geometry->daughters; g != NULL; g = g->next) {
                pumas_geometry_polyhedron_destroy(g);
        }
        free(geometry);
}


void pumas_geometry_polyhedron_get(struct pumas_geometry * geometry,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p)
{
#define POLYHEDRON_STEP_MIN 1E-05

        struct pumas_geometry_polyhedron * p = (void *)geometry;
        const double * const position = state->position;

        struct pumas_state_extended * extended = (void *)state;
        const double sgn =
            (extended->context->mode.direction == PUMAS_MODE_FORWARD)? 1 : -1;
        const double direction[3] = {sgn * state->direction[0],
                                     sgn * state->direction[1],
                                     sgn * state->direction[2]};

        double dE = -DBL_MAX, dL = DBL_MAX;
        int i, inside = 1;
        struct pumas_polyhedron_face * s;
        for (i = 0, s = p->faces; i < p->n_faces; i++, s++) {
                const double rn = (position[0] - s->origin[0]) * s->normal[0] +
                    (position[1] - s->origin[1]) * s->normal[1] +
                    (position[2] - s->origin[2]) * s->normal[2];
                if (rn > 0) inside = 0;
                const double un = direction[0] * s->normal[0] +
                    direction[1] * s->normal[1] + direction[2] * s->normal[2];
                if (fabs(un) <= FLT_EPSILON) continue;
                const double d = (rn == 0) ? 0 : -rn / un;
                if ((un > 0) && (d < dL))
                        dL = d;
                else if ((un < 0.) && (d > dE))
                        dE = d;
        }

        double step;
        struct pumas_medium * medium;
        if (inside && (dL > 0)) {
                step = (dL > POLYHEDRON_STEP_MIN) ? dL : POLYHEDRON_STEP_MIN;
                medium = p->medium;
        } else if (!inside && (dE > 0)) {
                step = (dE > POLYHEDRON_STEP_MIN) ? dE : POLYHEDRON_STEP_MIN;
                medium = NULL;
        } else {
                step = DBL_MAX;
                medium = (dL == 0) ? p->medium : NULL;
        }

        if (step_p != NULL) *step_p = step;
        if (medium_p != NULL) *medium_p = medium;

#undef POLYHEDRON_STEP_MIN
}


struct pumas_flux_tabulation * pumas_flux_tabulation_load(const char * path)
{
        FILE * fid = fopen(path, "rb");
        if (fid == NULL) return NULL;

        struct pumas_flux_tabulation * tabulation = NULL;
        int64_t shape[3];
        double range[6];

        if (fread(shape, 8, 3, fid) != 3) goto error;
        if (fread(range, 8, 6, fid) != 6) goto error;

        /* XXX check endianess */

        int64_t size = 2 * shape[0] * shape[1] * shape[2];
        tabulation = malloc(sizeof (*tabulation) + 4 * size);
        if (tabulation == NULL) goto error;

        if (fread(tabulation->data, 4, size, fid) != (size_t)size) goto error;
        fclose(fid);

        tabulation->n_k = shape[0];
        tabulation->n_c = shape[1];
        tabulation->n_h = shape[2];
        tabulation->k_min = range[0];
        tabulation->k_max = range[1];
        tabulation->c_min = range[2];
        tabulation->c_max = range[3];
        tabulation->h_min = range[4];
        tabulation->h_max = range[5];

        return tabulation;
error:
        fclose(fid);
        free(tabulation);
        return NULL;
}


double pumas_flux_tabulation_get(
    const struct pumas_flux_tabulation * tabulation, double k, double c,
    double h, double charge)
{
        /* Compute the interpolation indices and coefficients */
        const double dlk = log(tabulation->k_max / tabulation->k_min) /
                           (tabulation->n_k - 1);
        double hk = log(k / tabulation->k_min) / dlk;
        if ((hk < 0.) || (hk > tabulation->n_k - 1)) return 0.;
        const int ik = (int)hk;
        hk -= ik;

        const double dc = (tabulation->c_max - tabulation->c_min) /
                          (tabulation->n_c - 1);
        double hc = (c - tabulation->c_min) / dc;
        if ((hc < 0.) || (hc > tabulation->n_c - 1)) return 0.;
        const int ic = (int)hc;
        hc -= ic;

        const double dh = (tabulation->h_max - tabulation->h_min) /
                          (tabulation->n_h - 1);
        double hh = (h - tabulation->h_min) / dh;
        if ((hh < 0.) || (hh > tabulation->n_h - 1)) return 0.;
        const int ih = (int)hh;
        hh -= ih;

        const int ik1 = (ik < tabulation->n_k - 1) ?
            ik + 1 : tabulation->n_k - 1;
        const int ic1 = (ic < tabulation->n_c - 1) ?
            ic + 1 : tabulation->n_c - 1;
        const int ih1 = (ih < tabulation->n_h - 1) ?
            ih + 1 : tabulation->n_h - 1;
        const float * const f000 =
            tabulation->data + 2 * ((ih * tabulation->n_c + ic) *
            tabulation->n_k + ik);
        const float * const f010 =
            tabulation->data + 2 * ((ih * tabulation->n_c + ic1) *
            tabulation->n_k + ik);
        const float * const f100 =
            tabulation->data + 2 * ((ih * tabulation->n_c + ic) *
            tabulation->n_k + ik1);
        const float * const f110 =
            tabulation->data + 2 * ((ih * tabulation->n_c + ic1) *
            tabulation->n_k + ik1);
        const float * const f001 =
            tabulation->data + 2 * ((ih1 * tabulation->n_c + ic) *
            tabulation->n_k + ik);
        const float * const f011 =
            tabulation->data + 2 * ((ih1 * tabulation->n_c + ic1) *
            tabulation->n_k + ik);
        const float * const f101 =
            tabulation->data + 2 * ((ih1 * tabulation->n_c + ic) *
            tabulation->n_k + ik1);
        const float * const f111 =
            tabulation->data + 2 * ((ih1 * tabulation->n_c + ic1) *
            tabulation->n_k + ik1);

        /* Interpolate the flux */
        double flux = 0.;
        int i;
        for (i = 0; i < 2; i++) {
                if ((1 - 2 * i) * charge < 0) continue;

                /* Linear interpolation along cos(theta) */
                const double g00 = f000[i] * (1. - hc) + f010[i] * hc;
                const double g10 = f100[i] * (1. - hc) + f110[i] * hc;
                const double g01 = f001[i] * (1. - hc) + f011[i] * hc;
                const double g11 = f101[i] * (1. - hc) + f111[i] * hc;

                /* Log or linear interpolation along log(kinetic) */
                double g0;
                if ((g00 <= 0.) || (g10 <= 0.))
                        g0 = g00 * (1. - hk) + g10 * hk;
                else
                        g0 = exp(log(g00) * (1. - hk) + log(g10) * hk);

                double g1;
                if ((g01 <= 0.) || (g11 <= 0.))
                        g1 = g01 * (1. - hk) + g11 * hk;
                else
                        g1 = exp(log(g01) * (1. - hk) + log(g11) * hk);

                /* Log or linear interpolation along altitude */
                if ((g0 <= 0.) || (g1 <= 0.))
                        flux += g0 * (1. - hh) + g1 * hh;
                else
                        flux += exp(log(g0) * (1. - hh) + log(g1) * hh);
        }
        return flux;
}
