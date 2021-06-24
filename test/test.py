from pumas import Context, InfiniteGeometry, Physics, StateArray, UniformMedium


physics = Physics('../pumas-luajit/share/materials/examples')
context = Context(physics, accuracy=0.1, random_seed=1, energy_loss='hybrid',
    direction='backward', scattering='longitudinal', decay='stable')
print(context.accuracy, context.random_seed, context.energy_loss,
    context.direction, context.scattering, context.decay)

context.distance_limit = 1
print(context.distance_limit, context._c.event)

medium = UniformMedium('StandardRock')
geometry = InfiniteGeometry(medium)
context.geometry = geometry

states = StateArray(10)
print(type(states[1]))
states[:3]['energy'] = 3
context.transport(states)
print(states.energy)
