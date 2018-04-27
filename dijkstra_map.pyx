import numpy as np
cimport numpy as np


def build_map(long [:, :] dmap, np.uint8_t [:, :] walkable, 
              long goal=0, long initial=999):
    cdef bint updated = True
    while updated:
        updated = update(dmap, walkable, goal, initial)
    return np.array(dmap)

def update(long [:, :] dmap, np.uint8_t [:, :] walkable, 
           long goal=0, long initial=999):
    cdef Py_ssize_t i, j
    cdef bint updated = False
    for i in range(dmap.shape[0]):
        for j in range(dmap.shape[1]):
            if walkable[i, j] and dmap[i, j] == initial:
                updated = update_entry(i, j, dmap, initial) or updated
    return updated 

def update_entry(Py_ssize_t i, Py_ssize_t j, long [:, :] dmap, long initial):
    cdef long u = initial
    cdef long d = initial
    cdef long l = initial
    cdef long r = initial
    cdef long new = initial

    if i > 0 and dmap[i - 1, j] != initial:
        l = dmap[i - 1, j] + 1
    if i < dmap.shape[0] - 1 and dmap[i + 1, j] != initial:
        r = dmap[i + 1, j] + 1
    if j > 0 and dmap[i, j - 1] != initial:
        d = dmap[i, j - 1] + 1
    if j < dmap.shape[1] - 1 and dmap[i, j + 1] != initial:
        u = dmap[i, j + 1] + 1

    new = min(u, d, l, r)
    dmap[i, j] = new
    if new != initial:
        return True
    else:
        return False
