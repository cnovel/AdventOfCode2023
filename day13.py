from day_processing import Day
import multiprocessing


class Pattern:
    def __init__(self, lines, v_axis_to_remove = set(), h_axis_to_remove = set()) -> None:
        self.lines = lines.copy()
        self.v_axis = v_axis_to_remove
        self.h_axis = h_axis_to_remove
        self.score_a = 0
        self.score_b = 0

    def get_vertical_axis(self):
        possible_axis = set([i for i in range(len(self.lines[0]))])
        possible_axis -= self.v_axis
        for line in self.lines:
            for i in [x for x in range(len(line)) if x in possible_axis]:
                a = line[0:i][::-1]
                b = line[i:]
                if len(a) == 0 or len(b) == 0:
                    possible_axis.remove(i)
                    continue
                if len(a) <= len(b):
                    if not b.startswith(a):
                        possible_axis.remove(i)
                else:
                    if not a.startswith(b):
                        possible_axis.remove(i)
        return possible_axis

    def get_horizontal_axis(self):
        lines = []
        for i in range(len(self.lines[0])):
            s = ""
            for j in range(len(self.lines)):
                s += self.lines[j][i]
            lines.append(s)
        return Pattern(lines, self.h_axis).get_vertical_axis()

    def score(self):
        s = 0
        for a in self.get_horizontal_axis():
            s += 100*a
        for a in self.get_vertical_axis():
            s += a
        self.score_a = s
        return s

    def get_smudge_score(self):
        h_axis = self.get_horizontal_axis()
        v_axis = self.get_vertical_axis()
        for j in range(len(self.lines)):
            for i in range(len(self.lines[0])):
                new_lines = self.lines.copy()
                t = list(new_lines[j])
                t[i] = '.' if t[i] == '#' else '#'
                new_lines[j] = ''.join(t)
                s = Pattern(new_lines, v_axis, h_axis).score()
                if s > 0:
                    self.score_b = s
                    return s
        return 0


def compute_score(p):
    return p.score()


def compute_smudge(p):
    return p.get_smudge_score()


class Day13(Day):
    def _name(self):
        return "--- Day 13: Point of Incidence ---"

    def _file(self):
        return "data/input_13.txt"

    def _process(self):
        patterns = []
        lines = []
        for l in self.lines:
            l = l.strip("\n")
            if len(l) == 0:
                patterns.append(Pattern(lines))
                lines.clear()
            else:
                lines.append(l)
        patterns.append(Pattern(lines))

        pool = multiprocessing.Pool(4)
        print("Day 13 - Star 1:", sum(pool.map(compute_score, patterns)))
        print("Day 13 - Star 2:", sum(pool.map(compute_smudge, patterns)))


if __name__ == "__main__":
    Day13().run()
