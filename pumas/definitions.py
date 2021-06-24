import copy
from dataclasses import dataclass, field
import numpy
import os
import re
import sys
from typing import Dict

__all__ = ('ElementDefinition', 'elements', 'ElementsDict',
    'MaterialDefinition', 'materials', 'MaterialsDescription', 'MaterialsDict')


def __getattr__(name):
    if name == 'elements':
        from ._elements import data
    elif name == 'materials':
        from ._materials import data
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    this = sys.modules[__name__]
    setattr(this, name, data)

    return data


@dataclass
class ElementDefinition:
    '''
    Data defining an atomic element
    '''
    Z: float
    '''Atomic charge number
    '''

    A: float
    '''Atomic mass number in g/mol
    '''

    I: float
    '''Mean excitation energy, in GeV
    '''


@dataclass
class MaterialDefinition:
    '''
    Data defining a base material
    '''

    density: float
    '''Material density, in kg/m^3
    '''

    elements: Dict[str, float]
    '''Mass weights of constitutive atomic elements
    '''

    I: float = field(default=None)
    '''Mean excitation energy, in GeV
    '''

    ZoA: float = field(init=False)
    '''Ratio of the total electric number over the molar mass, in mol/g
    '''

    def __post_init__(self):
        if self.I:
            self.ZoA = self._compute_ZoA(self.elements)
        else:
            self.ZoA, self.I = self._compute_ZoA_and_I(self.elements)

    @staticmethod
    def _compute_ZoA(elements, elements_db=None):
        if not elements_db:
            this = sys.modules[__name__]
            elements_db = getattr(this, 'elements')

        ZoA = 0.
        for symbol, wi in elements.items():
            e = elements_db[symbol]
            tmp = wi * e.Z / e.A
            ZoA = ZoA + tmp

        return ZoA

    @staticmethod
    def _compute_ZoA_and_I(elements, elements_db=None):
        if not elements_db:
            this = sys.modules[__name__]
            elements_db = getattr(this, 'elements')

        ZoA, mee = 0., 0.
        for symbol, wi in elements.items():
            e = elements_db[symbol]
            tmp = wi * e.Z / e.A
            ZoA += tmp
            mee += tmp * numpy.log(e.I)

        I = numpy.exp(mee / ZoA) * 1.13 # 13% rule, see Groom et al.

        return ZoA, I


class DefinitionsDict(dict):
    '''Specialisation of dict for storing PUMAS materials definitions
    '''

    _default = None
    '''Default definitions
    '''

    def __init__(self, *args, **kwargs):
        self.add(*args, **kwargs)

    def add(self, *args, **kwargs):
        if args:
            if self._default is None:
                try:
                    self._setdefault()
                except AttributeError:
                    raise('no default definitions')
            for arg in args:
                self[arg] = copy.deepcopy(self._default[arg])
        self.update(kwargs)

    def remove(self, *args):
        for arg in args:
            del self[arg]


class ElementsDict(DefinitionsDict):
    '''Specialised dict for storing atomic elements properties
    '''

    @classmethod
    def _setdefault(cls):
        cls._default = sys.modules[__name__].elements


class MaterialsDict(DefinitionsDict):
    '''Specialised dict for storing materials properties
    '''

    @classmethod
    def _setdefault(cls):
        cls._default = sys.modules[__name__].materials


@dataclass
class MaterialsDescription:
    '''Wrapper for Materials Description Files (MDFs)
    '''

    materials : MaterialsDict = field(default=None)
    '''Container for materials data
    '''

    elements : ElementsDict = field(default=None)
    '''Container for atomic elements data
    '''

    composites : Dict[str, Dict[str, float]] = field(default=None)
    '''Container for composite materials data
    '''

    def __post_init__(self):
        self._update()

    def update(self, other=None):
        '''Update the current data
        '''
        self._update()
        if other:
            other._update()
            if other.elements:
                self.elements.update(other.elements)
            if other.materials:
                self.materials.update(other.materials)
            if other.composites:
                self.composites.update(other.composites)

    def _update(self):
        this = sys.modules[__name__]

        # Update the materials
        if self.composites:
            material_names = set()
            for composite in self.composites.values():
                for name in composite.keys():
                    material_names.add(name)

            materials = self.materials or MaterialsDict()
            for name in material_names:
                if name not in materials:
                    materials[name] = copy.deepcopy(this.materials[name])
            if materials:
                self.materials = materials
            else:
                self.materials = None

        # Update the atomic elements
        if self.materials:
            element_names = set()
            for material in self.materials.values():
                for symbol in material.elements.keys():
                    element_names.add(symbol)

            elements = self.elements or ElementsDict()
            for name in element_names:
                if name not in elements:
                    elements[name] = copy.copy(this.elements[name])
            if elements:
                for symbol in elements.keys():
                    if symbol not in element_names:
                        del elements[symbol]
                self.elements = elements
            else:
                self.elements = None

    def dump(self, path=None):
        self._update()

        # Build a sorted list of elements
        if self.elements:
            elements = [(k, len(k), v) for k, v in self.elements.items()]
            elements.sort(key=lambda v: (v[2].Z, v[2].A, v[2].I))
        else:
            elements = None

        # Build a sorted list of base materials
        if self.materials:
            materials = [(k, v) for k, v in self.materials.items()]
            materials.sort()
        else:
            materials = None

        # Build a sorted list of composite materials
        if self.composites:
            composites = [(k, v) for k, v in self.composites.items()]
            composites.sort()
        else:
            composites = None

        # Build the MDF
        xml = ['<pumas>']

        if elements:
            padmax = max(v[1] for v in elements)
            for symbol, n, e in elements:
                align1 = (padmax - n) * ' '
                align2 = '' if e.Z >= 10 else ' '
                align3 = '' if e.A >= 10 else ' '
                align4 = '' if e.I >= 100E-09 else ' '
                pattern = '  <element name="{}"{} Z="{:d}"{} '                 \
                          'A="{:.6f}"{} I="{:.1f}"{} />'
                xml.append(pattern.format(symbol, align1, e.Z, align2, e.A,
                    align3, e.I * 1E+09, align4))

        if materials:
            for name, material in materials:
                xml.append('')

                dedx = self._snakify(name) + '.txt'
                pattern = '  <material name="{}" file="{}" '                   \
                          'density="{:.7g}" I="{:.7g}">'
                xml.append(pattern.format(name, dedx, material.density * 1E-03,
                    material.I * 1E+09))

                elements = [(k, len(k), v, self.elements[k])
                    for k, v in material.elements.items()]
                elements.sort(key=lambda v: (v[3].Z, v[3].A, v[3].I))

                padmax = max(v[1] for v in elements)
                for symbol, n, w, _ in elements:
                    pad = (padmax - n) * ' '
                    pattern = '    <component name="{}"{} fraction="{:.7g}" />'
                    xml.append(pattern.format(symbol, pad, w))
                xml.append('  </material>')

        if composites:
            for name, composite in self.composites.items():
                xml += ['', f'  <composite name="{name}">']

                data = [(k, len(k), v) for k, v in composite.items()]
                data.sort(key=lambda v: v[2])
                padmax = max(v[1] for v in data)
                for material, n, weight in data:
                    pad = (padmax - n) * ' '
                    pattern = '    <component name="{}"{} fraction="{:.7g}" />'
                    xml.append(pattern.format(material, pad, weight))
                xml.append('  </composite>')

        xml += ['</pumas>', '']

        if path is None:
            path = 'materials.xml'

        with open(path, 'w+') as f:
            f.write(os.linesep.join(xml))

    @staticmethod
    def _snakify(camel):
        s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
