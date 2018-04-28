import numpy as np
cimport numpy as np
cimport cython


def build_map(dmap, walkable, initial=999):
    if dmap.shape != walkable.shape:
        raise ValueError(f"dmap (shape {dmap.shape}) and walkable "
                         f"(shape {walkable.shape}) must have the same shape.")
    dmap = dmap.astype(np.float64, copy=False)
    walkable = walkable.astype(np.uint8, copy=False)
    return _build_map(dmap, walkable, initial)


def _build_map(double [:, :] dmap,
               np.uint8_t [:, :] walkable, 
               double initial=999):
    cdef bint updated = True
    while updated:
        updated = _update_map(dmap, walkable, initial)
    return np.array(dmap)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef bint _update_map(double [:, :] dmap,
                      np.uint8_t [:, :] walkable, 
                      double initial=999):
    cdef Py_ssize_t i, j
    cdef bint updated = False
    for i in range(dmap.shape[0]):
        for j in range(dmap.shape[1]):
            if walkable[i, j]:
                updated = _update_entry(i, j, dmap, initial) or updated
    return updated 

@cython.boundscheck(False)
@cython.wraparound(False)
cdef bint _update_entry(Py_ssize_t i, Py_ssize_t j,
                        double [:, :] dmap,
                        double initial):
    cdef double current = dmap[i, j]
    cdef double u = initial
    cdef double d = initial
    cdef double l = initial
    cdef double r = initial
    cdef double lu = initial
    cdef double ld = initial
    cdef double ru = initial
    cdef double rd = initial
    cdef double new = initial

    if i > 0 and current >= dmap[i - 1, j] + 2 :
        l = dmap[i - 1, j] + 1
    if i < dmap.shape[0] - 1 and current >= dmap[i + 1, j] + 2:
        r = dmap[i + 1, j] + 1
    if j > 0 and current >= dmap[i, j - 1] + 2:
        d = dmap[i, j - 1] + 1
    if j < dmap.shape[1] - 1 and current >= dmap[i, j + 1] + 2:
        u = dmap[i, j + 1] + 1
    # Diagonals
    if i > 0 and j > 0 and current >= dmap[i - 1, j] + 2:
        ld = dmap[i - 1, j - 1] + 1
    if i > 0 and j < dmap.shape[1] - 1 and current >= dmap[i - 1, j + 1] + 2:
        lu = dmap[i - 1, j + 1] + 1
    if i < dmap.shape[1] - 1 and j > 0 and current >= dmap[i + 1, j - 1] + 2:
        rd = dmap[i + 1, j - 1] + 1
    if (i < dmap.shape[1] - 1 and j < dmap.shape[1] - 1 and
        current >= dmap[i + 1, j + 1] + 2):
        ru = dmap[i + 1, j + 1] + 1

    new = min(u, d, l, r, ld, lu, rd, ru)
    if new <= current:
        dmap[i, j] = new
        return 1
    else:
        return 0
