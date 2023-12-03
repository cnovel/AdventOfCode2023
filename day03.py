import regex as re

from day_processing import Day

class BlockNumber:
   def __init__(self, x_s, x_e, y, value) -> None:
      self.x_s = x_s
      self.x_e = x_e
      self.y = y
      self.value = value
   def next_to(self, star) -> bool:
      return self.y - 1 <= star[1] <= self.y + 1 and self.x_s - 1 <= star[0] <= self.x_e


class Day03(Day):
   def _name(self):
      return "--- Day 3: Gear Ratios ---"

   def _file(self):
      return "data/input_03.txt"

   def _process(self):
      sum_a = 0
      symbol_pos = set()
      star_pos = set()
      symbol_rg = re.compile("([^\d.\n])")
      for i in range(0, len(self.lines)):
         l = self.lines[i]
         for s in symbol_rg.finditer(l):
            symbol_pos.add((s.span()[0],i))
            if s.group() == "*":
               star_pos.add((s.span()[0],i))

      numbers = re.compile("(\d+)")
      number_blocks = []
      for i in range(0, len(self.lines)):
         l = self.lines[i]
         for n in numbers.finditer(l):
            x_s = n.span()[0]
            x_e = n.span()[1]
            y_s = i - 1
            y_e = i + 2
            hit = any([(x,y) in symbol_pos for y in range(y_s, y_e) for x in range(x_s - 1, x_e + 1)])
            if hit:
               sum_a += int(n.group())
            number_blocks.append(BlockNumber(x_s, x_e, i, int(n.group())))

      sum_b = 0
      for star in star_pos:
         neighs = [n.value for n in number_blocks if n.next_to(star)]
         if len(neighs) == 2:
            sum_b += neighs[0] * neighs[1]

      print("Day 03 - Star 1:", sum_a)
      print("Day 03 - Star 2:", sum_b)

if __name__ == "__main__":
   Day03().run()
