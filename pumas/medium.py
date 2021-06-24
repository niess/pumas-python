from .libpumas import ffi, lib

import weakref


class Medium:
    '''Base wrapper for `pumas_medium` objects
    '''

    _last_physics = None
    '''Reference to the last physics object in use
    '''

    _media = []
    '''Weak-references to existing media instances
    '''

    def __init__ (self, ctype, material, name):
        self._c = ffi.new(ctype)
        self.material = material
        self.name = name
        self._media.append(weakref.ref(self))

    @classmethod
    def _update(cls, physics):
        '''Update the material indices for the given physics
        '''
        if cls._last_physics is physics:
            return None

        dead, missing = [], None
        index = ffi.new('int *')
        for ref in cls._media:
            medium = ref()
            if medium is None:
                dead.append(ref)
                continue

            material = medium.material
            if material and (material != 'Transparent'):
                try:
                    material = material.encode()
                except AttributeError:
                    pass

                rc = lib.pumas_physics_material_index(
                    physics._c, material, index)
                if rc != lib.PUMAS_RETURN_SUCCESS:
                    missing = medium
                    break
                else:
                    m = ffi.cast('struct pumas_medium *', medium._c)
                    m.material = index[0]

        cls._last_physics = physics

        if dead:
            for ref in dead:
                cls._media.remove(ref)

        return missing


class UniformMedium(Medium):
    '''Medium with uniform properties
    '''

    def __init__(self, material, density=None, magnet=None, name=None):
        if density is None:
            density = 0

        if magnet is None:
            magnet = ffi.NULL

        super().__init__('struct pumas_medium_uniform *', material, name)
        lib.pumas_medium_uniform_initialise(self._c, -1, density, magnet)
