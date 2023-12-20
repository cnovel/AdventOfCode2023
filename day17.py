from day_processing import Day
from heapq import heappop, heappush

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)


class Day17(Day):
    def _name(self):
        return "--- Day 17: Clumsy Crucible ---"

    def _file(self):
        return "data/input_17.txt"

    def get_neigh(self, curr, ultra):
        if ultra:
            max_moves = 10
            min_moves = 4
        else:
            max_moves = 3
            min_moves = None

        h = len(self.lines)
        w = len(self.lines[-1])
        (y, x, direction, nb_moves) = curr
        neigh = []
        for new_dir in [EAST, WEST, NORTH, SOUTH]:
            (new_y, new_x) = (y + new_dir[0], x + new_dir[1])
            if not (0 <= new_y < h and 0 <= new_x < w):
                continue

            if direction == new_dir:
                new_direction_moves = nb_moves + 1
            else:
                new_direction_moves = 1

            # Max move condition
            if new_direction_moves > max_moves:
                continue

            # Min move condition before turning if ultra
            if min_moves and new_dir != direction and nb_moves < min_moves:
                continue

            # No reversing
            if (new_dir[0] * -1, new_dir[1] * -1) == direction:
                continue

            neigh.append((new_y, new_x, new_dir, new_direction_moves))
        return neigh

    def dijkstra(self, ultra: bool):
        h = len(self.lines)
        w = len(self.lines[-1])
        start = (0, 0)
        end = (w - 1, h - 1)
        dist = {}
        q = []

        # In q, I store (cost, (y, x, direction, nb_moves))
        for direction in [EAST, SOUTH]:
            heappush(q, (0, (*start, direction, 0)))
        while q:
            (cost, curr) = heappop(q)
            if curr in dist:  # We already know the optimal cost for this position/direction/moves
                continue
            dist[curr] = cost  # Save optimal cost

            for n in self.get_neigh(curr, ultra):
                new_cost = cost + int(self.lines[n[0]][n[1]])
                # Either we have not yet encounter n or we found a better way to encounter it
                if n not in dist or new_cost < dist[curr]:
                    heappush(q, (new_cost, n))

        return min([c for ((y, x, _dir, _moves), c) in dist.items() if (x, y) == end])

    def _process(self):
        self.prnt_a(self.dijkstra(False))
        self.prnt_b(self.dijkstra(True))


if __name__ == "__main__":
    Day17().run()
