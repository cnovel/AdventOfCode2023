import re
from day_processing import Day

class TransformMap:
   def __init__(self, lines) -> None:
      self._transfos = []
      numbers_rg = re.compile("(\d+)")
      for l in lines:
         self._transfos.append([int(n) for n in numbers_rg.findall(l)])

   def transform(self, i: int) -> int:
      for t in self._transfos:
         if not i in range(t[1], t[1] + t[2]):
            continue
         return t[0] + i - t[1]
      return i

   def transform_segments(self, segments: []) -> []:
      new_segments = []
      for s in segments:
         mapped_segments = []
         for t in self._transfos:
            n_s = max(s[0], t[1])
            n_e = min(s[1], t[1] + t[2])
            if n_s >= n_e:
               continue  # no overlap
            mapped_segments.append((n_s, n_e))
            new_segments.append((t[0] + n_s - t[1], t[0] + n_e - t[1]))
         mapped_segments.sort(key=lambda a: a[0])

         if len(mapped_segments) == 0:  # no overlap at all
            new_segments.append(s)
            continue
         # Edge cases
         if s[0] < mapped_segments[0][0]:
            new_segments.append((s[0], mapped_segments[0][0]))
         if s[1] > mapped_segments[-1][1]:
            new_segments.append((mapped_segments[-1][1], s[1]))

         # Between the mapped segments
         for i in range(0, len(mapped_segments) - 1):
            new_segments.append((mapped_segments[i][1], mapped_segments[i+1][0]))
      return new_segments


class Day05(Day):
   def _name(self):
      return "--- Day 5: If You Give A Seed A Fertilizer ---"

   def _file(self):
      return "data/input_05.txt"

   def _process(self):
      numbers_rg = re.compile("(\d+)")
      seeds = [int(n) for n in numbers_rg.findall(self.lines[0])]

      maps = []
      lines = []
      for l in self.lines[3:]:
         if len(l.strip("\n")) == 0:
            continue
         if "map" in l:
            maps.append(TransformMap(lines))
            lines = []
            continue
         lines.append(l)
      maps.append(TransformMap(lines))

      for tm in maps:
         for i in range(0, len(seeds)):
            seeds[i] = tm.transform(seeds[i])

      print("Day 05 - Star 1:", min(seeds))

      seeds = [int(n) for n in numbers_rg.findall(self.lines[0])]
      segments = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
      for tm in maps:
         segments = tm.transform_segments(segments)
      segments.sort(key=lambda a: a[0])

      print("Day 05 - Star 2:", segments[0][0])

if __name__ == "__main__":
   Day05().run()
