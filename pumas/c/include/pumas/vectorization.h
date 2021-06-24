#ifndef pumas_vectorization_h
#define pumas_vectorization_h
#ifdef __cplusplus
extern "C" {
#endif

#include "pumas.h"


enum pumas_return pumas_context_transport_v(struct pumas_context * context,
    size_t n_states, struct pumas_state * states);

void pumas_context_random_v(
    struct pumas_context * context, size_t n, double * data);

void pumas_dcs_call_v(pumas_dcs_t * dcs, double Z, double A, double mass,
    double energy, size_t n, double * qs, double * values);

enum pumas_return pumas_physics_property_elastic_cutoff_angle_v(
    const struct pumas_physics * physics, int material, size_t n,
    double * energies, double * values);

void pumas_elastic_path_v(int order, double Z, double A, double mass,
    size_t n, double * energies, double * values);

enum pumas_return pumas_physics_property_energy_loss_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values);

enum pumas_return pumas_physics_property_energy_straggling_v(
    const struct pumas_physics * physics, int material, size_t n,
    double * energies, double * values);

enum pumas_return pumas_physics_property_grammage_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values);

enum pumas_return pumas_physics_property_multiple_scattering_length_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values);

enum pumas_return pumas_physics_property_proper_time_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values);

enum pumas_return pumas_physics_table_value_v(
    const struct pumas_physics * physics, enum pumas_property property,
    enum pumas_mode scheme, int material, double * values);

#ifdef __cplusplus
}
#endif
#endif
