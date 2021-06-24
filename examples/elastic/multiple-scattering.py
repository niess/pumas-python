'''
  Simulate the multiple scattering distribution of muons for some experimental
  configurations

  The following configurations have been implemented:

    1. HYPERON, Akimenko et al. (1996) :
       - 7.3 GeV /c muon beam on a 14.36 cm thick Cu target.

    2. MUSCAT, Attwood et al. (2006) :
       - 172 MeV/c muon beam on 1.5 mm of Al or 0.24 mm of Fe.

  Reference:
    - Akimenko et al. (1996),
      https://doi.org/10.1016/0168-9002(86)90990-3

    - Attwood et al. (2006),
      https://doi.org/10.1016/j.nimb.2006.05.006

  Author: Valentin Niess
'''
import numpy
import pumas
from pumas.constants import MUON_MASS
from pumas.definitions import MaterialsDescription, MaterialsDict
import sys


# Parse the setup from the command line
try:
    setup = sys.argv[1]
except IndexError:
    setup = 'Al'

# Build the scattering target
density = None
if setup == 'Cu':
    # Akimenko et al. (1984)
    material, thickness, momentum = 'Copper', 1.436E-02, 7.3
    edges = (0, 1E-03, 2E-03, 3E-03, 4E-03, 5E-03, 6E-03, 7E-03, 8E-03, 9E-03,
        13E-03, 17E-03, 21E-03, 25E-03, 29E-03, 7.)
else:
    # Attwood et al. (2006)
    edges = (0, 0.00269, 0.00895, 0.0162, 0.0248, 0.0347, 0.0463, 0.0597,
        0.0754, 0.0938, 0.1151, 7.)
    momentum = 0.172

    if setup == 'Al':
        material, thickness = 'Aluminum', 1.5E-03
    elif setup == 'Fe':
        material, thickness = 'Iron', 0.24E-03
    elif setup == 'H2':
        material, thickness, density = 'LiquidHydrogen', 109E-03, 0.0755E+03
    else:
        raise ValueError(f"bad setup '{setup}'")


def Box(center, hx, hy, hz):
    '''Helper function for creating data for an axis aligned box
    '''
    x0, y0, z0 = center
    return (
        (x0 + hx, 0, 0,  1,  0,  0),
        (0, y0 + hy, 0,  0,  1,  0),
        (0, 0, z0 + hz,  0,  0,  1),
        (x0 - hx, 0, 0, -1,  0,  0),
        (0, y0 - hy, 0,  0, -1,  0),
        (0, 0, z0 - hz,  0,  0, -1)
    )

medium = pumas.UniformMedium(material, density)
geometry = pumas.PolyhedronGeometry(
    Box((0, 0, 0.5 * thickness), 10, 10, 0.5 * thickness), medium=medium)

# Create the transport engine
simulation = pumas.Context(
    pumas.Physics(MaterialsDescription(materials=MaterialsDict(material))),
    geometry = geometry
)

# Create the array of Monte Carlo states
n_events = 10000000
states = pumas.StateArray(n_events)
states.energy = (momentum**2 + MUON_MASS**2)**0.5 - MUON_MASS

# Run the simulation
simulation.transport(states)

# Histogram the result
if setup == 'Cu':
    rho = numpy.sqrt(states.direction[:,0]**2 + states.direction[:,1]**2)
    theta = numpy.arctan2(rho, states.direction[:,2])
else:
    theta = numpy.arctan2(states.direction[:,1], states.direction[:,2])
    theta = numpy.absolute(theta)

epsilon = 1E-09
K = (states.energy > 0.1E-03) & (states.position[:,2] >= thickness - epsilon)
theta = theta[K]
counts, _ = numpy.histogram(theta, edges)

# Print the result
print('# angle       pdf      uncert.')
print('# (rad)    (rad^-1)   (rad^-1)')
xlow = 0.
for i, xi in enumerate(edges[1:]):
    if setup == 'Cu':
        a = numpy.pi * (xi**2 - xlow**2)
    else:
        a = 2 * (xi - xlow)
    norm = 1. / (n_events * a)
    yi = counts[i]
    xlow = xi
    print('{:.4f}   {:.5E} {:.5E}'.format(
        xi, yi * norm, numpy.sqrt(yi) * norm))
