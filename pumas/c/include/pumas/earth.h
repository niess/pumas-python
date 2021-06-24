#pragma once
#include "gull.h"
#include "pumas/extensions.h"
#include "turtle.h"


/* Per context data for the Earth geometry */
struct pumas_geometry_earth {
        struct pumas_geometry base;

        struct turtle_stepper * stepper[1];
        struct pumas_medium ** media;
        int n_layers;

        struct {
                double * workspace[1];
                struct gull_snapshot * snapshot[1];
                double distance;
                double last[3];
        } magnet;
};

/* Getters for an Earth geometry */
void pumas_geometry_earth_get(struct pumas_geometry * geometry,
    struct pumas_state * state, struct pumas_medium ** medium_p,
    double * step_p);

double pumas_geometry_earth_magnet(struct pumas_geometry * geometry,
    struct pumas_state * state, double * magnet);

/* Initialiser for the Earth geometry */
void pumas_geometry_earth_reset(struct pumas_geometry * geometry);

/* Finaliser for the Earth geometry */
void pumas_geometry_earth_destroy(struct pumas_geometry * geometry);

/* Altitude projection for vertical gradient media */
double pumas_medium_gradient_project_altitude(
    struct pumas_medium_gradient * medium, struct pumas_state_extended * state);
