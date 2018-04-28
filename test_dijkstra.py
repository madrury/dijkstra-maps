import pytest
import numpy as np
from dijkstra_map import build_map

def test_sink():
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

def test_two_sinks():
    dmap = np.full((3, 5), 999)
    dmap[1, 1] = 0
    dmap[1, 3] = 0
    walkable = np.ones((3, 5)).astype(np.uint8)
    result = np.array([[1, 1, 1, 1, 1], 
                       [1, 0, 1, 0, 1],
                       [1, 1, 1, 1, 1]])
    dmap = build_map(dmap, walkable) 
    assert np.all(dmap == result)

def test_corridor():
    dmap = np.full((3, 5), 999)
    dmap[1, 1] = 0
    walkable = np.zeros((3, 5)).astype(np.uint8)
    walkable[1, 1:4] = 1
    result = np.array([[999, 999, 999, 999, 999], 
                       [999, 0,   1,   2,   999],
                       [999, 999, 999, 999, 999]])
    dmap = build_map(dmap, walkable) 
    assert np.all(dmap == result)

def test_cross():
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
