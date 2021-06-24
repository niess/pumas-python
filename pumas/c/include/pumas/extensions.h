#ifndef pumas_extensions_h
#define pumas_extensions_h
#ifdef __cplusplus
extern "C" {
#endif

#include "pumas.h"

/* Wrapper for geometries */
struct pumas_geometry {
        void (*get)(struct pumas_geometry *, struct pumas_state *,
            struct pumas_medium **, double *);
        double (*magnet)(struct pumas_geometry *, struct pumas_state *,
            double *);
        void (*reset)(struct pumas_geometry *);
        void (*destroy)(struct pumas_geometry *);

        struct pumas_geometry * mother;
        struct pumas_geometry * daughters;
        struct pumas_geometry * next;
};

/* A transparent medium, e.g. for a bounding box */
extern struct pumas_medium * PUMAS_MEDIUM_TRANSPARENT;

/* Layout of the user data section */
struct pumas_user_data {
        struct pumas_geometry * top;
        struct pumas_geometry * current;
        void (*callback)(struct pumas_geometry *, struct pumas_state *,
            struct pumas_medium *, double); /* User callback for debug */
};

/* Forward errors */
void pumas_error_initialise(void);
void pumas_error_clear(void);
const char * pumas_error_get(void);

/* Extended state  with a ref to the processing context */
struct pumas_state_extended {
        struct pumas_state base;
        struct pumas_context * context;

        struct {
                int computed;
                double latitude;
                double longitude;
                double altitude;
        } geodetic;

        struct {
                double distance;
                double last[3];
        } vertical;
};

void pumas_state_extended_reset(struct pumas_state_extended * state,
    struct pumas_context * context);

/* A uniform medium */
struct pumas_medium_uniform {
        struct pumas_medium medium;
        struct pumas_locals locals;
};

void pumas_medium_uniform_initialise(struct pumas_medium_uniform * uniform,
    int material, double density, const double * magnet);

/* A medium with a density gradient */
enum pumas_medium_gradient_type {
        PUMAS_MEDIUM_GRADIENT_LINEAR = 0,
        PUMAS_MEDIUM_GRADIENT_EXPONENTIAL
};

struct pumas_medium_gradient {
        struct pumas_medium medium;
        double magnet[3];

        struct {
                enum pumas_medium_gradient_type type;
                double lambda;
                double z0;
                double rho0;

                double axis[3];
                double (* project)(struct pumas_medium_gradient * medium,
                                   struct pumas_state_extended * state);
        } gradient;
};

void pumas_medium_gradient_initialise(
    struct pumas_medium_gradient * medium, int material,
    enum pumas_medium_gradient_type type, double lambda, double z0,
    double rho0, const double * magnet);

double pumas_medium_gradient_density(
    struct pumas_medium_gradient * medium, struct pumas_state_extended * state);

/* Setters and getters for the geometry */
struct pumas_geometry * pumas_geometry_get(struct pumas_context * context);

void pumas_geometry_set(
    struct pumas_context * context, struct pumas_geometry * geometry);

void pumas_geometry_destroy(struct pumas_context * context);

void pumas_geometry_reset(struct pumas_context * context);

void pumas_geometry_push(struct pumas_geometry * geometry,
    struct pumas_geometry * daughter);

/* Generic geometry callback for PUMAS */
enum pumas_step pumas_geometry_medium(struct pumas_context * context,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p);

/* Per context data for the infinite geometry */
struct pumas_geometry_infinite {
        struct pumas_geometry base;
        struct pumas_medium * medium;
};

/* Geometry creation for a single medium of infinite extension */
struct pumas_geometry_infinite * pumas_geometry_infinite_create(
    struct pumas_medium * medium);

/* Data for the Polyhedron geometry */
struct pumas_polyhedron_face {
        double origin[3];
        double normal[3];
};

struct pumas_geometry_polyhedron {
        struct pumas_geometry base;
        struct pumas_medium * medium;

        int n_faces;
        struct pumas_polyhedron_face faces[];
};

/* Create and destroy a polyhedron geometry */
struct pumas_geometry_polyhedron * pumas_geometry_polyhedron_create(
    struct pumas_medium * medium, int n_faces);

void pumas_geometry_polyhedron_destroy(struct pumas_geometry * geometry);

/* Getter for a Polyhedron geometry */
void pumas_geometry_polyhedron_get(struct pumas_geometry * geometry,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p);

/* Flux tabulations */
struct pumas_flux_tabulation {
        int n_k;
        int n_c;
        int n_h;
        double k_min;
        double k_max;
        double c_min;
        double c_max;
        double h_min;
        double h_max;
        float data[];
};

struct pumas_flux_tabulation * pumas_flux_tabulation_load(const char * path);

double pumas_flux_tabulation_get(
    const struct pumas_flux_tabulation * tabulation, double k, double c,
    double h, double charge);

#ifdef __cplusplus
}
#endif
#endif
