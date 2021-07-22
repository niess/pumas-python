from .core import pcall
from .libpumas import ffi, lib
from .medium import Medium

import numpy
import weakref


class Context:
    '''Wrapper for a `pumas_context` object
    '''

    _ENERGY_LOSS_STR = None
    _ENERGY_LOSS_IDX = None

    def __init__(self, physics, **kwargs):
        # Create the simulation context
        self._physics = physics

        c = ffi.new('struct pumas_context *[1]')
        pcall(lib.pumas_context_create, c, physics._c,
            ffi.sizeof('struct pumas_user_data'))

        weakref.finalize(c, lib.pumas_context_destroy, c)
        self._c = c[0]

        c[0].medium = ffi.addressof(lib, 'pumas_geometry_medium')
        user_data = ffi.cast('struct pumas_user_data *', c[0].user_data)
        user_data.top = ffi.NULL
        user_data.current = ffi.NULL
        user_data.callback = ffi.NULL

        # Set the mappings
        if self._ENERGY_LOSS_STR is None:
            d_idx = {'disabled': None, 'csda': None, 'mixed': None,
                'straggled': None}
            d_str = {}
            for k in d_idx.keys():
                i = getattr(lib, f'PUMAS_MODE_{k.upper()}')
                d_idx[k] = i
                d_str[i] = k

            self._ENERGY_LOSS_IDX = d_idx
            self._ENERGY_LOSS_STR = d_str

        # Initialise the geometry ref
        self._geometry = None

        # Set any extra arguments
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def accuracy(self):
        return self._c.accuracy

    @accuracy.setter
    def accuracy(self, v):
        self._c.accuracy = v

    @property
    def decay(self):
        if self._c.mode.decay == lib.PUMAS_MODE_DISABLED:
            return 'disabled'
        elif self._c.mode.decay == lib.PUMAS_MODE_WEIGHTED:
            return 'weighted'
        else:
            return 'randomised'

    @decay.setter
    def decay(self, v):
        if v == 'disabled':
            self._c.mode.decay = lib.PUMAS_MODE_DISABLED
        elif v == 'weighted':
            self._c.mode.decay = lib.PUMAS_MODE_WEIGHTED
        elif v == 'randomised':
            self._c.mode.decay = lib.PUMAS_MODE_RANDOMISED
        else:
            raise ValueError(f"bad decay mode ('{v}')")

    @property
    def direction(self):
        if self._c.mode.direction == lib.PUMAS_MODE_FORWARD:
            return 'forward'
        else:
            return 'backward'

    @direction.setter
    def direction(self, v):
        if v == 'forward':
            self._c.mode.direction = lib.PUMAS_MODE_FORWARD
        elif v == 'backward':
            self._c.mode.direction = lib.PUMAS_MODE_BACKWARD
        else:
            raise ValueError(f"bad direction mode ('{v}')")

    @property
    def distance_limit(self):
        if self._c.event & lib.PUMAS_EVENT_LIMIT_DISTANCE:
            return self._c.limit.distance
        else:
            return None

    @distance_limit.setter
    def distance_limit(self, v):
        if v is None:
            self._c.limit.distance = 0
            self._c.event &= ~lib.PUMAS_EVENT_LIMIT_DISTANCE
        else:
            self._c.event |= lib.PUMAS_EVENT_LIMIT_DISTANCE
            self._c.limit.distance = v

    @property
    def energy_limit(self):
        if self._c.event & lib.PUMAS_EVENT_LIMIT_ENERGY:
            return self._c.limit.energy
        else:
            return None

    @energy_limit.setter
    def energy_limit(self, v):
        if v is None:
            self._c.limit.energy = 0
            self._c.event &= ~lib.PUMAS_EVENT_LIMIT_ENERGY
        else:
            self._c.event |= lib.PUMAS_EVENT_LIMIT_ENERGY
            self._c.limit.energy = v

    @property
    def energy_loss(self):
        return self._ENERGY_LOSS_STR[self._c.mode.energy_loss]

    @energy_loss.setter
    def energy_loss(self, v):
        try:
            self._c.mode.energy_loss = self._ENERGY_LOSS_IDX[v]
        except KeyError:
            raise ValueError(f"bad energy loss mode ('{v}')")

    @property
    def geometry(self):
        return self._geometry

    @geometry.setter
    def geometry(self, v):
        if self._geometry is v:
            return

        if self._geometry is not None:
            lib.pumas_geometry_destroy(self._c)
        self._geometry = v

    @property
    def grammage_limit(self):
        if self._c.event & lib.PUMAS_EVENT_LIMIT_GRAMMAGE:
            return self._c.limit.grammage
        else:
            return None

    @grammage_limit.setter
    def grammage_limit(self, v):
        if v is None:
            self._c.limit.grammage = 0
            self._c.event &= ~lib.PUMAS_EVENT_LIMIT_GRAMMAGE
        else:
            self._c.event |= lib.PUMAS_EVENT_LIMIT_GRAMMAGE
            self._c.limit.grammage = v

    @property
    def physics(self):
        return self._physics

    def random(self, n=None):
        '''Get pseudo random number(s) from the current stream
        '''
        if (n is None) or (n <= 1):
            return self._c.random(self._c)
        else:
            u = numpy.empty(n, dtype='f8')
            data = ffi.cast('double *', u.ctypes.data)
            lib.pumas_context_random_v(self._c, n, data)
            return u

    @property
    def random_seed(self):
        seed = ffi.new('unsigned long *')
        lib.pumas_context_random_seed_get(self._c, seed)
        return seed[0]

    @random_seed.setter
    def random_seed(self, v):
        seed = ffi.new('unsigned long *', v)
        lib.pumas_context_random_seed_set(self._c, seed)

    @property
    def scattering(self):
        if self._c.mode.scattering == lib.PUMAS_MODE_DISABLED:
            return 'disabled'
        else:
            return 'mixed'

    @scattering.setter
    def scattering(self, v):
        if v == 'disabled':
            self._c.mode.scattering = lib.PUMAS_MODE_DISABLED
        elif v == 'mixed':
            self._c.mode.scattering = lib.PUMAS_MODE_MIXED
        else:
            raise ValueError(f"bad scattering mode ('{v}')")

    @property
    def time_limit(self):
        if self._c.event & lib.PUMAS_EVENT_LIMIT_TIME:
            return self._c.limit.time
        else:
            return None

    @time_limit.setter
    def time_limit(self, v):
        if v is None:
            self._c.limit.time = 0
            self._c.event &= ~lib.PUMAS_EVENT_LIMIT_TIME
        else:
            self._c.event |= lib.PUMAS_EVENT_LIMIT_TIME
            self._c.limit.time = v 

    def transport(self, states):
        '''Transport Monte Carlo state(s)
        '''
        missing = Medium._update(self._physics)
        if missing:
            raise KeyError(f"bad material '{missing.material}'")

        if self._geometry is None:
            raise ValueError("bad geometry 'None'")
        else:
            self._geometry._update(self)

        data = ffi.cast('struct pumas_state *', states.ctypes.data)
        pcall(lib.pumas_context_transport_v, self._c, states.size, data)
