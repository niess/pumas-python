#include <signal.h>

#include "pumas/extensions.h"
#include "pumas/vectorization.h"


/* Manage system signals during long computations */
enum signal_code {
        SIGNAL_CATCH = -1,
        SIGNAL_RAISE = -2
};

static int signum = 0;

static void signal_handler(int code)
{
        static sighandler_t sigint_handler = SIG_IGN;

        if (code == SIGNAL_CATCH) {
                /* Substitute the runtime signal handler(s) */
                sigint_handler = signal(SIGINT, signal_handler);
        } else if (code == SIGNAL_RAISE) {
                /* Restore the original signal handler(s) */
                signal(SIGINT, sigint_handler);

                if (signum) {
                        const int tmp = signum;
                        signum = 0;
                        raise(tmp); /* Forward the signal */
                }
        } else {
                /* Update the signal flag */
                signum = code;
        }
}


/* Vectorization of the transport */
enum pumas_return pumas_context_transport_v(struct pumas_context * context,
    size_t n_states, struct pumas_state * states)
{
        signal_handler(SIGNAL_CATCH);

        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        struct pumas_state * state;
        size_t i;
        for (i = 0, state = states; (i < n_states) && !signum; i++, state++) {
                struct pumas_state_extended extended;
                memcpy(&extended, state, sizeof(*state));
                pumas_state_extended_reset(&extended, context);

                rc = pumas_context_transport(context,
                    &extended.base, NULL, NULL);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;

                memcpy(state, &extended, sizeof(*state));
        }

        signal_handler(SIGNAL_RAISE);

        return rc;
}


/* Vectorization of random numbers generation */
void pumas_context_random_v(
    struct pumas_context * context, size_t n, double * data)
{
        size_t i;
        double * d;
        for (i = 0, d = data; i < n; i++, d++) {
                *d = context->random(context);
        }
}


/* Vectorization of DCS calls */
void pumas_dcs_call_v(pumas_dcs_t * dcs, double Z, double A, double mass,
    double energy, size_t n, double * qs, double * values)
{
        double * q, * value;
        size_t i;
        for (i = 0, q = qs, value = values; i < n; i++, q++, value++) {
                *value = dcs(Z, A, mass, energy, *q);
        }
}


/* Vectorization of the elastic path */
void pumas_elastic_path_v(int order, double Z, double A, double mass,
    size_t n, double * energies, double * values)
{
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                *value = pumas_elastic_length(
                    order, Z, A, mass, *energy);
        }
}


/* Vectorization of the elastic cutoff angle */
enum pumas_return pumas_physics_property_elastic_cutoff_angle_v(
    const struct pumas_physics * physics, int material, size_t n,
    double * energies, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                rc = pumas_physics_property_elastic_cutoff_angle(physics,
                    material, *energy, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}


/* Vectorization of the energy loss computation */
enum pumas_return pumas_physics_property_energy_loss_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                rc = pumas_physics_property_energy_loss(physics,
                    scheme, material, *energy, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}


/* Vectorization of the energy straggling computation */
enum pumas_return pumas_physics_property_energy_straggling_v(
    const struct pumas_physics * physics, int material, size_t n,
    double * energies, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                rc = pumas_physics_property_energy_straggling(physics,
                    material, *energy, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}


/* Vectorization of the grammage range computation */
enum pumas_return pumas_physics_property_grammage_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                rc = pumas_physics_property_grammage(physics,
                    scheme, material, *energy, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}

/* Vectorization of the multiple scattering length computation */
enum pumas_return pumas_physics_property_multiple_scattering_length_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                rc = pumas_physics_property_multiple_scattering_length(physics,
                    scheme, material, *energy, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}

/* Vectorization of the proper time computation */
enum pumas_return pumas_physics_property_proper_time_v(
    const struct pumas_physics * physics, enum pumas_mode scheme,
    int material, size_t n, double * energies, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        double * energy, * value;
        size_t i;
        for (i = 0, energy = energies, value = values; i < n;
            i++, energy++, value++) {
                rc = pumas_physics_property_proper_time(physics,
                    scheme, material, *energy, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}

/* Vectorized getter for table values */
enum pumas_return pumas_physics_table_value_v(
    const struct pumas_physics * physics, enum pumas_property property,
    enum pumas_mode scheme, int material, double * values)
{
        enum pumas_return rc = PUMAS_RETURN_SUCCESS;
        const int n = pumas_physics_table_length(physics);
        int i;
        double * value;
        for (i = 0, value = values; i < n; i++, value++) {
                rc = pumas_physics_table_value(
                    physics, property, scheme, material, i, value);
                if (rc != PUMAS_RETURN_SUCCESS)
                        break;
        }

        return rc;
}
