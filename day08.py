import re
from day_processing import Day
from functools import reduce
from utils import ppcm


class Day08(Day):
    def _name(self):
        return "--- Day 8: Haunted Wasteland ---"

    def _file(self):
        return "data/input_08.txt"

    def _process(self):
        instructions = [0 if a == 'L' else 1 for a in self.lines[0].strip("\n")]
        carte = {}
        rg = re.compile("([0-9A-Z]+)")
        for l in self.lines[2:]:
            m = rg.findall(l)
            carte[m[0]] = (m[1], m[2])

        cur_pos = "AAA"
        steps = 0
        while cur_pos != "ZZZ":
            i = steps % len(instructions)
            cur_pos = carte[cur_pos][instructions[i]]
            steps += 1
        self.prnt_a(steps)

        cur_pos = [pos for pos in carte.keys() if pos.endswith('A')]
        steps_by_pos = []
        ends = []
        for p in cur_pos:
            steps = 0
            while not p.endswith("Z"):
                i = steps % len(instructions)
                p = carte[p][instructions[i]]
                steps += 1
            ends.append(p)
            steps_by_pos.append(steps)

        self.prnt_b(int(reduce(lambda x, y: ppcm(x, y), steps_by_pos)))

        # Check solution is right
        """
        steps_by_cycle = []
        for p in ends:
           steps = 0
           s = p
           while steps == 0 or not p.endswith("Z"):
              i = steps % len(instructions)
              p = carte[p][instructions[i]]
              steps +=1
           steps_by_cycle.append(steps)
        if steps_by_pos != steps_by_pos:
           print("Solution is false!")
        """


if __name__ == "__main__":
    Day08().run()
