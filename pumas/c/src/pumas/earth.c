#include "pumas_coordinates.h"
#include "pumas_earth.h"


void pumas_geometry_earth_get(struct pumas_geometry * base_geometry,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p)
{
        struct pumas_geometry_earth * earth = (void *)base_geometry;
        struct pumas_state_extended * extended = (void *)state;
        double elevation[2];
        int index[2];

        turtle_stepper_step(*earth->stepper, state->position, NULL,
            &extended->geodetic.latitude, &extended->geodetic.longitude,
            &extended->geodetic.altitude, elevation, step_p, index);
        extended->geodetic.computed = 1;

        if (medium_p != NULL) {
                if ((index[0] >= 0) && (earth->media != NULL)) {
                        if (earth->n_layers > 1) {
                                *medium_p = ((index[0] < earth->n_layers) &&
                                    (elevation[1] != DBL_MAX)) ?
                                    earth->media[index[0]] : NULL;
                        } else {
                                *medium_p = (extended->geodetic.altitude <
                                             elevation[0]) ?
                                    earth->media[0] :
                                    NULL;
                        }
                } else {
                        *medium_p = NULL;
                }
        }
}


double pumas_geometry_earth_magnet(struct pumas_geometry * base_geometry,
    struct pumas_state * state, double * magnet)
{
#define GEOMAGNET_UPDATE_DISTANCE 1E+03
        struct pumas_geometry_earth * earth = (void *)base_geometry;

        if (state->distance < earth->magnet.distance) {
                memcpy(magnet, earth->magnet.last, sizeof earth->magnet.last);
        } else {
                /* Get geodetic coordinates */
                struct pumas_geodetic_point geodetic_position;
                turtle_ecef_to_geodetic(state->position,
                    &geodetic_position.latitude, &geodetic_position.longitude,
                    &geodetic_position.altitude);

                /* Get the local frame */
                struct pumas_coordinates_unitary_transformation frame;
                struct pumas_cartesian_point ecef_position = {
                    state->position[0], state->position[1], state->position[2]};
                pumas_coordinates_frame_initialise_local(&frame, &ecef_position,
                    &geodetic_position, 0, 0);

                /* Get the local magnetic field (ENU frame) */
                struct pumas_cartesian_vector magnet_enu = {.frame = &frame};
                gull_snapshot_field(*earth->magnet.snapshot,
                    geodetic_position.latitude, geodetic_position.longitude,
                    geodetic_position.altitude, (double *)(&magnet_enu),
                    earth->magnet.workspace);

                /* Transform back to ECEF */
                pumas_coordinates_cartesian_vector_transform(
                    &magnet_enu, NULL);

                /* Update the magnet and its history */
                memcpy(&earth->magnet.last, &magnet_enu,
                    sizeof earth->magnet.last);
                memcpy(magnet, &magnet_enu, sizeof earth->magnet.last);
                earth->magnet.distance = state->distance +
                                         GEOMAGNET_UPDATE_DISTANCE;
        }

        struct pumas_state_extended * extended = (void *)state;

        return GEOMAGNET_UPDATE_DISTANCE / extended->context->accuracy;

#undef GEOMAGNET_UPDATE_DISTANCE
}


void pumas_geometry_earth_reset(struct pumas_geometry * base_geometry)
{
        struct pumas_geometry_earth * earth = (void *)base_geometry;
        earth->magnet.distance = -1;
        memset(earth->magnet.last, 0x0, sizeof earth->magnet.last);
}


void pumas_geometry_earth_destroy(struct pumas_geometry * base_geometry)
{
        struct pumas_geometry_earth * earth = (void *)base_geometry;
        turtle_stepper_destroy(earth->stepper);
        free(*earth->magnet.workspace);
        *earth->magnet.workspace = NULL;
        gull_snapshot_destroy(earth->magnet.snapshot);
        free(base_geometry);
}


double pumas_medium_gradient_project_altitude(
    struct pumas_medium_gradient * medium,
    struct pumas_state_extended * state)
{
#define VERTICAL_UPDATE_DISTANCE 1E+03

        if (!state->geodetic.computed) {
                turtle_ecef_to_geodetic(state->base.position,
                                        &state->geodetic.latitude,
                                        &state->geodetic.longitude,
                                        &state->geodetic.altitude);
                state->geodetic.computed = 1;
        }

        if (state->base.distance >= state->vertical.distance) {
                turtle_ecef_from_horizontal(state->geodetic.latitude,
                                            state->geodetic.longitude, 0, 90,
                                            state->vertical.last);
                state->vertical.distance = state->base.distance +
                    VERTICAL_UPDATE_DISTANCE;
        }
        memcpy(medium->gradient.axis, state->vertical.last,
               sizeof medium->gradient.axis);

        return state->geodetic.altitude;

#undef VERTICAL_UPDATE_DISTANCE
}
