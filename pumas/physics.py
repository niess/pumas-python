from .core import pcall
from .definitions import MaterialsDescription
from .libpumas import ffi, lib

from collections import namedtuple
from dataclasses import dataclass, field
import glob
import numbers
import numpy
import os
import tempfile
from typing import ClassVar, NamedTuple
import weakref


class Physics:
    '''Wrapper for a `pumas_physics` object
    '''

    def __init__(self, materials, path=None, particle=None, settings=None):
        if isinstance(materials, MaterialsDescription):
            if path is None:
                with tempfile.TemporaryDirectory(prefix='pumas') as tmpdir:
                    c = self._from_description(
                        materials, tmpdir, particle, settings)
            else:
                c = self._from_description(materials, path, particle, settings)
        elif isinstance(materials, str):
            if materials.endswith('.xml'):
                c = self._from_mdf(materials, path, particle, settings)
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
                                materials, path, particle, settings)
                            break
                        else:
                            raise ValueError(
                                f"could not locate physics in '{materials}'")

        weakref.finalize(c, lib.pumas_physics_destroy, c)
        self._c = c[0]
        self._materials = None

    def _from_description(self, materials, path, particle, settings):
        # Create the physics from a MD
        os.makedirs(path, exist_ok=True)
        mdf = os.path.join(path, 'materials.xml')
        materials.dump(mdf)
        return self._from_mdf(mdf, path, particle, settings)

    def _from_mdf(self, materials, path, particle, settings):
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
            settings = ffi.NULL

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
            c, particle, materials, path, settings)
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


class TabulatedData(NamedTuple):
    '''Wrapper for physics tabulation
    '''

    kinetic_energy: numpy.ndarray
    multiple_scattering_length: numpy.ndarray
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
        'detailed': lib.PUMAS_MODE_DETAILED,
        'hybrid': lib.PUMAS_MODE_HYBRID,
        'virtual': lib.PUMAS_MODE_VIRTUAL
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
                lib.PUMAS_PROPERTY_MULTIPLE_SCATTERING_LENGTH, 0, self.index,
                ffi.cast('double *',
                    data.multiple_scattering_length.ctypes.data))
            lib.pumas_physics_table_value_v(physics,
                lib.PUMAS_PROPERTY_ENERGY_LOSS, 0, self.index,
                ffi.cast('double *', data.stopping_power.ctypes.data))

        return self._data

    def elastic_cutoff_angle(self, energy):
        '''Cutoff angle for hard elastic events, in rad
        '''
        return self._property(lib.pumas_physics_property_elastic_cutoff_angle,
            lib.pumas_physics_property_elastic_cutoff_angle_v, energy, False)

    def energy_straggling(self, energy):
        '''Energy loss straggling per unit mass of the material
        '''
        return self._property(lib.pumas_physics_property_energy_straggling,
            lib.pumas_physics_property_energy_straggling_v, energy, False)

    def multiple_scattering_length(self, energy, mode=None):
        '''Multiple scattering length per unit mass of the material
        '''
        return self._property(
            lib.pumas_physics_property_multiple_scattering_length,
            lib.pumas_physics_property_multiple_scattering_length_v, energy,
            mode)

    def range(self, energy, mode=None):
        '''CSDA range per unit mass of the material
        '''
        return self._property(lib.pumas_physics_property_grammage,
            lib.pumas_physics_property_grammage_v, energy, mode)

    def proper_time(self, energy, mode=None):
        '''Total proper time for continuous energy loss
        '''
        return self._property(lib.pumas_physics_property_proper_time,
            lib.pumas_physics_property_proper_time_v, energy, mode)

    def stopping_power(self, energy, mode=None):
        '''Average energy loss per unit mass of the material
        '''
        return self._property(lib.pumas_physics_property_energy_loss,
            lib.pumas_physics_property_energy_loss_v, energy, mode)

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
