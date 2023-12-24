import re
from day_processing import Day


class HailLine2D:
    def __init__(self, start_pos, v) -> None:
        # ax + by + c = 0
        self.a = -v[1]
        self.b = v[0]
        self.c = - (self.a * start_pos[0] + self.b * start_pos[1])
        self.sp = start_pos
        self.v = v

    def intersect(self, other) -> bool:
        if self.a/self.b == other.a/other.b:
            return False, None
        x = (self.b*other.c - other.b*self.c)/(self.a*other.b - other.a*self.b)
        y = (other.a*self.c - self.a*other.c)/(self.a*other.b - other.a*self.b)
        return True, (x,y)

    def is_future(self, xy):
        v_n = (xy[0] - self.sp[0], xy[1] - self.sp[1])
        return v_n[0]*self.v[0] + v_n[1]*self.v[1] > 0


class Day24(Day):
    def _name(self):
        return "--- Day 24: Never Tell Me The Odds ---"

    def _file(self):
        return "data/input_24.txt"

    def _process(self):
        rg_line = re.compile(r"(\d+), (\d+), (\d+) @ (-?\d+), (-?\d+), (-?\d+)")
        hail_lines = []
        r_min, r_max = (200000000000000, 400000000000001)
        for line in self.lines:
            m = rg_line.findall(line)
            v = [int(c) for c in m[0]]
            hail_lines.append(HailLine2D((v[0], v[1]), (v[3], v[4])))
        star_a = 0
        for i in range(len(hail_lines)):
            hi = hail_lines[i]
            for j in range(i+1, len(hail_lines)):
                hj= hail_lines[j]
                inter, xy = hi.intersect(hj)
                if not inter:
                    continue
                if not(r_min <= xy[0] < r_max and r_min <= xy[1] < r_max):
                    continue
                if hj.is_future(xy) and hi.is_future(xy):
                    star_a += 1
        self.prnt_a(star_a)


if __name__ == "__main__":
    Day24().run()
