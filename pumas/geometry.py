from .libpumas import ffi, lib

__all__ = ('InfiniteGeometry', 'Geometry', 'PolyhedronGeometry')


class Geometry:
    '''Base wrapper for `pumas_geometry` objects
    '''

    def __init__(self):
        self._daughters = []
        self._mothers = {}
        self._valid = True

    def __getitem__(self, i):
        return self._daughters[i]

    def __setitem__(self, i, v):
        self._check_circular(v)

        # Pop out the existing item
        old = self._daughters[i]
        if v is old:
            return
        self._unregister(old)

        # Replace with the new item
        self._daughters[i] = v
        self._register(v)
        self._invalidate()

    def append(self, v):
        self._check_circular(v)
        self._daughters.append(v)
        self._register(v)
        self._invalidate()

    def insert(self, i, v):
        self._check_circular(v)
        self._daughters.insert(i, v)
        self._register(v)
        self._invalidate()

    def pop(self, pos=-1):
        v = self.daughters.pop(pos)
        self._unregister(v)
        self._invalidate()
        return v

    def remove(self, v):
        self.daughters.remove(v)
        self._unregister(v)
        self._invalidate()

    def _check_circular(self, v):
        circular = self is v

        def check(v):
            if self == v:
                circular = True
                return True

        if not circular:
            self.walk_up(self, check)
        if circular:
            raise ValueError('circular geometry reference')

    def _register(self, v):
        '''Register ownership on a geometry 
        '''
        try:
            v._mothers[self] += 1
        except KeyError:
            v._mothers[self] = 1

    def _unregister(self, v):
        '''Release ownership on a geometry 
        '''
        v._mothers[self] -= 1
        if v._mothers[self] == 0:
            del v._mothers[self]

    @staticmethod
    def walk_up(geometry, f):
        '''Traverse geometry objects from bottom to top
        '''
        for k, v in geometry._mothers.items():
            if f(k, v):
                break
            Geometry.walk_up(k, f)

    def _invalidate(self):
        '''Invalidate a geometry and all its parents
        '''
        def invalidate(v):
            v._valid = False

        self.walk_up(self, invalidate)
        invalidate(self)

    def _update(self, context):
        '''Update the per-context data of a geometry
        '''
        lib.pumas_geometry_reset(context._c)
        if (lib.pumas_geometry_get(context._c) != ffi.NULL) and self._valid:
            return # XXX What is the 1st condition for?

        def set_daughters(mother, c_mother):
            for daughter in mother._daughters:
                c_daughter = daughter._new()
                lib.pumas_geometry_push(c_mother, c_daughter)
                set_daughters(daughter, c_daughter)

        c = self._new()
        set_daughters(self, c)
        lib.pumas_geometry_set(context._c, c)
        self._valid = True


class InfiniteGeometry(Geometry):
    '''Geometry of infinite extension
    '''

    def __init__(self, medium=None):
        super().__init__()
        self._medium = medium

    def _new(self):
        '''Spawn a new C geometry object
        '''
        if self._medium:
            c_medium = ffi.cast('struct pumas_medium *', self._medium._c)
        else:
            c_medium = ffi.NULL
        c = lib.pumas_geometry_infinite_create(c_medium)
        if c == ffi.NULL:
            raise MemoryError('could not allocate geometry')

        return ffi.cast('struct pumas_geometry *', c)


class PolyhedronGeometry(Geometry):
    '''Static geometry made from a hierarchy of polyhedrons
    '''

    def __init__(self, data, medium=None, daughters=None):
        super().__init__()
        self._refs = []
        self._build_polyhedrons((data, medium, daughters), self._refs, 1, 0)

    def _new(self):
        '''Spawn a C geometry reference
        '''
        return ffi.cast('struct pumas_geometry *', self._refs[0])

    @staticmethod 
    def _build_polyhedrons(args, refs, depth, index):
        data = args[0]
        try:
            medium = args[1]
        except IndexError:
            medium = None
        try:
            daughters = args[2]
        except IndexError:
            daughters = None

        n_faces = len(data)
        size = ffi.sizeof('struct pumas_geometry_polyhedron') +                \
            n_faces * ffi.sizeof('struct pumas_polyhedron_face')
        if medium is not None:
            m = ffi.cast('struct pumas_medium *', medium._c)
        else:
            m = ffi.NULL
        mother = lib.pumas_geometry_polyhedron_create(m, n_faces)
        refs.append(mother)
        if medium is not None:
            refs.append(medium)

        for i in range(n_faces):
            d = data[i]
            mother.faces[i].origin[0] = d[0]
            mother.faces[i].origin[1] = d[1]
            mother.faces[i].origin[2] = d[2]
            mother.faces[i].normal[0] = d[3]
            mother.faces[i].normal[1] = d[4]
            mother.faces[i].normal[2] = d[5]

        mother = ffi.cast('struct pumas_geometry *', mother)

        if daughters is not None:
            last_daughter = None
            for i, daughter_args in enumerate(daughters):
                daughter = build_polyhedrons(daughter_args, frame, refs,
                    depth + 1, i)

                if i == 0:
                    mother.daughters = daughter
                else:
                    last_daughter.next = daughter
                daughter.mother = mother
                last_daughter = daughter

        return mother
