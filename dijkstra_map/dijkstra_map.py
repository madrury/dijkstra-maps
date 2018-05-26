import numpy as np
from _dijkstra_map import build_map


class DijskstraMap:

    def __init__(self, walkable, initial=999):
        self.walkable = walkable.astype(np.uint8)
        self.dmap = np.full(self.walkable.shape, initial).astype(np.float)
        self.initial = initial

    def build(self):
        self.dmap = build_map(self.dmap, self.walkable, initial=self.initial)

    def set_source(self, position, *, distance=0):
        x, y = position
        if not self.walkable[x, y]:
            raise ValueError("Cannot set value in dmap at non-walkable space")
        self.dmap[x, y] = distance

    def set_sources(self, *positions, distance=0):
        for position in positions:
            self.set_source(position, distance=0)
