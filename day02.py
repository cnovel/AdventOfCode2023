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

      rg_game_id = re.compile("Game ([0-9]+):")
      rg_red = re.compile("([0-9]+) red")
      rg_green = re.compile("([0-9]+) green")
      rg_blue = re.compile("([0-9]+) blue")

      for l in self.lines:
         game_id = int(rg_game_id.findall(l)[0])
         red = max([int(s) for s in rg_red.findall(l)] + [0])
         green = max([int(s) for s in rg_green.findall(l)] + [0])
         blue = max([int(s) for s in rg_blue.findall(l)] + [0])
         possible = red <= max_red and blue <= max_blue and green <= max_green
         if possible:
            sum_a += game_id
         sum_b += red*green*blue

      print("Day 02 - Star 1:", sum_a)
      print("Day 02 - Star 2:", sum_b)

if __name__ == "__main__":
   Day02().run()
