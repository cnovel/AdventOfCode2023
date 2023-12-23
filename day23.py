import re
from day_processing import Day
import json

WEST = (-1, 0)
SOUTH = (0, 1)
EAST = (1, 0)
NORTH = (0, -1)

directions = [WEST, SOUTH, EAST, NORTH]

class Day23(Day):
    def _name(self):
        return "--- Day 23: A Long Walk ---"

    def _file(self):
        return "data/input_23.txt"

    def _get_next_pos(self, cur_pos, prev_pos):
        r = []
        for d in directions:
            np = (cur_pos[0] + d[0], cur_pos[1] + d[1])
            if not (0 <= np[0] < self.w and 0 <= np[1] < self.h):
                continue
            if np == prev_pos:
                continue
            c = self.lines[np[1]][np[0]]
            if c == "#":
                continue
            if c == ">" and d == WEST:
                continue
            if c == "<" and d == EAST:
                continue
            if c == "v" and d == NORTH:
                continue
            if c == "^" and d == SOUTH:
                continue
            r.append(np)
        return r

    def _get_max_path(self, prev_length, cur_pos, prev_pos, end):
        length = prev_length
        while True:
            if cur_pos == end:
                return length
            length += 1
            nps = self._get_next_pos(cur_pos, prev_pos)
            if len(nps) > 1:
                b_a = self._get_max_path(length, nps[0], cur_pos, end)
                b_b = self._get_max_path(length, nps[1], cur_pos, end)
                return max(b_a, b_b)
            prev_pos = cur_pos
            cur_pos = nps[0]


    def _process(self):
        start = None
        end = None
        self.w = len(self.lines[-1])
        self.h = len(self.lines)
        for i in range(self.w):
            if self.lines[0][i] == '.':
                start = (i, 0)
            if self.lines[self.h-1][i] == '.':
                end = (i, self.h-1)
        self.prnt_a(self._get_max_path(0, start, None, end))



if __name__ == "__main__":
    Day23().run()
