from day_processing import Day
import re
from collections import Counter


def get_dir(c: str):
    if c == "R":
        return (1, 0)
    if c == "D":
        return (0, 1)
    if c == "L":
        return (-1, 0)
    return (0, -1)

def get_symbol(c: str):
    if c == "R" or c== "L":
        return "-"
    return "|"

def get_turn(c: str, cn: str):
    if c == "R" and cn == "D":
        return "7"
    if c == "R" and cn == "U":
        return "J"
    if c == "L" and cn == "U":
        return "L"
    if c == "L" and cn == "D":
        return "F"
    if c == "D" and cn == "R":
        return "L"
    if c == "D" and cn == "L":
        return "J"
    if c == "U" and cn == "R":
        return "F"
    if c == "U" and cn == "L":
        return "7"
    if c == cn and (c == "R" or c == "L"):
        return "-"
    if c == cn and (c == "U" or c == "D"):
        return "|"
    return None


def get_letter(c: int):
    if c == 0:
        return "R"
    if c == 1:
        return "D"
    if c == 2:
        return "L"
    return "U"


def in_vert(s, mid_y):
    return s[0][1] <= mid_y < s[1][1] + 1 or s[0][1] + 1 > mid_y >= s[1][1]
def in_hori(s, mid_x):
    return s[0][0] <= mid_x < s[1][0] + 1 or s[0][0] + 1 > mid_x >= s[1][0]

class Day18(Day):
    def _name(self):
        return "--- Day 18: Clumsy Crucible ---"

    def _file(self):
        return "data/ex_18_2.txt"

    def get_area(self, instructions):
        pos = (0, 0)
        vert_segments = []
        hori_segments = []
        abs = set([0])
        ord = set([0])
        for i in instructions:
            dir = get_dir(i[0])
            d = int(i[1])
            new_pos = (pos[0] + d*dir[0], pos[1] + d*dir[1])
            if dir[0] == 0:
                vert_segments.append((pos, new_pos))
            else:
                hori_segments.append((pos, new_pos))
            pos = new_pos
            abs.add(pos[0])
            ord.add(pos[1])

        area = 0
        abs = sorted(list(abs))
        ord = sorted(list(ord))
        abs.append(abs[-1]+1)
        ord.append(ord[-1]+1)
        for i in range(len(abs) - 1):
            for j in range(len(ord) - 1):
                print(f"Computing rectangle {abs[i]} -> {abs[i+1]} {ord[j]} -> {ord[j+1]}")
                dx = abs[i+1] - abs[i]
                mid_x = abs[i] + float(dx) / 2.
                dy = ord[j+1] - ord[j]
                mid_y = ord[j] + float(dy) / 2.

                # If dx or dy == 1, we are on a border

                c_l = 0
                for v in vert_segments:
                    if not in_vert(v, mid_y):
                        continue
                    if v[0][0] < mid_x:
                        c_l += 1

                c_t = 0
                for h in hori_segments:
                    if not in_hori(h, mid_x):
                        continue
                    if v[0][1] < mid_y:
                        c_t += 1

                print("Params:", mid_x, mid_y, dx, c_l, dy, c_t)

                print(" Adding", dx*dy)
                area += dx*dy
        print(area)

    def _process(self):
        rg = re.compile(r"([RDLU]) (\d+) \(#(.+)\)")
        instructions = [rg.findall(line)[0] for line in self.lines]
        self.get_area(instructions)
        """
        pos = (0,0)
        c = {}
        for i in range(len(self.instructions)):
            i_curr = self.instructions[i]
            i_next = self.instructions[(i + 1) % len(self.instructions)]
            dir = get_dir(i_curr[0])
            symbol = get_symbol(i_curr[0])
            for _ in range(int(i_curr[1])):
                pos = (pos[0] + dir[0], pos[1] + dir[1])
                c[pos] = symbol
            c[pos] = get_turn(i_curr[0], i_next[0])

        min_x = min(p[0] for p in c.keys())
        max_x = max(p[0] for p in c.keys()) + 1
        min_y = min(p[1] for p in c.keys())
        max_y = max(p[1] for p in c.keys()) + 1

        digged = 0
        for j in range(min_y, max_y):
            inside = False
            start = ""
            on_pipe = False
            for i in range(min_x, max_x):
                if (i, j) not in c.keys():
                    digged += 1 if inside else 0
                    continue
                digged += 1
                s = c[(i,j)]
                if s in {"F", "L"} and not on_pipe:
                    start = s
                    on_pipe = True
                    continue
                if s in {"7", "J"} and on_pipe:
                    if start == "F" and s == "J":
                        inside = not inside
                    if start == "L" and s == "7":
                        inside = not inside
                    on_pipe = False
                    continue
                if s == "|":
                    inside = not inside
                    continue
        print(digged)

        """
        fix_instructions = []
        for i in instructions:
            d = int(i[2][0:5], 16)
            c = get_letter(int(i[2][-1]))
            fix_instructions.append((c, d))
        pos = (0, 0)
        vert_segments = []
        hori_segments = []
        abs = set([0])
        ord = set([0])
        for i in fix_instructions:
            dir = get_dir(i[0])
            d = int(i[1])
            new_pos = (pos[0] + d*dir[0], pos[1] + d*dir[1])
            if dir[0] == 0:
                vert_segments.append((pos, new_pos))
            else:
                hori_segments.append((pos, new_pos))
            pos = new_pos
            abs.add(pos[0])
            ord.add(pos[1])

        area = 0
        abs = sorted(list(abs))
        ord = sorted(list(ord))
        for i in range(len(abs) - 1):
            for j in range(len(ord) - 1):
                dx = abs[i+1] - abs[i]
                mid_x = float(dx) / 2.
                dy = ord[j+1] - ord[j]
                mid_y = float(dy) / 2.

                c_x = 0
                for v in vert_segments:
                    if not in_vert(v, mid_y):
                        continue
                    if v[0][0] < mid_x:
                        c_x += 1
                if c_x % 2 == 0:
                    continue

                c_y = 0
                for h in hori_segments:
                    if not in_hori(h, mid_x):
                        continue
                    if v[0][1] <= mid_y:
                        c_y += 1
                if c_y % 2 == 0:
                    continue
                area += dx*dy
        print(area)




if __name__ == "__main__":
    Day18().run()
