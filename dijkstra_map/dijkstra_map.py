import numpy as np
from _dijkstra_map import build_map


class DijkstraMap:

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

    def set_square_sources(self, center, radius, distance=0):
        imin = max(0, center[0] - radius)
        imax = min(center[0] + radius + 1, self.walkable.shape[0])
        jmin = max(0, center[1] - radius)
        jmax = min(center[1] + radius + 1, self.walkable.shape[1])
        if center[0] - radius >= 0:
            self.dmap[center[0] - radius, jmin:jmax] = np.where(
                self.walkable[center[0] - radius, jmin:jmax],
                distance, self.initial)
        if center[0] + radius < self.walkable.shape[0]:
            self.dmap[center[0] + radius, jmin:jmax] = np.where(
                self.walkable[center[0] + radius, jmin:jmax],
                distance, self.initial)
        if center[1] - radius >= 0:
            self.dmap[imin:imax, center[1] - radius] = np.where(
                self.walkable[imin:imax, center[1] - radius],
                distance, self.initial)
        if center[1] + radius < self.walkable.shape[1]:
            self.dmap[imin:imax, center[1] + radius] = np.where(
                self.walkable[imin:imax, center[1] + radius],
                distance, self.initial)
