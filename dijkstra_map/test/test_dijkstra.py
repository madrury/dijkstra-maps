import pytest
import numpy as np

import dijkstra_map.dijkstra_map
from dijkstra_map.dijkstra_map import DijkstraMap
from _dijkstra_map import build_map


def test_sink():
    walkable = np.ones((5, 5)).astype(np.uint8)
    dm = DijkstraMap(walkable)
    dm.set_source((2, 2))
    dm.build()
    result = np.array([[2, 2, 2, 2, 2],
                       [2, 1, 1, 1, 2], 
                       [2, 1, 0, 1, 2], 
                       [2, 1, 1, 1, 2],
                       [2, 2, 2, 2, 2]])
    assert np.all(dm.dmap == result)

def test_two_sinks():
    walkable = np.ones((3, 5)).astype(np.uint8)
    dm = DijkstraMap(walkable)
    dm.set_sources((1, 1), (1, 3))
    dm.build()
    result = np.array([[1, 1, 1, 1, 1], 
                       [1, 0, 1, 0, 1],
                       [1, 1, 1, 1, 1]])
    assert np.all(dm.dmap == result)

def test_corridor():
    walkable = np.zeros((3, 5)).astype(np.uint8)
    walkable[1, 1:4] = 1
    dm = DijkstraMap(walkable)
    dm.set_source((1, 1))
    dm.build()
    result = np.array([[999, 999, 999, 999, 999], 
                       [999, 0,   1,   2,   999],
                       [999, 999, 999, 999, 999]])
    assert np.all(dm.dmap == result)

def test_cross():
    walkable = np.zeros((7, 7)).astype(np.uint8)
    walkable[3, 1:6] = 1
    walkable[1:6, 3] = 1
    dm = DijkstraMap(walkable)
    dm.set_source((3, 3))
    dm.build()
    result = np.array([[999, 999, 999, 999, 999, 999, 999], 
                       [999, 999, 999, 2,   999, 999, 999],
                       [999, 999, 999, 1,   999, 999, 999],
                       [999, 2,   1,   0,   1,   2,   999],
                       [999, 999, 999, 1,   999, 999, 999],
                       [999, 999, 999, 2,   999, 999, 999],
                       [999, 999, 999, 999, 999, 999, 999]])
    assert np.all(dm.dmap == result)

def test_simple_square():
    walkable = np.ones((7, 7)).astype(np.uint8)
    dm = DijkstraMap(walkable)
    dm.set_square_sources((3, 3), 2)
    dm.build()
    result = np.array([
        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.],
        [ 1.,  0.,  0.,  0.,  0.,  0.,  1.],
        [ 1.,  0.,  1.,  1.,  1.,  0.,  1.],
        [ 1.,  0.,  1.,  2.,  1.,  0.,  1.],
        [ 1.,  0.,  1.,  1.,  1.,  0.,  1.],
        [ 1.,  0.,  0.,  0.,  0.,  0.,  1.],
        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.]])
    assert np.all(dm.dmap == result)

#-----------------------------------------------------------------------------
# Private C api
#-----------------------------------------------------------------------------
def test_sink_c():
    dmap = np.full((5, 5), 999)
    dmap[2, 2] = 0
    walkable = np.ones((5, 5)).astype(np.uint8)
    result = np.array([[2, 2, 2, 2, 2],
                       [2, 1, 1, 1, 2], 
                       [2, 1, 0, 1, 2], 
                       [2, 1, 1, 1, 2],
                       [2, 2, 2, 2, 2]])
    dmap = build_map(dmap, walkable) 
    assert np.all(dmap == result)

def test_two_sinks_c():
    dmap = np.full((3, 5), 999)
    dmap[1, 1] = 0
    dmap[1, 3] = 0
    walkable = np.ones((3, 5)).astype(np.uint8)
    result = np.array([[1, 1, 1, 1, 1], 
                       [1, 0, 1, 0, 1],
                       [1, 1, 1, 1, 1]])
    dmap = build_map(dmap, walkable) 
    assert np.all(dmap == result)

def test_corridor_c():
    dmap = np.full((3, 5), 999)
    dmap[1, 1] = 0
    walkable = np.zeros((3, 5)).astype(np.uint8)
    walkable[1, 1:4] = 1
    result = np.array([[999, 999, 999, 999, 999], 
                       [999, 0,   1,   2,   999],
                       [999, 999, 999, 999, 999]])
    dmap = build_map(dmap, walkable) 
    assert np.all(dmap == result)

def test_cross_c():
    dmap = np.full((7, 7), 999)
    dmap[3, 3] = 0
    walkable = np.zeros((7, 7)).astype(np.uint8)
    walkable[3, 1:6] = 1
    walkable[1:6, 3] = 1
    result = np.array([[999, 999, 999, 999, 999, 999, 999], 
                       [999, 999, 999, 2,   999, 999, 999],
                       [999, 999, 999, 1,   999, 999, 999],
                       [999, 2,   1,   0,   1,   2,   999],
                       [999, 999, 999, 1,   999, 999, 999],
                       [999, 999, 999, 2,   999, 999, 999],
                       [999, 999, 999, 999, 999, 999, 999]])
    dmap = build_map(dmap, walkable) 
    assert np.all(dmap == result)
