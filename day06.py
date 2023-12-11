import re
from day_processing import Day
from math import sqrt


class Day06(Day):
    def _name(self):
        return "--- Day 6: Wait For It ---"

    def _file(self):
        return "data/input_06.txt"

    def _process(self):
        numbers_rg = re.compile(r"(\d+)")
        times = [int(n) for n in numbers_rg.findall(self.lines[0])]
        distances = [int(n) for n in numbers_rg.findall(self.lines[1])]
        star_a = 1
        for td in zip(times, distances):
            star_a *= len([i for i in range(0, td[0] + 1) if i * (td[0] - i) > td[1]])
        print("Day 05 - Star 1:", star_a)

        time = int(''.join([n for n in numbers_rg.findall(self.lines[0])]))
        dist = int(''.join([n for n in numbers_rg.findall(self.lines[1])]))

        # Solving x*(time-x) > dist
        # -x² + time*x - dist > 0
        # D = time*time - 4*dist
        # x = 0.5*(time +- sqrt(D))
        min_x = int(0.5 * (time - sqrt(time * time - 4 * dist)) + 0.5)
        max_x = int(0.5 * (sqrt(time * time - 4 * dist) + time) + 1.5)
        print("Day 06 - Star 2:", max_x - min_x)


if __name__ == "__main__":
    Day06().run()
