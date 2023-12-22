import re
from day_processing import Day
from collections import deque
import copy


class Brick:
    def __init__(self, coords):
        self.coords = coords

    def __lt__(self, other):
        return self.coords[2] <= other.coords[2]


class Day22(Day):
    def _name(self):
        return "--- Day 22: Sand Slabs ---"

    def _file(self):
        return "data/input_22.txt"

    def _process(self):
        rg_brick = re.compile(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)")

        # Occupancy: (x,y,z) -> brick_id
        occupancy = {}
        is_supported_by = {}
        bricks = []
        for line in self.lines:
            m = rg_brick.findall(line)
            bricks.append(Brick([int(c) for c in m[0]]))
        bricks.sort()
        for brick, b_id in zip(bricks, range(len(bricks))):
            x_min = brick.coords[0]
            y_min = brick.coords[1]
            x_max = brick.coords[3] + 1
            y_max = brick.coords[4] + 1
            z_start = brick.coords[2]
            hits = []
            while z_start > 0:
                hits = [(x, y, z_start) for x in range(x_min, x_max) for y in range(y_min, y_max)
                        if (x, y, z_start) in occupancy]
                if len(hits) > 0:
                    break
                z_start -= 1
            final_z = z_start+1
            is_supported_by[b_id] = {occupancy[h] for h in hits}
            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    for z in range(final_z, final_z + (brick.coords[5] - brick.coords[2]) + 1):
                        occupancy[(x, y, z)] = b_id

        brick_being_solo_support = set()
        for k, v in is_supported_by.items():
            if len(v) == 1:
                brick_being_solo_support.update(v)
        self.prnt_a(len(bricks) - len(brick_being_solo_support))

        star_b = 0
        for b_id in range(len(bricks)):
            q = deque()
            q.append(b_id)
            support = copy.deepcopy(is_supported_by)
            visited = set()
            while q:
                new_b_id = q.pop()
                for k in support:
                    if new_b_id not in support[k]:
                        continue
                    support[k].remove(new_b_id)
                    if k not in visited and len(support[k]) == 0:
                        visited.add(k)
                        q.append(k)
            star_b += len(visited)
        self.prnt_b(star_b)


if __name__ == "__main__":
    Day22().run()
