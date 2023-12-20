from day_processing import Day
from collections import deque


class Day16(Day):
    def _name(self):
        return "--- Day 16: The Floor Will Be Lava ---"

    def _file(self):
        return "data/input_16.txt"

    def _get_next_pos(self, np, c):
        next_positions = []
        if np[2] == ">":
            if (c == "." or c == "-") and np[0] + 1 < len(self.lines[-1]):
                next_positions.append((np[0] + 1, np[1], ">"))
            elif c == "\\" and np[1] + 1 < len(self.lines):
                next_positions.append((np[0], np[1] + 1, "v"))
            elif c == "/" and np[1] - 1 >= 0:
                next_positions.append((np[0], np[1] - 1, "^"))
            elif c == "|":
                if np[1] - 1 >= 0:
                    next_positions.append((np[0], np[1] - 1, "^"))
                if np[1] + 1 < len(self.lines):
                    next_positions.append((np[0], np[1] + 1, "v"))

        if np[2] == "<":
            if (c == "." or c == "-") and np[0] - 1 >= 0:
                next_positions.append((np[0] - 1, np[1], "<"))
            elif c == "\\" and np[1] - 1 >= 0:
                next_positions.append((np[0], np[1] - 1, "^"))
            elif c == "/" and np[1] + 1 < len(self.lines):
                next_positions.append((np[0], np[1] + 1, "v"))
            elif c == "|":
                if np[1] - 1 >= 0:
                    next_positions.append((np[0], np[1] - 1, "^"))
                if np[1] + 1 < len(self.lines):
                    next_positions.append((np[0], np[1] + 1, "v"))

        if np[2] == "^":
            if (c == "." or c == "|") and np[1] - 1 >= 0:
                next_positions.append((np[0], np[1] - 1, "^"))
            elif c == "\\" and np[0] - 1 >= 0:
                next_positions.append((np[0] - 1, np[1], "<"))
            elif c == "/" and np[0] + 1 < len(self.lines[-1]):
                next_positions.append((np[0] + 1, np[1], ">"))
            elif c == "-":
                if np[0] - 1 >= 0:
                    next_positions.append((np[0] - 1, np[1], "<"))
                if np[0] + 1 < len(self.lines[-1]):
                    next_positions.append((np[0] + 1, np[1], ">"))

        if np[2] == "v":
            if (c == "." or c == "|") and np[1] + 1 < len(self.lines):
                next_positions.append((np[0], np[1] + 1, "v"))
            elif c == "\\" and np[0] + 1 < len(self.lines[-1]):
                next_positions.append((np[0] + 1, np[1], ">"))
            elif c == "/" and np[0] - 1 >= 0:
                next_positions.append((np[0] - 1, np[1], "<"))
            elif c == "-":
                if np[0] - 1 >= 0:
                    next_positions.append((np[0] - 1, np[1], "<"))
                if np[0] + 1 < len(self.lines[-1]):
                    next_positions.append((np[0] + 1, np[1], ">"))
        return next_positions

    def _get_score(self, start_pos):
        visited = set()
        pos = set()
        next_positions = deque([start_pos])
        while next_positions:
            np = next_positions.pop()
            if np in visited:
                continue  # We found a cycle
            visited.add(np)
            pos.add((np[0], np[1]))
            c = self.lines[np[1]][np[0]]
            next_positions.extend(self._get_next_pos(np, c))
        return len(pos)

    def _process(self):
        self.prnt_a(self._get_score((0, 0, ">")))
        best = 0
        for i in range(len(self.lines[-1])):
            best = max(best, self._get_score((i, 0, "v")))
            best = max(best, self._get_score((i, len(self.lines) - 1, "^")))
        for j in range(len(self.lines)):
            best = max(best, self._get_score((0, j, ">")))
            best = max(best, self._get_score((len(self.lines[-1]) - 1, j, "<")))
        self.prnt_b(best)


if __name__ == "__main__":
    Day16().run()
