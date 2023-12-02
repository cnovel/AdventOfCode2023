import regex as re

from day_processing import Day

class Day01(Day):
   def _name(self):
      return "--- Day 1: Trebuchet?! ---"

   def _file(self):
      return "data/input_01.txt"

   def _process(self):
      r_a = re.compile("([0-9])")
      r_b = re.compile("(one|two|three|four|five|six|seven|eight|nine|zero|[0-9])")

      transfo = {"zero": "0", "one": "1", "two": "2", "three": "3",
                              "four": "4", "five": "5", "six": "6", "seven": "7",
                              "eight": "8", "nine": "9", "1": "1", "2": "2", "3": "3",
                              "4": "4", "5": "5", "6": "6", "7": "7", "8": "8",
                              "9": "9", "0": "0"}

      sum_a = 0
      sum_b = 0

      for l in self.lines:
         matches = r_a.findall(l)
         nb_str = transfo[matches[0]] + transfo[matches[-1]]
         nb = int(nb_str)
         sum_a += nb

         matches = r_b.findall(l.strip(), overlapped=True)
         nb_str = transfo[matches[0]] + transfo[matches[-1]]
         nb = int(nb_str)
         sum_b += nb

      print("Day 01 - Star 1:", sum_a)
      print("Day 01 - Star 2:", sum_b)


if __name__ == "__main__":
   Day01().run()
