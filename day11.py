from day_processing import Day
import re
import math


def man_dist(g, h):
    return math.fabs(h[0] - g[0]) + math.fabs(h[1] - g[1])


class Day11(Day):
    def _name(self):
        return "--- Day 11: Cosmic Expansion ---"

    def _file(self):
        return "data/input_11.txt"

    def _get_sum_distances(self, offset):
        set_x = set()
        rg_sharp = re.compile("(#)")
        galaxies = []
        offset_y = 0
        for l in self.lines:
            if '#' not in l:
                offset_y += offset
                continue
            g = rg_sharp.finditer(l)
            for m in g:
                galaxies.append((m.start(0), offset_y))
                set_x.add(m.start(0))
            offset_y += 1
        empty_cols = set([x for x in range(len(self.lines[-1])) if x not in set_x])
        galaxies = [(g[0] + (offset - 1) * len([x for x in empty_cols if x < g[0]]), g[1]) for g in galaxies]
        star = 0
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                star += man_dist(galaxies[i], galaxies[j])
        return int(star)

    def _process(self):
        self.prnt_a(self._get_sum_distances(2))
        self.prnt_b(self._get_sum_distances(1000000))


if __name__ == "__main__":
    Day11().run()
