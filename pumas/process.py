from .core import pcall
from .libpumas import ffi, lib

import numbers
import numpy
import sys

__all__ = ('Bremsstrahlung', 'BremsstrahlungABB', 'BremsstrahlungKKP',
    'BremsstrahlungSSR', 'Elastic', 'Electronic', 'PairProduction',
    'PairProductionKKP', 'PairProductionSSR', 'Photonuclear',
    'PhotonuclearBBKS', 'PhotonuclearBM', 'PhotonuclearDRSS',
    'RadiativeProcess')


def __getattr__(name):
    '''Wrap attributes getter in order to create lazy link(s) for default
       radiative model(s)
    '''

    processes = {
        'Bremsstrahlung': lib.PUMAS_PROCESS_BREMSSTRAHLUNG,
        'PairProduction': lib.PUMAS_PROCESS_PAIR_PRODUCTION,
        'Photonuclear': lib.PUMAS_PROCESS_PHOTONUCLEAR
    }

    try:
        process = processes[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    model = ffi.string(lib.pumas_dcs_default(process)).decode()
    this = sys.modules[__name__]
    cls = getattr(this, name + model)
    setattr(this, name, cls)

    return cls


class Elastic:
    '''Elastic collisions with atoms
    '''

    name = 'Elastic'

    @staticmethod
    def dcs(Z, A, mass, energy, mu):
        '''DCS for elastic collisions
        '''
        if isinstance(q, numbers.Number):
            return lib.pumas_elastic_dcs(Z, A, mass, energy, mu)
        else:
            qs = numpy.asarray(q, dtype='f8')
            n = qs.size
            values = numpy.empty(n, dtype='f8')
            dcs = ffi.addressof(lib, 'pumas_elastic_dcs')
            lib.pumas_dcs_call_v(dcs, Z, A, mass, energy, n,
                ffi.cast('double *', qs.ctypes.data),
                ffi.cast('double *', values.ctypes.data))
            return values

    @classmethod
    def transport_path(cls, Z, A, mass, energy):
        '''First transport path for elastic collisions
        '''
        return cls._path(1, Z, A, mass, energy)

    @classmethod
    def free_path(cls, Z, A, mass, energy):
        '''Mean free path for elastic collisions
        '''
        return cls._path(0, Z, A, mass, energy)

    @staticmethod
    def _path(order, Z, A, mass, energy):
        if isinstance(energy, numbers.Number):
            return lib.pumas_elastic_length(order, Z, A, mass, energy)
        else:
            energies = numpy.asarray(energy, dtype='f8')
            n = energies.size
            values = numpy.empty(n, dtype='f8')
            lib.pumas_elastic_path_v(order, Z, A, mass, n,
                ffi.cast('double *', energies.ctypes.data),
                ffi.cast('double *', values.ctypes.data))
            return values


class Electronic:
    '''Inelastic collisions with atomic electrons
    '''

    name = 'Electronic'

    @staticmethod
    def dcs(Z, I, mass, energy, q):
        '''Effective DCS for close collisions
        '''
        if isinstance(q, numbers.Number):
            return lib.pumas_electronic_dcs(Z, I, mass, energy, q)
        else:
            qs = numpy.asarray(q, dtype='f8')
            n = qs.size
            values = numpy.empty(n, dtype='f8')
            dcs = ffi.addressof(lib, 'pumas_electronic_dcs')
            lib.pumas_dcs_call_v(dcs, Z, I, mass, energy, n,
                ffi.cast('double *', qs.ctypes.data),
                ffi.cast('double *', values.ctypes.data))
            return values

    @staticmethod
    def density_effect():
        pass

    @staticmethod
    def stopping_power():
        pass


class RadiativeProcess:
    '''Generic wrapper for a radiative process
    '''

    _dcs = None

    @classmethod
    def dcs(cls, Z, A, mass, energy, q):
        '''Call the default DCS
        '''
        if cls._dcs is None:
            cls._dcs = cls._wrap_dcs()
        return cls._dcs(Z, A, mass, energy, q)

    @classmethod
    def range(cls, Z, mass, energy):
        '''Get the DCS kinematic range
        '''
        r = ffi.new('double[2]')
        lib.pumas_dcs_range(cls.process, Z, mass, energy, r, r + 1)
        return (float(r[0]), float(r[1]))

    @classmethod
    def _wrap_dcs(cls):
        try:
            model_b = cls.model.encode()
        except AttributeError:
            model_b = cls.model

        dcs = ffi.new('pumas_dcs_t *[1]')
        pcall(lib.pumas_dcs_get, cls.process, model_b, dcs)
        dcs = dcs[0]

        def dcs_wrapper(Z, A, mass, energy, q):
            '''Wrapper for calling a C-defined DCS
            '''
            if isinstance(q, numbers.Number):
                return dcs(Z, A, mass, energy, q)
            else:
                qs = numpy.asarray(q, dtype='f8')
                n = qs.size
                values = numpy.empty(n, dtype='f8')
                lib.pumas_dcs_call_v(dcs, Z, A, mass, energy, n,
                    ffi.cast('double *', qs.ctypes.data),
                    ffi.cast('double *', values.ctypes.data))
                return values

        return dcs_wrapper


class BremsstrahlungABB(RadiativeProcess):
    '''ABB parametrization of the bremsstrahlung process

       References:
         Andreev, Bezrukov & Bugaev, Physics of Atomic Nuclei 57 (1994) 2066.
    '''
    name = 'BremsstrahlungABB'
    process = lib.PUMAS_PROCESS_BREMSSTRAHLUNG
    model = 'ABB'


class BremsstrahlungKKP(RadiativeProcess):
    '''KKP parametrization of the bremsstrahlung process

       References:
         Kelner, Kokoulin & Petrukhin, Moscow Engineering Physics Inst.,
         Moscow, 1995.
    '''
    name = 'BremsstrahlungKKP'
    process = lib.PUMAS_PROCESS_BREMSSTRAHLUNG
    model = 'KKP'


class BremsstrahlungSSR(RadiativeProcess):
    '''SSR parametrization of the bremsstrahlung process

       References:
         Sandrock, Soedingresko & Rhode, ICRC 2019 [arXiv:1910.07050].
    '''
    name = 'BremsstrahlungSSR'
    process = lib.PUMAS_PROCESS_BREMSSTRAHLUNG
    model = 'SSR'


class PairProductionKKP(RadiativeProcess):
    '''KKP parametrization of the e+e- pair production process

       References:
         Kelner, Kokoulin & Petrukhin, Soviet Journal of Nuclear Physics 7
           (1968) 237.
    '''
    name = 'PairProductionKKP'
    process = lib.PUMAS_PROCESS_PAIR_PRODUCTION
    model = 'KKP'


class PairProductionSSR(RadiativeProcess):
    '''SSR parametrization of the e+e- pair production process

       References:
         Sandrock, Soedingresko & Rhode, ICRC 2019 [arXiv:1910.07050].
    '''
    name = 'PairProductionSSR'
    process = lib.PUMAS_PROCESS_PAIR_PRODUCTION
    model = 'SSR'


class PhotonuclearBBKS(RadiativeProcess):
    '''BBKS parametrization of the photonuclear process

       References:
         Bezrukov, Bugaev, Sov. J. Nucl. Phys. 33 (1981), 635.
         Kokoulin, Nucl. Phys. B Proc. Sup. 70 (1999) 475.
         Bugaev & Shlepin, Phys.Rev. D67 (2003) 034027.
    '''
    name = 'PhotonuclearBBKS'
    process = lib.PUMAS_PROCESS_PHOTONUCLEAR
    model = 'BBKS'


class PhotonuclearBM(RadiativeProcess):
    '''BM parametrization of the photonuclear process

       References:
         Butkevich & Mikheyev, Soviet Journal of Experimental and Theoretical
           Physics 95 (2002) 11.
    '''
    name = 'PhotonuclearBM'
    process = lib.PUMAS_PROCESS_PHOTONUCLEAR
    model = 'BM'


class PhotonuclearDRSS(RadiativeProcess):
    '''DRSS parametrization of the photonuclear process

       References:
         Dutta, Reno, Sarcevic & Seckel, Phys.Rev. D63 (2001) 094020
           [arXiv:hep-ph/0012350].
    '''
    name = 'PhotonuclearDRSS'
    process = lib.PUMAS_PROCESS_PHOTONUCLEAR
    model = 'DRSS'
