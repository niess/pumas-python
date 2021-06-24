from cffi import FFI
import io
import os
from pcpp.preprocessor import Preprocessor
from tempfile import TemporaryDirectory


PUMAS_C = os.path.join('pumas', 'c')
SOURCES = (
    'pumas.c',
    os.path.join('pumas', 'extensions.c'),
    os.path.join('pumas', 'vectorization.c')
)
HEADERS = (
    'pumas.h',
    os.path.join('pumas', 'extensions.h'),
    os.path.join('pumas', 'vectorization.h')
)


def load_headers(*paths):
    '''
    Load the given header file(s) and run a C preprocessor.
    '''
    headers = []
    for path in paths:
        with open(os.path.join(PUMAS_C, 'include', path)) as f:
            header_content = f.read()

        header_content = header_content.replace('#include <stdio.h>',
            'struct FILE;')
        header_content = header_content.replace('#include "pumas.h"', '')

        cpp = Preprocessor()
        cpp.parse(header_content)
        output = io.StringIO()
        cpp.write(output)

        headers.append(output.getvalue())
    return os.linesep.join(headers)


def load_sources(*paths):
    '''
    Load the given source file(s).
    '''
    sources = []
    for path in paths:
        with open(os.path.join(PUMAS_C, 'src', path)) as f:
            sources.append(f.read())
    return os.linesep.join(sources)


ffi = FFI()
ffi.set_source('pumas.libpumas', load_sources(*SOURCES),
    extra_compile_args=['-std=c99', f'-I{PUMAS_C}/include'])
ffi.cdef(load_headers(*HEADERS))


if __name__ == '__main__':
    ffi.compile(verbose=True)
