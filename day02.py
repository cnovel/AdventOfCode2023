import re
from day_processing import Day


class Day02(Day):
    def _name(self):
        return "--- Day 2: Cube Conundrum ---"

    def _file(self):
        return "data/input_02.txt"

    def _process(self):
        sum_a = 0
        sum_b = 0
        max_red = 12
        max_green = 13
        max_blue = 14

        rg_game_id = re.compile(r"Game (\d+):")
        rg_red = re.compile(r"(\d+) red")
        rg_green = re.compile(r"(\d+) green")
        rg_blue = re.compile(r"(\d+) blue")

        for l in self.lines:
            game_id = int(rg_game_id.findall(l)[0])
            red = max([int(s) for s in rg_red.findall(l)] + [0])
            green = max([int(s) for s in rg_green.findall(l)] + [0])
            blue = max([int(s) for s in rg_blue.findall(l)] + [0])
            possible = red <= max_red and blue <= max_blue and green <= max_green
            if possible:
                sum_a += game_id
            sum_b += red * green * blue

        self.prnt_a(sum_a)
        self.prnt_b(sum_b)


if __name__ == "__main__":
    Day02().run()
