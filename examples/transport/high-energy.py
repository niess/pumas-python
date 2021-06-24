import numpy
import pumas

# Simulation settings
n_events = 100000
energy_min, energy_max = 1E-02, 1E+06
distance = 1E+03
mode = {
    'energy_loss' : 'detailed',
    'direction' : 'backward',
    'scattering' : 'fullspace'
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
    '''Sample the Gaisser primary muon flux
    '''
    states.weight *= 0.14E+04 * states.energy**(-2.7) * (
        1 / (1 + 1.1 * states.energy / 115) +
        0.054 / (1 + 1.1 * states.energy / 850))

# Create the array of Monte Carlo states
states = pumas.StateArray(n_events)

prng = simulation.random
states.randomise_energy(energy_min, energy_max, mode = 'log', prng = prng)

# Sample the flux and transport the Monte Carlo states
if simulation.direction == 'forward':
    sample_flux(states)

simulation.transport(states)

if simulation.direction == 'backward':
    sample_flux(states)

# Compute the transmitted flux
K = (states.energy <= energy_min) | (states.energy >= energy_max)
states.weight[K] = 0

mu = numpy.mean(states.weight)
sigma = numpy.std(states.weight) / numpy.sqrt(n_events)

print(f'flux = {mu:.5E} +- {sigma:.5E} m^{-2} s^{-1} sr^{-1}')
