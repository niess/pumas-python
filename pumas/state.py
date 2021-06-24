import numpy

__all__ = ('StateArray',)


class StateArray(numpy.ndarray):
    '''An array of Monte Carlo state(s)
    '''

    _dtype = numpy.dtype([('charge', 'f8'), ('energy', 'f8'),
        ('distance', 'f8'), ('grammage', 'f8'), ('time', 'f8'),
        ('weight', 'f8'), ('position', 'f8', 3), ('direction', 'f8', 3),
        ('decayed', 'i4')], align=True)
    '''NumPy structured array data type
    '''

    def __new__(cls, size, **kwargs):
        obj = super().__new__(cls, size, dtype=cls._dtype, order='C')
        obj.reset(**kwargs)

        return obj

    @property
    def charge(self):
        return self['charge']

    @charge.setter
    def charge(self, v):
        self['charge'] = v

    @property
    def decayed(self):
        return self['decayed']

    @decayed.setter
    def decayed(self, v):
        self['decayed'] = v

    @property
    def direction(self):
        return self['direction']

    @direction.setter
    def direction(self, v):
        self['direction'] = v

    @property
    def distance(self):
        return self['distance']

    @distance.setter
    def distance(self, v):
        self['distance'] = v

    @property
    def energy(self):
        return self['energy']

    @energy.setter
    def energy(self, v):
        self['energy'] = v

    @property
    def grammage(self):
        return self['grammage']

    @grammage.setter
    def grammage(self, v):
        self['grammage'] = v

    @property
    def position(self):
        return self['position']

    @position.setter
    def position(self, v):
        self['position'] = v

    def randomise_charge(self, ratio=None, prng=None):
        '''Randomise the charge according to a given charge ratio
        '''
        if ratio is None:
            # CMS collaboration (2010) [doi.org/10.1016/j.physletb.2010.07.033]
            ratio = 1.2766
        if prng is None:
            prng = numpy.random.rand

        u = prng(self.size)
        p = ratio / (1 + ratio)
        K = u <= p
        self['charge'][K] = 1
        self['weight'][K] *= 1 / p
        K = ~K
        self['charge'][K] = -1
        self['weight'][K] *= 1 / (1 - p)

    def randomise_energy(self, e_min, e_max, mode=None, prng=None):
        '''Randomise the energy over an interval
        '''
        if mode is None:
            mode = 'uniform'
        if prng is None:
            prng = numpy.random.rand

        u = prng(self.size)
        if mode == 'uniform':
            self['energy'] = e_min + (e_max - e_min) * u
            self['weight'] *= e_max - e_min
        elif mode == 'log':
            lne = numpy.log(e_max / e_min)
            e = e_min * numpy.exp(u * lne)
            self['energy'] = e
            self['weight'] *= lne * e

    def reset(self, **kwargs):
        '''Reset the state(s) to default values
        '''
        default = {'charge': -1., 'energy': 1., 'distance': 0., 'grammage': 0.,
            'time': 0., 'weight': 1., 'position': (0., 0., 0.),
            'direction': (0., 0., 1.), 'decayed': 0}
        default.update(kwargs)

        for k, v in default.items():
            self[k] = v

    @property
    def time(self):
        return self['time']

    @time.setter
    def time(self, v):
        self['time'] = v

    @property
    def weight(self):
        return self['weight']

    @weight.setter
    def weight(self, v):
        self['weight'] = v
