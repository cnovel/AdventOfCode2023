from day_processing import Day


class Day15(Day):
    def _name(self):
        return "--- Day 15: Lens Library ---"

    def _file(self):
        return "data/input_15.txt"

    def _hash(self, w):
        s = 0
        for c in w:
            s += ord(c)
            s *= 17
            s = s % 256
        return s

    def _process(self):
        words = []
        for line in self.lines:
            words += line.split(",")
        star_a = 0
        for w in words:
            star_a += self._hash(w)
        print("Day 15 - Star 1:", star_a)

        box = [[] for _ in range(256)]
        for w in words:
            label = ""
            lens = -1
            if w.endswith("-"):
                label = w[:-1]
            else:
                label = w[:-2]
                lens = int(w[-1])
            box_id = self._hash(label)
            if lens == -1:
                box[box_id] = [b for b in box[box_id] if b[0] != label]
            else:
                new_box = []
                inside = False
                for b in box[box_id]:
                    if b[0] == label:
                        new_box.append((b[0], lens))
                        inside =  True
                        continue
                    new_box.append(b)
                if not inside:
                    new_box.append((label, lens))
                box[box_id] = new_box
        f_power = 0
        for i in range(len(box)):
            for j in range(len(box[i])):
                f_power += (i+1) * (j+1) * box[i][j][1]
        print("Day 15 - Star 2:", f_power)



if __name__ == "__main__":
    Day15().run()
