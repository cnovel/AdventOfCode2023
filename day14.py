from day_processing import Day


class Day14(Day):
    def _name(self):
        return "--- Day 14: Parabolic Reflector Dish ---"

    def _file(self):
        return "data/input_14.txt"

    def _cycle(self, boulders, stoppers):
        b = boulders.copy()
        # Cycle north
        tops = [0 for _ in range(len(self.lines[-1]))]
        new_boulders = set()
        for j in range(len(self.lines)):
            for i in range(len(self.lines[-1])):
                if (i,j) in stoppers:
                    tops[i] = j + 1
                    continue
                if (i, j) in b:
                    new_boulders.add((i, tops[i]))
                    tops[i] += 1
        b = new_boulders.copy()
        new_boulders.clear()

        # Cycle west
        for j in range(len(self.lines)):
            left = 0
            for i in range(len(self.lines[-1])):
                if (i,j) in stoppers:
                    left = i + 1
                    continue
                if (i, j) in b:
                    new_boulders.add((left, j))
                    left += 1
        b = new_boulders.copy()
        new_boulders.clear()

        # Cycle south
        bottoms = [len(self.lines) - 1 for _ in range(len(self.lines[-1]))]
        for j in range(len(self.lines) - 1, -1, -1):
            for i in range(len(self.lines[-1])):
                if (i, j) in stoppers:
                    bottoms[i] = j - 1
                    continue
                if (i, j) in b:
                    new_boulders.add((i, bottoms[i]))
                    bottoms[i] -= 1
        b = new_boulders.copy()
        new_boulders.clear()

        # Cycle east
        for j in range(len(self.lines)):
            right = len(self.lines[-1]) - 1
            for i in range(len(self.lines[-1]) - 1, -1, -1):
                if (i,j) in stoppers:
                    right = i - 1
                    continue
                if (i, j) in b:
                    new_boulders.add((right, j))
                    right -= 1
        b = new_boulders.copy()
        new_boulders.clear()
        return b

    def _process(self):
        tops = [0 for _ in range(len(self.lines[-1]))]
        star_a = 0
        for j in range(len(self.lines)):
            for i in range(len(self.lines[-1])):
                if self.lines[j][i] == '#':
                    tops[i] = j+1
                    continue
                if self.lines[j][i] == 'O':
                    star_a += len(self.lines) - tops[i]
                    tops[i] += 1
                    continue
        print("Day 14 - Star 1:", star_a)

        boulders = set()
        stoppers = set()
        for j in range(len(self.lines)):
            for i in range(len(self.lines[-1])):
                if self.lines[j][i] == '#':
                    stoppers.add((i,j))
                    continue
                if self.lines[j][i] == 'O':
                    boulders.add((i,j))
                    continue
        known_configs_to_cycle = {}
        cycle_to_load = {}
        start_cycle = -1
        size_cycle = -1
        nb_cycle = 1000000000
        for i in range(1,nb_cycle + 1):
            boulders = self._cycle(boulders, stoppers)
            fb = frozenset(boulders)
            if fb in known_configs_to_cycle.keys():
                start_cycle = known_configs_to_cycle[fb]
                size_cycle = i - start_cycle
                break
            known_configs_to_cycle[fb] = i
            cycle_to_load[i] = sum([len(self.lines) - b[1] for b in fb])

        idx = ((nb_cycle - start_cycle) % size_cycle) + start_cycle
        print("Day 14 - Star 2:", cycle_to_load[idx])


if __name__ == "__main__":
    Day14().run()
