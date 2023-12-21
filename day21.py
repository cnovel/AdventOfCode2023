from day_processing import Day
from heapq import heappop, heappush

WEST = (-1, 0)
SOUTH = (0, 1)
EAST = (1, 0)
NORTH = (0, -1)


class Day21(Day):
    def _name(self):
        return "--- Day 21: ??? ---"

    def _file(self):
        return "data/input_21.txt"

    def _get_neigh(self, pos, h, w):
        n = []
        for d in [NORTH, EAST, SOUTH, WEST]:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if not (0 <= new_pos[0] < w and 0 <= new_pos[1] < h):
                continue
            if self.lines[new_pos[1]][new_pos[0]] == "#":
                continue
            n.append(new_pos)
        return n

    def _dijkstra(self, start, start_cost):
        h = len(self.lines)
        w = len(self.lines[-1])
        dist = {}
        q = []
        # In q, (cost, (x,y))
        heappush(q, (start_cost, start))
        while q:
            (cost, pos) = heappop(q)
            if pos in dist:
                continue
            dist[pos] = cost
            for n in self._get_neigh(pos, h, w):
                new_cost = cost + 1
                if n not in dist or new_cost < dist[n]:
                    heappush(q, (new_cost, n))

        return dist

    def _process(self):
        h = len(self.lines)
        w = len(self.lines[-1])

        start = None
        for j in range(h):
            for i in range(w):
                if self.lines[j][i] == "S":
                    start = (i, j)

        moves = 64
        r = moves % 2
        dist = self._dijkstra(start, 0)
        self.prnt_a(len([x for x in dist.values() if x <= moves and x % 2 == r]))


if __name__ == "__main__":
    Day21().run()
