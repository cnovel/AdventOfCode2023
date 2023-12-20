from day_processing import Day


def hash_w(w):
    s = 0
    for c in w:
        s += ord(c)
        s *= 17
        s = s % 256
    return s


class Day15(Day):
    def _name(self):
        return "--- Day 15: Lens Library ---"

    def _file(self):
        return "data/input_15.txt"

    def _process(self):
        words = []
        for line in self.lines:
            words += line.split(",")
        self.prnt_a(sum(hash_w(w) for w in words))

        box = [[] for _ in range(256)]
        for w in words:
            lens = -1
            if w.endswith("-"):
                label = w[:-1]
            else:
                label = w[:-2]
                lens = int(w[-1])
            box_id = hash_w(label)
            if lens == -1:
                box[box_id] = [b for b in box[box_id] if b[0] != label]
            else:
                new_box = []
                inside = False
                for b in box[box_id]:
                    if b[0] == label:
                        new_box.append((b[0], lens))
                        inside = True
                        continue
                    new_box.append(b)
                if not inside:
                    new_box.append((label, lens))
                box[box_id] = new_box
        self.prnt_b(sum((i + 1) * (j + 1) * box[i][j][1] for i in range(len(box)) for j in range(len(box[i]))))


if __name__ == "__main__":
    Day15().run()
