#! /usr/bin/env python3
import matplotlib.pyplot as plot
import numpy
from pumas import Physics


physics = Physics('../pumas/examples/data')
rock = physics.materials.StandardRock

e = numpy.logspace(numpy.log10(rock.data.kinetic_energy[1]),
    numpy.log10(rock.data.kinetic_energy[-1]), 1000)

plot.figure()
plot.plot(rock.data.kinetic_energy, rock.data.stopping_power, 'k.',
    label='tabulation')
plot.plot(e, rock.stopping_power(e), 'r-', label='interpolation')
plot.xscale('log')
plot.yscale('log')
plot.xlabel('kinetic energy (GeV)')
plot.ylabel('stopping power, $S$ (GeV m$^2$ / kg)')
plot.legend(loc=2)

plot.figure()
plot.plot(rock.data.kinetic_energy, rock.data.multiple_scattering_length, 'k.',
    label='tabulation')
plot.plot(e, rock.multiple_scattering_length(e), 'r-', label='interpolation')
plot.xscale('log')
plot.yscale('log')
plot.xlabel('kinetic energy (GeV)')
plot.ylabel('First transport path length (m$^2$ / kg)')
plot.legend(loc=2)

plot.show()
