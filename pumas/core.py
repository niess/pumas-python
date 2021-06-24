from .libpumas import ffi, lib

import re

__all__ = ('LibraryError', 'pcall')


class LibraryError(Exception):
    '''PUMAS C library error
    '''
    pass



def pcall(function, *args):
    '''Protected library call with exception handling
    '''
    if function(*args) != lib.PUMAS_RETURN_SUCCESS:
        message = ffi.string(lib.pumas_error_get()).decode()

        match = re.search('[^}+]} (.*)$', message)
        if match:
            message = match.group(1)

        raise LibraryError(message)
