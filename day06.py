import re
from day_processing import Day


class Day06(Day):
   def _name(self):
      return "--- Day 6: Wait For It ---"

   def _file(self):
      return "data/input_06.txt"

   def _process(self):
      numbers_rg = re.compile("(\d+)")
      times = [int(n) for n in numbers_rg.findall(self.lines[0])]
      distances = [int(n) for n in numbers_rg.findall(self.lines[1])]
      star_a =  1
      for td in zip(times, distances):
         star_a *= len([i for i in range(0, td[0] + 1) if i * (td[0] - i) > td[1]])
      print("Day 05 - Star 1:", star_a)

      time = int(''.join([n for n in numbers_rg.findall(self.lines[0])]))
      dist = int(''.join([n for n in numbers_rg.findall(self.lines[1])]))
      min_i = -1
      for i in range(0, time):
         if i * (time - i) > dist:
            min_i = i
            break
      max_i = -1
      for i in range(time - min_i, time+1):
         if i * (time - i) <= dist:
            max_i = i
            break
      print("Day 06 - Star 2:", max_i - min_i)

if __name__ == "__main__":
   Day06().run()
