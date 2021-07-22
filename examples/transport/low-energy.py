import numpy
import os
import pumas


def simulate(n_events, energy_loss, direction):
    '''Simulate a bunch of muon events
    '''

    # Simulation settings
    energy_min, energy_max = 1E-03, 1E+00
    distance = 1.
    mode = {
        'energy_loss' : energy_loss,
        'direction' : direction,
        'scattering' : 'disabled'
    }

    # Create the simulation
    energy_limit = energy_min if mode['direction'] == 'forward' else energy_max
    limits = {
        'distance_limit' : distance,
        'energy_limit' : energy_limit
    }

    simulation = pumas.Context(
        pumas.Physics('../pumas/examples/data'),
        geometry = pumas.InfiniteGeometry(pumas.UniformMedium('StandardRock')),
        **mode,
        **limits
    )

    def sample_flux(states):
        '''Sample the primary flux model
        '''
        ratio = 1
        K = states.charge > 0
        states.weight[K] *= (energy_max - energy_min) * ratio / (1 + ratio)
        states.weight[~K] *= (energy_max - energy_min) / (1 + ratio)

    # Create the array of Monte Carlo states
    states = pumas.StateArray(n_events)

    prng = simulation.random
    states.randomise_energy(energy_min, energy_max, prng = prng)
    states.randomise_charge(prng = prng)

    # Sample the flux and transport the Monte Carlo states
    if simulation.direction == 'forward':
        sample_flux(states)
    else:
        energies = states.energy.copy()

    simulation.transport(states)

    if simulation.direction == 'backward':
        sample_flux(states)
    else:
        energies = states.energy

    # Compute the transmitted flux
    K = (states.distance < distance) | (energies <= energy_min) |              \
        (energies >= energy_max)
    states.weight[K] = 0

    mu = numpy.mean(states.weight)
    sigma = numpy.std(states.weight) / numpy.sqrt(n_events)

    print(f'probability({energy_loss}, {direction}) = {mu:.5E} +- {sigma:.5E}')

    return mu, sigma, energies, states.weight


if __name__ == '__main__':
    n_events = 100000
    configs = (
        ('straggled', 'forward', 'k-'),
        ('straggled', 'backward', 'r-'),
        ('mixed', 'forward', 'k--'),
        ('mixed', 'backward', 'r--'),
        ('csda', 'forward', 'k:'),
        ('csda', 'backward', 'r:')
    )

    # Prepare the energy grid for histograms
    e_grid = numpy.linspace(0, 0.7, 71)
    x = 0.5 * (e_grid[1:] + e_grid[:-1])
    norm = 1 / ((e_grid[1] - e_grid[0]) * n_events)
    y = numpy.empty((x.size, len(configs)))
    dy = numpy.empty((x.size, len(configs)))

    mu, sigma = numpy.empty(len(configs)), numpy.empty(len(configs))

    for i, config in enumerate(configs):
        mu[i], sigma[i], energies, weights = simulate(n_events, *config[:2])
        n, _ = numpy.histogram(energies, e_grid, weights=weights)
        y[:,i] = n * norm
        dy[:,i] = numpy.sqrt(n) * norm

    with open('low-energy.txt', 'w+') as f:
        f.write('''#
#   E     Forward-straggled     Backward-straggled      Forward-mixed        Backward-mixed         Forward-CSDA          Backward-CSDA
#           Mean      Std         Mean      Std         Mean      Std         Mean    Std           Mean      Std         Mean      Std
# (GeV)       (GeV^{-1})            (GeV^{-1})            (GeV^{-1})            (GeV^{-1})            (GeV^{-1})            (GeV^{-1})
#
''')
        for i, xi in enumerate(x):
            f.write(f'  {xi:.3f}')
            for j in range(len(configs)):
                f.write(f'   {y[i,j]:.3E} {dy[i,j]:.3E}')
            f.write(os.linesep)
