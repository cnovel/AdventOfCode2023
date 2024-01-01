import re
from day_processing import Day
from collections import defaultdict


class Day25(Day):
    def _name(self):
        return "--- Day 25: Snowverload ---"

    def _file(self):
        return "data/input_25.txt"

    def _process(self):
        rg = re.compile("(\w+)")
        edges = []
        for line in self.lines:
            m = rg.findall(line)
            for j in range(1, len(m)):
                edges.append((m[0], m[j]))
                edges.append((m[j], m[0]))

        g = defaultdict(set)
        for e in edges:
            g[e[0]].add(e[1])

        s = set(g)
        count = lambda v: len(g[v] - s)
        while sum(map(count, s)) != 3:
            s.remove(max(s, key=count))
        self.prnt_a(len(s) * len(set(g) - s))
        self.prnt_b("Congrats on completing the AoC 2023!")


if __name__ == "__main__":
    Day25().run()
