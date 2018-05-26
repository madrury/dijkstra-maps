import numpy as np
from _dijkstra_map import build_map


class DijkstraMap:

    def __init__(self, walkable, initial=999):
        self.walkable = walkable.astype(np.uint8)
        self.dmap = np.full(self.walkable.shape, initial).astype(np.float)
        self.initial = initial

    def build(self):
        self.dmap = build_map(self.dmap, self.walkable, initial=self.initial)

    def get_descent_path(self, source):
        path = [source]
        current_position = source
        previous_height = np.inf
        current_height = self.dmap[source]
        while current_height < previous_height:
            previous_height = current_height
            for coord in adjacent_coordinates(current_position):
                if (within_array(self.walkable, coord) 
                    and self.walkable[coord]
                    and self.dmap[coord] < current_height):
                    current_position = coord
                    current_height = self.dmap[coord]
                    path.append(current_position)
                    break
        return path

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


def adjacent_coordinates(center):
    dxdy = [(-1, 1), (0, 1), (1, 1),
            (-1, 0),         (1, 0),
            (-1, -1), (0, -1), (1, -1)]
    return [(center[0] + dx, center[1] + dy) for dx, dy in dxdy]

def within_array(arr, coord):
    return 0 <= coord[0] < arr.shape[0] and 0 <= coord[1] < arr.shape[1]
