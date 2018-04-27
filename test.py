import numpy as np
from dijkstra_map import build_map

dmap = np.full((5, 5), 999)
dmap[1, 1] = 0
walkable = np.ones((5, 5)).astype(np.uint8)

dmap = build_map(dmap, walkable) 
print(dmap)
