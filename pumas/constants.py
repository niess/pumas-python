from .libpumas import ffi, lib

import sys

__all__ = ('AVOGADRO_NUMBER', 'ELECTRON_MASS', 'MUON_C_TAU', 'MUON_MASS',
    'NEUTRON_MASS', 'PROTON_MASS', 'TAU_C_TAU', 'TAU_MASS')


def __getattr__(name):
    try:
        code = getattr(lib, f'PUMAS_CONSTANT_{name}')
    except AttributeError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    value = ffi.new('double *')
    lib.pumas_constant(code, value)
    value = float(value[0])

    this = sys.modules[__name__]
    setattr(this, name, value)

    return value
