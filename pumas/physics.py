from .core import pcall
from .definitions import MaterialsDescription
from .libpumas import ffi, lib
from .process import RadiativeProcess

from collections import namedtuple
from dataclasses import dataclass, field
import glob
import numbers
import numpy
import os
import tempfile
from typing import ClassVar, NamedTuple
import weakref

__all__ = ('Material', 'Physics', 'TabulatedData')


class Physics:
    '''Wrapper for a `pumas_physics` object
    '''

    def __init__(self, materials, path=None, particle=None, settings=None,
                 **kwargs):
        if isinstance(materials, MaterialsDescription):
            if path is None:
                with tempfile.TemporaryDirectory(prefix='pumas') as tmpdir:
                    c = self._from_description(
                        materials, tmpdir, particle, settings, **kwargs)
            else:
                c = self._from_description(
                    materials, path, particle, settings, **kwargs)
        elif isinstance(materials, str):
            if materials.endswith('.xml'):
                c = self._from_mdf(
                    materials, path, particle, settings, **kwargs)
            elif materials.endswith('.pumas'):
                c = self._from_dump(materials)
            else:
                # Attempt to load the physics from a binary dump
                if os.path.isdir(materials):
                    for match in glob.iglob(os.path.join(materials, '*.pumas')):
                        materials = match
                        c = self._from_dump(materials)
                        break
                    else:
                        for match in glob.iglob(
                            os.path.join(materials, '*.xml')):

                            materials = match
                            c = self._from_mdf(
                                materials, path, particle, settings, **kwargs)
                            break
                        else:
                            raise ValueError(
                                f"could not locate physics in '{materials}'")

        weakref.finalize(c, lib.pumas_physics_destroy, c)
        self._c = c[0]
        self._materials = None

    def _from_description(self, materials, path, particle, settings, **kwargs):
        # Create the physics from a MD
        os.makedirs(path, exist_ok=True)
        mdf = os.path.join(path, 'materials.xml')
        materials.dump(mdf)
        return self._from_mdf(mdf, path, particle, settings, **kwargs)

    def _from_mdf(self, materials, path, particle, settings, **kwargs):
        # Create the physics from a MDF
        if path is None:
            path = os.path.dirname(materials)

        if particle is None:
            particle = lib.PUMAS_PARTICLE_MUON
        else:
            try:
                particle = getattr(lib,
                    f'PUMAS_PARTICLE_{particle.upper()}')
            except:
                raise IndexError(f"bad particle ('{particle}')")

        if settings is None:
            if kwargs:
                settings = PhysicsSettings(**kwargs) # Keep this in scope
                c_settings = settings._c
            else:
                c_settings = ffi.NULL
        else:
            if kwargs:
                settings = settings.copy(**kwargs)
            c_settings = settings._c

        try:
            materials = materials.encode()
        except AttributeError:
            pass

        try:
            path = path.encode()
        except AttributeError:
            pass

        c = ffi.new('struct pumas_physics *[1]')
        pcall(lib.pumas_physics_create,
            c, particle, materials, path, c_settings)
        return c

    def _from_dump(self, materials):
        with open(materials, 'rb') as f:
            c = ffi.new('struct pumas_physics *[1]')
            pcall(lib.pumas_physics_load, c, f)
            return c

    @property
    def cutoff(self):
        try:
            return self._cutoff
        except AttributeError:
            self._cutoff = lib.pumas_physics_cutoff(self._c)
            return self._cutoff

    @property
    def materials(self):
        if self._materials is None:
            n = lib.pumas_physics_material_length(self._c)
            materials = n * [None]

            c_str = ffi.new('char *[1]')
            for i in range(n):
                lib.pumas_physics_material_name(self._c, i, c_str)
                name = ffi.string(c_str[0]).decode()
                materials[i] = Material(self, name)

            PhysicsMaterials = namedtuple('PhysicsMaterials',
                [v.name for v in materials])
            self._materials = PhysicsMaterials(*materials)

        return self._materials


    def dump(self, path):
        if os.path.isdir(path):
            path = os.path.join(path, 'materials.pumas')

        with open(path, 'wb+') as f:
            lib.pumas_physics_dump(self._c, f)


class PhysicsSettings:
    '''Wrapper for a `pumas_physics_settings` object
    '''

    def __init__(self, **kwargs):
        c = ffi.new('struct pumas_physics_settings [1]')
        self._c = c
        self.update(**kwargs)

    def copy(self, **kwargs):
        try:
            energies = self._energies
        except AttributeError:
            energies = None

        c = self._c[0]
        copy = self.__class__(
            cutoff = c.cutoff,
            elastic_ratio = c.elastic_ratio,
            energies = energies,
            update = c.update,
            dry = c.dry,
            bremsstrahlung = c.bremsstrahlung,
            pair_production = c.pair_production,
            photonuclear = c.photonuclear
        )

        if kwargs:
            copy.update(**kwargs)

        return copy

    def update(self, cutoff=None, elastic_ratio=None, energies=None,
               update=False, dry=False, bremsstrahlung=None,
               pair_production=None, photonuclear=None):

        c = self._c[0]

        if cutoff is not None:
            c.cutoff = cutoff

        if elastic_ratio is not None:
            c.elastic_ratio = elastic_ratio

        if energies is not None:
            n = len(energies)
            c.n_energies = n
            energies = ffi.new(f'double [{n}]', energies)
            self._energies = energies # Keep reference alive
            c.energy = energies

        c.update = update
        c.dry = dry

        def set_dcs(process, value):
            if value is None:
                return

            if isinstance(value, RadiativeProcess):
                value = bremsstrahlung.model

            setattr(c, process, value)

        set_dcs('bremsstrahlung', bremsstrahlung)
        set_dcs('pair_production', pair_production)
        set_dcs('photonuclear', photonuclear)


class TabulatedData(NamedTuple):
    '''Wrapper for physics tabulation
    '''

    kinetic_energy: numpy.ndarray
    transport_path: numpy.ndarray
    stopping_power: numpy.ndarray


@dataclass
class Material:
    '''Proxy for a tabulated material
    '''

    physics: Physics
    '''Physics instance of the material
    '''

    name: str
    '''Label of the material
    '''

    index: int = field(init=False)
    '''Material index in the physics tables
    '''

    _data: None = field(init=False, repr=False)
    '''Tabulated data
    '''

    _mode : ClassVar[dict] = {
        'csda': lib.PUMAS_MODE_CSDA,
        'disabled': lib.PUMAS_MODE_DISABLED,
        'mixed': lib.PUMAS_MODE_MIXED,
        'straggled': lib.PUMAS_MODE_STRAGGLED
    }

    def __post_init__(self):
        try:
            name = self.name.encode()
        except AttributeError:
            name = self.name

        physics = self.physics._c
        index = ffi.new('int *')
        pcall(lib.pumas_physics_material_index, physics, name, index)
        self.index = int(index[0])

        self._data = None
        self._density = None

    @property
    def data(self):
        if self._data is None:
            physics = self.physics._c
            n = lib.pumas_physics_table_length(physics)
            data = TabulatedData(*[numpy.empty(n) for _ in
                range(len(TabulatedData._fields))])
            self._data = data

            lib.pumas_physics_table_value_v(physics,
                lib.PUMAS_PROPERTY_KINETIC_ENERGY, 0, self.index,
                ffi.cast('double *', data.kinetic_energy.ctypes.data))
            lib.pumas_physics_table_value_v(physics,
                lib.PUMAS_PROPERTY_TRANSPORT_PATH, 0, self.index,
                ffi.cast('double *',
                    data.transport_path.ctypes.data))
            lib.pumas_physics_table_value_v(physics,
                lib.PUMAS_PROPERTY_STOPPING_POWER, 0, self.index,
                ffi.cast('double *', data.stopping_power.ctypes.data))

        return self._data

    @property
    def density(self):
        if self._density is None:
            physics = self.physics._c
            d = ffi.new('double[1]')
            lib.pumas_physics_material_properties(physics, self.index, ffi.NULL,
                d, ffi.NULL, ffi.NULL, ffi.NULL)
            self._density = float(d[0])

        return self._density

    def elastic_cutoff_angle(self, energy):
        '''Cutoff angle for hard elastic events, in rad
        '''
        return self._property(lib.pumas_physics_property_elastic_cutoff_angle,
            lib.pumas_physics_property_elastic_cutoff_angle_v, energy, False)

    def elastic_path(self, energy):
        '''Mean free path for elastic collisions
        '''
        return self._property(lib.pumas_physics_property_elastic_path,
            lib.pumas_physics_property_elastic_path_v, energy, False)

    def energy_straggling(self, energy):
        '''Energy loss straggling per unit mass of the material
        '''
        return self._property(lib.pumas_physics_property_energy_straggling,
            lib.pumas_physics_property_energy_straggling_v, energy, False)

    def kinetic_energy(self, range_, mode=None):
        '''CSDA energy, in GeV, for a given range, in kg / m^2
        '''
        return self._property(lib.pumas_physics_property_kinetic_energy,
            lib.pumas_physics_property_kinetic_energy_v, range_, mode)

    def transport_path(self, energy, mode=None):
        '''Multiple scattering length per unit mass of the material
        '''
        return self._property(
            lib.pumas_physics_property_transport_path,
            lib.pumas_physics_property_transport_path_v, energy,
            mode)

    def range(self, energy, mode=None):
        '''CSDA range per unit mass of the material
        '''
        return self._property(lib.pumas_physics_property_range,
            lib.pumas_physics_property_range_v, energy, mode)

    def proper_time(self, energy, mode=None):
        '''Total proper time for continuous energy loss
        '''
        return self._property(lib.pumas_physics_property_proper_time,
            lib.pumas_physics_property_proper_time_v, energy, mode)

    def stopping_power(self, energy, mode=None):
        '''Average energy loss per unit mass of the material
        '''
        return self._property(lib.pumas_physics_property_stopping_power,
            lib.pumas_physics_property_stopping_power_v, energy, mode)

    def _property(self, property_s, property_v, energy, mode):
        '''Wrapper for physics properties of materials
        '''
        if mode is None:
            mode = lib.PUMAS_MODE_CSDA
        elif mode:
            mode = self._mode[mode]

        physics = self.physics._c

        if isinstance(energy, numbers.Number):
            value = ffi.new('double *')
            if mode is not False:
                pcall(property_s, physics, mode, self.index, energy, value)
            else:
                pcall(property_s, physics, self.index, energy, value)
            return value[0]
        else:
            energies = numpy.asarray(energy, dtype='f8')
            n = int(energies.size)
            values = numpy.empty(n, dtype='f8')
            if mode is not False:
                pcall(property_v, physics, mode, self.index, n,
                    ffi.cast('double *', energies.ctypes.data),
                    ffi.cast('double *', values.ctypes.data))
            else:
                pcall(property_v, physics, self.index, n,
                    ffi.cast('double *', energies.ctypes.data),
                    ffi.cast('double *', values.ctypes.data))
            return values
