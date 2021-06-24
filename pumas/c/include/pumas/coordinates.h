#pragma once
#include "turtle.h"

/* Coordinates objects */
struct pumas_coordinates_unitary_transformation {
    double translation[3];
    double matrix[3][3];
};

struct pumas_cartesian_point {
    double x, y, z;
    struct pumas_coordinates_unitary_transformation * frame;
};

struct pumas_cartesian_vector {
    double x, y, z;
    struct pumas_coordinates_unitary_transformation * frame;
};

struct pumas_spherical_point {
    double r, theta, phi;
    struct pumas_coordinates_unitary_transformation * frame;
};

struct pumas_spherical_vector {
    double norm, theta, phi;
    struct pumas_coordinates_unitary_transformation * frame;
};

struct pumas_geodetic_point {
    double latitude, longitude, altitude;
};

struct pumas_horizontal_vector {
    double norm, elevation, azimuth;
    struct pumas_coordinates_unitary_transformation * frame;
};

/* Coordinates transforms */
void pumas_coordinates_cartesian_point_transform(
    struct pumas_cartesian_point * self,
    const struct pumas_coordinates_unitary_transformation * frame);

void pumas_coordinates_cartesian_vector_transform(
    struct pumas_cartesian_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame);

void pumas_coordinates_horizontal_vector_transform(
    struct pumas_horizontal_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame);

void pumas_coordinates_spherical_point_transform(
    struct pumas_spherical_point * self,
    const struct pumas_coordinates_unitary_transformation * frame);

void pumas_coordinates_spherical_vector_transform(
    struct pumas_spherical_vector * self,
    const struct pumas_coordinates_unitary_transformation * frame);

void pumas_coordinates_cartesian_point_from_geodetic(
    struct pumas_cartesian_point * self,
    const struct pumas_geodetic_point * point);

void pumas_coordinates_cartesian_point_from_spherical(
    struct pumas_cartesian_point * self,
    const struct pumas_spherical_point * point);

void pumas_coordinates_cartesian_vector_from_horizontal(
    struct pumas_cartesian_vector * self,
    const struct pumas_horizontal_vector * vector);

void pumas_coordinates_cartesian_vector_from_spherical(
    struct pumas_cartesian_vector * self,
    const struct pumas_spherical_vector * vector);

void pumas_coordinates_geodetic_point_from_cartesian(
    struct pumas_geodetic_point * self,
    const struct pumas_cartesian_point * point);

void pumas_coordinates_geodetic_point_from_spherical(
    struct pumas_geodetic_point * self,
    const struct pumas_spherical_point * point);

void pumas_coordinates_horizontal_vector_from_cartesian(
    struct pumas_horizontal_vector * self,
    const struct pumas_cartesian_vector * vector);

void pumas_coordinates_horizontal_vector_from_spherical(
    struct pumas_horizontal_vector * self,
    const struct pumas_spherical_vector * vector);

void pumas_coordinates_spherical_point_from_cartesian(
    struct pumas_spherical_point * self,
    const struct pumas_cartesian_point * point);

void pumas_coordinates_spherical_point_from_geodetic(
    struct pumas_spherical_point * self,
    const struct pumas_geodetic_point * point);

void pumas_coordinates_spherical_vector_from_cartesian(
    struct pumas_spherical_vector * self,
    const struct pumas_cartesian_vector * vector);

void pumas_coordinates_spherical_vector_from_horizontal(
    struct pumas_spherical_vector * self,
    const struct pumas_horizontal_vector * vector);

/* Rotation matrix from Euler angles */
void pumas_coordinates_unitary_transformation_from_euler(
    struct pumas_coordinates_unitary_transformation * transformation,
    int n, int * axis, double * angles);

/* Local frame initialiser */
void pumas_coordinates_frame_initialise_local(
    struct pumas_coordinates_unitary_transformation * frame,
    const struct pumas_cartesian_point * cartesian,
    const struct pumas_geodetic_point * geodetic, double declination,
    double inclination);
