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

    def _get_neigh(self, pos, h, w, max_cost):
        n = []
        for d in [NORTH, EAST, SOUTH, WEST]:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if not max_cost and not (0 <= new_pos[0] < w and 0 <= new_pos[1] < h):
                continue
            e = (new_pos[0] % w, new_pos[1] % h)
            if self.lines[e[1]][e[0]] == "#":
                continue
            n.append(new_pos)
        return n

    def _dijkstra(self, start, max_cost=None):
        h = len(self.lines)
        w = len(self.lines[-1])
        dist = {}
        q = []
        # In q, (cost, (x,y))
        heappush(q, (0, start))
        while q:
            (cost, pos) = heappop(q)
            if pos in dist:
                continue
            dist[pos] = cost
            for n in self._get_neigh(pos, h, w, max_cost):
                new_cost = cost + 1
                if max_cost and new_cost > max_cost:
                    continue
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
        dist = self._dijkstra(start, None)
        self.prnt_a(len([x for x in dist.values() if x <= moves and x % 2 == r]))

        # It actually fits a quadratic equation, thanks Reddit
        moves = 26501365
        seen_states = []
        mod = moves % h
        n = moves // h
        # We need the first 3 terms to get the equation
        for run in [mod, mod + h, mod + h * 2]:
            r = run % 2
            dist = self._dijkstra(start, run)
            seen_states.append(len([x for x in dist.values() if x <= moves and x % 2 == r]))

        y0 = seen_states[0]
        y1 = seen_states[1]
        y2 = seen_states[2]
        a = (y2 + y0 - 2 * y1) / 2
        b = y1 - y0 - a
        c = y0

        self.prnt_b(int(a*n**2 + b*n + c))


if __name__ == "__main__":
    Day21().run()
