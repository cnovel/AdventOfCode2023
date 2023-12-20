from day_processing import Day


class Day10(Day):
    def _name(self):
        return "--- Day 10: Pipe Maze ---"

    def _file(self):
        return "data/input_10.txt"

    def _get_s_eq(self, x, y):
        connect = set()
        if x > 0 and self.lines[y][x-1] in ["-", "L", "F"]:
            connect.add("L")
        if x < len(self.lines[0]) and self.lines[y][x+1] in ["-", "7", "J"]:
            connect.add("R")
        if y > 0 and self.lines[y-1][x] in ["|", "7", "F"]:
            connect.add("U")
        if y < len(self.lines) - 1 and self.lines[y+1][x] in ["|", "J", "L"]:
            connect.add("D")
        if connect == {"L", "R"}:
            return "-"
        if connect == {"U", "D"}:
            return "|"
        if connect == {"L", "U"}:
            return "J"
        if connect == {"L", "D"}:
            return "7"
        if connect == {"R", "U"}:
            return "L"
        return "F"

    def _possible_next_pipes(self, x, y):
        nexts = []

        if self.lines[y][x] == "|":
            return [(x, y-1), (x, y+1)]
        if self.lines[y][x] == "-":
            return [(x+1, y), (x-1, y)]
        if self.lines[y][x] == "L":
            return [(x, y-1), (x+1, y)]
        if self.lines[y][x] == "J":
            return [(x, y-1), (x-1, y)]
        if self.lines[y][x] == "F":
            return [(x+1, y), (x, y+1)]
        if self.lines[y][x] == "7":
            return [(x-1, y), (x, y+1)]

        # Special case: start
        if x > 0 and self.lines[y][x-1] in ["-", "L", "F"]:
            nexts.append((x-1, y))
        if x < len(self.lines[0]) and self.lines[y][x+1] in ["-", "7", "J"]:
            nexts.append((x+1, y))
        if y > 0 and self.lines[y-1][x] in ["|", "7", "F"]:
            nexts.append((x, y-1))
        if y < len(self.lines) - 1 and self.lines[y+1][x] in ["|", "J", "L"]:
            nexts.append((x, y+1))
        return nexts

    def _process(self):
        s_pos = None
        for j in range(len(self.lines)):
            for i in range(len(self.lines[-1])):
                if self.lines[j][i] != "S":
                    continue
                s_pos = (i, j)
                break

        loop = [s_pos, self._possible_next_pipes(s_pos[0], s_pos[1])[0]]
        while True:
            nexts = self._possible_next_pipes(loop[-1][0], loop[-1][1])
            n = nexts[0] if nexts[1] == loop[-2] else nexts[1]
            if n == s_pos:
                break
            loop.append(n)
        self.prnt_a(int(len(loop) / 2))

        # Get S equivalent
        s_eq = self._get_s_eq(s_pos[0], s_pos[1])
        self.lines[s_pos[1]].replace("S", s_eq)

        inside_tiles = 0
        loop = set(loop)
        for j in range(len(self.lines)):
            inside = False
            start = ""
            on_pipe = False
            for i in range(len(self.lines[-1])):
                if (i, j) not in loop:
                    inside_tiles += 1 if inside else 0
                    continue
                c = self.lines[j][i]
                if c in {"F", "L"} and not on_pipe:
                    start = c
                    on_pipe = True
                    continue
                if c in {"7", "J"} and on_pipe:
                    if start == "F" and c == "J":
                        inside = not inside
                    if start == "L" and c == "7":
                        inside = not inside
                    on_pipe = False
                    continue
                if c == "|":
                    inside = not inside
                    continue

        self.prnt_b(inside_tiles)


if __name__ == "__main__":
    Day10().run()
