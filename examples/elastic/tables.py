import matplotlib.pyplot as plot
import numpy
from pumas import Physics


physics = Physics('../pumas/examples/data')
rock = physics.materials.StandardRock
energy = rock.data.kinetic_energy[1:]

plot.figure()
plot.plot(energy, rock.elastic_cutoff_angle(energy), 'k-')
plot.xscale('log')
plot.yscale('log')

plot.figure()
plot.plot(energy, rock.transport_path(energy), 'k-')
plot.plot(energy, rock.elastic_path(energy), 'k:')
plot.plot(energy, rock.range(energy), 'k--')
plot.xscale('log')
plot.yscale('log')

plot.show()
