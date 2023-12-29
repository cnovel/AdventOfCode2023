import re
from day_processing import Day
import collections


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


Vec3 = collections.namedtuple("Vec3", "x,y,z", defaults = (0, 0, 0))


def cross(a, b):
    return Vec3(a.y*b.z - a.z*b.y, a.z*b.x - a.x*b.z, a.x*b.y - a.y*b.x)


def colinear(a, b) -> bool:
    return all(v == 0 for v in cross(a, b))


def dot(a, b):
    return a.x*b.x + a.y*b.y + a.z*b.z


def sub(a, b):
    return Vec3(a.x-b.x, a.y-b.y, a.z-b.z)


def get_plane(p1, v1, p2, v2):
    p12 = sub(p1, p2)
    v12 = sub(v1, v2)
    vv = cross(v1, v2)
    return (cross(p12, v12), dot(p12, vv))


def lin(r, a, s, b, t, c):
    x = r*a.x + s*b.x + t*c.x
    y = r*a.y + s*b.y + t*c.y
    z = r*a.z + s*b.z + t*c.z
    return Vec3(x, y, z)


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

        points = []
        speeds = []
        for line in self.lines:
            m = [int(c) for c in rg_line.findall(line)[0]]
            points.append(Vec3(m[0], m[1], m[2]))
            speeds.append(Vec3(m[3], m[4], m[5]))

        n = len(points)
        p1, v1 = points[0], speeds[0]
        for i in range(1, n):
            if not colinear(v1, speeds[i]):
                p2, v2 = points[i], speeds[i]
                break
        for j in range(i+1, n):
            if not colinear(v1, speeds[j]) and not colinear(v2, speeds[j]):
                p3, v3 = points[j], speeds[j]

        a, A = get_plane(p1, v1, p2, v2)
        b, B = get_plane(p1, v1, p3, v3)
        c, C = get_plane(p2, v2, p3, v3)

        w = lin(A, cross(b, c), B, cross(c, a), C, cross(a, b))
        t = dot(a, cross(b, c))
        w = Vec3(round(w.x / t), round(w.y / t), round(w.z / t))

        w1 = sub(v1, w)
        w2 = sub(v2, w)
        ww = cross(w1, w2)

        E = dot(ww, cross(p2, w2))
        F = dot(ww, cross(p1, w1))
        G = dot(p1, ww)
        S = dot(ww, ww)

        rock = lin(E, w1, -F, w2, G, ww)
        self.prnt_b(int(sum(rock) / S))



if __name__ == "__main__":
    Day24().run()
