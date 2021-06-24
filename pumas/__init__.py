from .context import Context
from .core import LibraryError
from .geometry import InfiniteGeometry, PolyhedronGeometry
from .libpumas import lib
from .medium import UniformMedium
from .physics import Physics
from .state import StateArray

__all__ = ('Context', 'ffi', 'InfiniteGeometry', 'lib', 'LibraryError',
    'Physics', 'PolyhedronGeometry', 'StateArray', 'UniformMedium')


def _initialise():
    lib.pumas_error_initialise()

_initialise()
