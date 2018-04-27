import numpy as np
from dijkstra_map import build_map

dmap = np.full((5, 5), 999)
dmap[1, 1] = 0
dmap[3, 3] = 0
walkable = np.ones((5, 5)).astype(np.uint8)
walkable[2, 0] = 0
walkable[2, 1] = 0
walkable[2, 3] = 0
walkable[2, 4] = 0

dmap = build_map(dmap, walkable) 
print(dmap)
