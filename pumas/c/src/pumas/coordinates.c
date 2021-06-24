#include "pumas_coordinates.h"


/* Coordinates transforms */
static void cartesian_point_transform(struct pumas_cartesian_point * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        const struct pumas_coordinates_unitary_transformation * initial_frame =
            self->frame;

        if (initial_frame != NULL) {
                const double r[3] = { self->x, self->y, self->z };
                self->x = initial_frame->translation[0] +
                          initial_frame->matrix[0][0] * r[0] +
                          initial_frame->matrix[0][1] * r[1] +
                          initial_frame->matrix[0][2] * r[2];
                self->y = initial_frame->translation[1] +
                          initial_frame->matrix[1][0] * r[0] +
                          initial_frame->matrix[1][1] * r[1] +
                          initial_frame->matrix[1][2] * r[2];
                self->z = initial_frame->translation[2] +
                          initial_frame->matrix[2][0] * r[0] +
                          initial_frame->matrix[2][1] * r[1] +
                          initial_frame->matrix[2][2] * r[2];
        }

        if (frame != NULL) {
                const double r[3] = { self->x - frame->translation[0],
                                      self->y - frame->translation[1],
                                      self->z - frame->translation[2] };
                self->x = frame->matrix[0][0] * r[0] +
                          frame->matrix[1][0] * r[1] +
                          frame->matrix[2][0] * r[2];
                self->y = frame->matrix[0][1] * r[0] +
                          frame->matrix[1][1] * r[1] +
                          frame->matrix[2][1] * r[2];
                self->z = frame->matrix[0][2] * r[0] +
                          frame->matrix[1][2] * r[1] +
                          frame->matrix[2][2] * r[2];
        }

        self->frame = (void *)frame;
}


void pumas_coordinates_cartesian_point_transform(
    struct pumas_cartesian_point * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        if (self->frame == frame) return;
        cartesian_point_transform(self, frame);
}


static void cartesian_vector_transform(struct pumas_cartesian_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        const struct pumas_coordinates_unitary_transformation * initial_frame =
            self->frame;

        if (initial_frame != NULL) {
                const double r[3] = { self->x, self->y, self->z };
                self->x = initial_frame->matrix[0][0] * r[0] +
                          initial_frame->matrix[0][1] * r[1] +
                          initial_frame->matrix[0][2] * r[2];
                self->y = initial_frame->matrix[1][0] * r[0] +
                          initial_frame->matrix[1][1] * r[1] +
                          initial_frame->matrix[1][2] * r[2];
                self->z = initial_frame->matrix[2][0] * r[0] +
                          initial_frame->matrix[2][1] * r[1] +
                          initial_frame->matrix[2][2] * r[2];
        }

        if (frame != NULL) {
                const double r[3] = { self->x, self->y, self->z };
                self->x = frame->matrix[0][0] * r[0] +
                          frame->matrix[1][0] * r[1] +
                          frame->matrix[2][0] * r[2];
                self->y = frame->matrix[0][1] * r[0] +
                          frame->matrix[1][1] * r[1] +
                          frame->matrix[2][1] * r[2];
                self->z = frame->matrix[0][2] * r[0] +
                          frame->matrix[1][2] * r[1] +
                          frame->matrix[2][2] * r[2];
        }

        self->frame = (void *)frame;
}


void pumas_coordinates_cartesian_vector_transform(
    struct pumas_cartesian_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        if (self->frame == frame) return;
        cartesian_vector_transform(self, frame);
}


static void cartesian_from_geodetic(struct pumas_cartesian_point * self,
    const struct pumas_geodetic_point * point)
{
        turtle_ecef_from_geodetic(point->latitude, point->longitude,
                                  point->altitude, (double *)self);
}


void pumas_coordinates_cartesian_point_from_geodetic(
    struct pumas_cartesian_point * self,
    const struct pumas_geodetic_point * point)
{
        cartesian_from_geodetic(self, point);
        self->frame = NULL;
}


static void cartesian_from_spherical(void * self_, const void * point_)
{
        struct pumas_cartesian_point * self = self_;
        const struct pumas_spherical_point * point = point_;
        const double st = sin(point->theta);
        self->x = point->r * cos(point->phi) * st;
        self->y = point->r * sin(point->phi) * st;
        self->z = point->r * cos(point->theta);
}


void pumas_coordinates_cartesian_point_from_spherical(
    struct pumas_cartesian_point * self,
    const struct pumas_spherical_point * point)
{
        cartesian_from_spherical(self, point);
        self->frame = point->frame;
}


static void spherical_from_horizontal(
    struct pumas_spherical_vector * self,
    const struct pumas_horizontal_vector * vector)
{
        memcpy(self, vector, sizeof *self);
        self->theta = 0.5 * M_PI - self->theta;
        self->phi = 0.5 * M_PI - self->phi;
}


static void cartesian_from_horizontal(
    struct pumas_cartesian_vector * self,
    const struct pumas_horizontal_vector * vector)
{
        struct pumas_spherical_vector tmp;
        spherical_from_horizontal(&tmp, vector);

        cartesian_from_spherical(self, &tmp);
}


void pumas_coordinates_cartesian_vector_from_horizontal(
    struct pumas_cartesian_vector * self,
    const struct pumas_horizontal_vector * vector)
{
        cartesian_from_horizontal(self, vector);
        self->frame = vector->frame;
}


void pumas_coordinates_cartesian_vector_from_spherical(
    struct pumas_cartesian_vector * self,
    const struct pumas_spherical_vector * vector)
{
        cartesian_from_spherical(self, vector);
        self->frame = vector->frame;
}


static void spherical_from_cartesian(void * self_, const void * point_)
{
        struct pumas_spherical_point * self = self_;
        const struct pumas_cartesian_point * point = point_;
        const double rho2 = point->x * point->x + point->y * point->y;
        const double rho = sqrt(rho2);
        self->theta = atan2(rho, point->z);

        double phi;
        if (fabs(self->theta) <= FLT_EPSILON)
                self->phi = 0;
        else
                self->phi = atan2(point->y, point->x);

        self->r = sqrt(rho2 + point->z * point->z);
}


void pumas_coordinates_spherical_point_from_cartesian(
    struct pumas_spherical_point * self,
    const struct pumas_cartesian_point * point)
{
        spherical_from_cartesian(self, point);
        self->frame = point->frame;
}


void pumas_coordinates_spherical_point_from_geodetic(
    struct pumas_spherical_point * self,
    const struct pumas_geodetic_point * point)
{
        struct pumas_cartesian_point tmp;
        cartesian_from_geodetic(&tmp, point);
        spherical_from_cartesian(self, &tmp);
        self->frame = NULL;
}


void pumas_coordinates_spherical_vector_from_cartesian(
    struct pumas_spherical_vector * self,
    const struct pumas_cartesian_vector * vector)
{
        spherical_from_cartesian(self, vector);
        self->frame = vector->frame;
}


void pumas_coordinates_spherical_vector_from_horizontal(
    struct pumas_spherical_vector * self,
    const struct pumas_horizontal_vector * vector)
{
        spherical_from_horizontal(self, vector);
        self->frame = vector->frame;
}


void pumas_coordinates_geodetic_point_from_cartesian(
    struct pumas_geodetic_point * self,
    const struct pumas_cartesian_point * point)
{
        struct pumas_cartesian_point tmp;
        if (point->frame != NULL) {
                memcpy(&tmp, point, sizeof tmp);
                cartesian_point_transform(&tmp, NULL);
                point = &tmp;
        }

        turtle_ecef_to_geodetic((double *)point, &self->latitude,
                                &self->longitude, &self->altitude);
}


void pumas_coordinates_geodetic_point_from_spherical(
    struct pumas_geodetic_point * self,
    const struct pumas_spherical_point * point)
{
        struct pumas_cartesian_point tmp;
        cartesian_from_spherical(&tmp, point);

        if (point->frame != NULL)
                cartesian_point_transform(&tmp, NULL);

        turtle_ecef_to_geodetic((double *)point, &self->latitude,
                                &self->longitude, &self->altitude);
}


static void horizontal_from_spherical(
    struct pumas_horizontal_vector * self,
    const struct pumas_spherical_vector * vector)
{
        memcpy(self, vector, sizeof *self);
        if ((self->elevation == 0) || (self->elevation == M_PI)) {
                self->elevation = 0.5 * M_PI - self->elevation;
                self->azimuth = 0;
        } else {
                self->elevation = 0.5 * M_PI - self->elevation;
                self->azimuth = 0.5 * M_PI - self->azimuth;
        }
}


static void horizontal_from_cartesian(
    struct pumas_horizontal_vector * self,
    const struct pumas_cartesian_vector * vector)
{
        struct pumas_spherical_vector tmp;
        spherical_from_cartesian(&tmp, vector);
        horizontal_from_spherical(self, &tmp);
}


void pumas_coordinates_horizontal_vector_from_cartesian(
    struct pumas_horizontal_vector * self,
    const struct pumas_cartesian_vector * vector)
{
        horizontal_from_cartesian(self, vector);
        self->frame = vector->frame;
}


void pumas_coordinates_horizontal_vector_from_spherical(
    struct pumas_horizontal_vector * self,
    const struct pumas_spherical_vector * vector)
{
        horizontal_from_spherical(self, vector);
        self->frame = vector->frame;
}


void pumas_coordinates_horizontal_vector_transform(
    struct pumas_horizontal_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        if (self->frame == frame) return;

        struct pumas_cartesian_vector tmp;
        cartesian_from_horizontal(&tmp, self);
        tmp.frame = self->frame;
        cartesian_vector_transform(&tmp, frame);
        horizontal_from_cartesian(self, &tmp);
        self->frame = (void *)frame;
}


void pumas_coordinates_spherical_point_transform(
    struct pumas_spherical_point * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        if (self->frame == frame) return;

        struct pumas_cartesian_point tmp;
        cartesian_from_spherical(&tmp, self);
        tmp.frame = self->frame;
        cartesian_point_transform(&tmp, frame);
        spherical_from_cartesian(self, &tmp);
        self->frame = (void *)frame;
}


void pumas_coordinates_spherical_vector_transform(
    struct pumas_spherical_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame)
{
        if (self->frame == frame) return;

        struct pumas_cartesian_vector tmp;
        cartesian_from_spherical(&tmp, self);
        tmp.frame = self->frame;
        cartesian_vector_transform(&tmp, frame);
        spherical_from_cartesian(self, &tmp);
        self->frame = (void *)frame;
}


void pumas_coordinates_unitary_transformation_from_euler(
    struct pumas_coordinates_unitary_transformation * transformation,
    int n, int * axis, double * angles)
{
        /* Initialise to the identity */
        int i, j, k, l;
        for (i = 0; i < 3; i++) for (j = 0; j < 3; j++) {
                transformation->matrix[i][j] = (i == j) ? 1. : 0.;
        }

        /* Fill with elementary rotations */
        for (l = n - 1; l >= 0; l--) {
                if (angles[l] == 0) continue;
                const double c = cos(angles[l]);
                const double s = sin(angles[l]);
                double r[3][3];

                if (axis[l] == 0) {
                        r[0][0] =  1, r[1][0] =  0, r[2][0] =  0;
                        r[0][1] =  0, r[1][1] =  c, r[2][1] =  s;
                        r[0][2] =  0, r[1][2] = -s, r[2][2] =  c;
                } else if (axis[l] == 1) {
                        r[0][0] =  c, r[1][0] =  0, r[2][0] = -s;
                        r[0][1] =  0, r[1][1] =  1, r[2][1] =  0;
                        r[0][2] =  s, r[1][2] =  0, r[2][2] =  c;
                } else if (axis[l] == 2) {
                        r[0][0] =  c, r[1][0] =  s, r[2][0] =  0;
                        r[0][1] = -s, r[1][1] =  c, r[2][1] =  0;
                        r[0][2] =  0, r[1][2] =  0, r[2][2] =  1;
                } else {
                        continue;
                }

                double m[3][3] = {0};
                for (i = 0; i < 3; i++)
                        for (j = 0; j <3; j++)
                                for (k = 0; k < 3; k++) {
                                        m[i][j] +=
                                            transformation->matrix[i][k] *
                                            r[k][j];
                }

                memcpy(transformation->matrix, m, sizeof(m));
        }
}


void pumas_coordinates_frame_initialise_local(
    struct pumas_coordinates_unitary_transformation * frame,
    const struct pumas_cartesian_point * cartesian,
    const struct pumas_geodetic_point * geodetic, double declination,
    double inclination)
{
        struct pumas_cartesian_point cartesian_data;
        struct pumas_geodetic_point geodetic_data;

        if (frame == NULL) return;
        else if ((cartesian == NULL) && (geodetic == NULL)) {
                memset(frame, 0x0, sizeof(*frame));
                int i;
                for (i = 0; i < 3; i++)
                        frame->matrix[i][i] = 1;
                return;
        }

        if (cartesian == NULL) {
                pumas_coordinates_cartesian_point_from_geodetic(
                    &cartesian_data, geodetic);
                cartesian = &cartesian_data;
        } else if (cartesian->frame != NULL) {
                memcpy(&cartesian_data, cartesian, sizeof cartesian_data);
                pumas_coordinates_cartesian_point_transform(
                    &cartesian_data, NULL);
                cartesian = &cartesian_data;
        }

        if (geodetic == NULL) {
                pumas_coordinates_geodetic_point_from_cartesian(
                    &geodetic_data, cartesian);
                geodetic = &geodetic_data;
        }

        frame->translation[0] = cartesian->x;
        frame->translation[1] = cartesian->y;
        frame->translation[2] = cartesian->z;

        double tmp[3];
        int i;

        turtle_ecef_from_horizontal(geodetic->latitude, geodetic->longitude,
            90 + declination, 0, tmp);
        for (i = 0; i < 3; i++)
                frame->matrix[i][0] = tmp[i];

        turtle_ecef_from_horizontal(geodetic->latitude, geodetic->longitude,
            declination, -inclination, tmp);
        for (i = 0; i < 3; i++)
                frame->matrix[i][1] = tmp[i];

        turtle_ecef_from_horizontal(geodetic->latitude, geodetic->longitude,
            0, 90 - inclination, tmp);
        for (i = 0; i < 3; i++)
                frame->matrix[i][2] = tmp[i];
}
