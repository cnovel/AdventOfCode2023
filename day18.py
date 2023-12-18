from day_processing import Day
import re


def get_dir(c: str):
    if c == "R":
        return 1, 0
    if c == "D":
        return 0, 1
    if c == "L":
        return -1, 0
    return 0, -1


def get_letter(c: int):
    if c == 0:
        return "R"
    if c == 1:
        return "D"
    if c == 2:
        return "L"
    return "U"


def in_vert(s, mid_y):
    return s[0][1] < mid_y < s[1][1] or s[0][1] > mid_y > s[1][1]


def in_hori(s, mid_x):
    return s[0][0] < mid_x < s[1][0] or s[0][0] > mid_x > s[1][0]


class Day18(Day):
    def _name(self):
        return "--- Day 18: Lavaduct Lagoon ---"

    def _file(self):
        return "data/input_18.txt"

    @staticmethod
    def get_area(instructions):
        pos = (0, 0)
        positions = [pos]
        for i in instructions:
            direction = get_dir(i[0])
            n = int(i[1])
            new_pos = (pos[0] + n*direction[0], pos[1] + n*direction[1])
            pos = new_pos
            positions.append(pos)

        positions = positions[:-1]
        real_pos = []
        for c in range(len(positions)):
            p = (c - 1) % len(positions)
            n = (c + 1) % len(positions)

            pos_c = positions[c]
            pos_p = positions[p]
            pos_n = positions[n]

            # Clockwise
            if pos_p[0] == pos_c[0] and pos_p[1] > pos_c[1] and pos_n[0] > pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append(pos_c)
            elif pos_p[0] < pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] > pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1]))
            elif pos_p[0] == pos_c[0] and pos_p[1] < pos_c[1] and pos_n[0] < pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1] + 1))
            elif pos_p[0] > pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] < pos_c[1]:
                real_pos.append((pos_c[0], pos_c[1] + 1))
            # Counterclockwise
            elif pos_p[0] > pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] > pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1] + 1))
            elif pos_p[0] == pos_c[0] and pos_p[1] < pos_c[1] and pos_n[0] > pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1]))
            elif pos_p[0] < pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] < pos_c[1]:
                real_pos.append(pos_c)
            elif pos_p[0] == pos_c[0] and pos_p[1] > pos_c[1] and pos_n[0] < pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append((pos_c[0], pos_c[1] + 1))

        seg_vert = []
        seg_hor = []
        xs = {0}
        ys = {0}
        for i in range(len(real_pos)):
            p = real_pos[i]
            np = real_pos[(i + 1) % len(real_pos)]
            if p[0] == np[0]:
                seg_vert.append((p, np))
            else:
                seg_hor.append((p, np))
            xs.add(np[0])
            ys.add(np[1])
        xs = sorted(list(xs))
        ys = sorted(list(ys))
        area = 0
        for i in range(len(xs) - 1):
            for j in range(len(ys) - 1):
                dx = xs[i + 1] - xs[i]
                dy = ys[j + 1] - ys[j]
                mid_x = xs[i] + float(dx) / 2.
                mid_y = ys[j] + float(dy) / 2.

                cr = 0
                for v in seg_vert:
                    if in_vert(v, mid_y) and v[0][0] < mid_x:
                        cr += 1
                if cr % 2 == 0:
                    continue
                ct = 0
                for h in seg_hor:
                    if in_hori(h, mid_x) and h[0][1] < mid_y:
                        ct += 1
                if ct % 2 == 0:
                    continue
                area += dx * dy
        return area

    @staticmethod
    def get_area_smart(instructions):
        pos = (0, 0)
        positions = [pos]
        for i in instructions:
            direction = get_dir(i[0])
            n = int(i[1])
            new_pos = (pos[0] + n * direction[0], pos[1] + n * direction[1])
            pos = new_pos
            positions.append(pos)

        positions = positions[:-1]
        real_pos = []
        for c in range(len(positions)):
            p = (c - 1) % len(positions)
            n = (c + 1) % len(positions)

            pos_c = positions[c]
            pos_p = positions[p]
            pos_n = positions[n]

            # Clockwise
            if pos_p[0] == pos_c[0] and pos_p[1] > pos_c[1] and pos_n[0] > pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append(pos_c)
            elif pos_p[0] < pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] > pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1]))
            elif pos_p[0] == pos_c[0] and pos_p[1] < pos_c[1] and pos_n[0] < pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1] + 1))
            elif pos_p[0] > pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] < pos_c[1]:
                real_pos.append((pos_c[0], pos_c[1] + 1))
            # Counterclockwise
            elif pos_p[0] > pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] > pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1] + 1))
            elif pos_p[0] == pos_c[0] and pos_p[1] < pos_c[1] and pos_n[0] > pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append((pos_c[0] + 1, pos_c[1]))
            elif pos_p[0] < pos_c[0] and pos_p[1] == pos_c[1] and pos_n[0] == pos_c[0] and pos_n[1] < pos_c[1]:
                real_pos.append(pos_c)
            elif pos_p[0] == pos_c[0] and pos_p[1] > pos_c[1] and pos_n[0] < pos_c[0] and pos_n[1] == pos_c[1]:
                real_pos.append((pos_c[0], pos_c[1] + 1))

        seg_hor = []
        for i in range(len(real_pos)):
            p = real_pos[i]
            np = real_pos[(i + 1) % len(real_pos)]
            if p[0] != np[0]:
                seg_hor.append((p, np))

        area = 0
        for s in seg_hor:
            area += (s[0][0] - s[1][0]) * s[0][1]
        return area

    def _process(self):
        rg = re.compile(r"([RDLU]) (\d+) \(#(.+)\)")
        instructions = [rg.findall(line)[0] for line in self.lines]
        print("Day 18 - Star 1:", self.get_area_smart(instructions))
        print("Day 18 - Star 2:", self.get_area_smart([(get_letter(int(i[2][-1])), int(i[2][:5], 16))
                                                       for i in instructions]))


if __name__ == "__main__":
    Day18().run()
