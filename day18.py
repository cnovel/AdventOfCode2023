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


class Day18(Day):
    def _name(self):
        return "--- Day 18: Lavaduct Lagoon ---"

    def _file(self):
        return "data/input_18.txt"

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
        self.prnt_a(self.get_area_smart(instructions))
        self.prnt_b(self.get_area_smart([(get_letter(int(i[2][-1])), int(i[2][:5], 16)) for i in instructions]))


if __name__ == "__main__":
    Day18().run()
