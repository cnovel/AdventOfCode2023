import re


sum_a = 0
sum_b = 0
max_red = 12
max_green = 13
max_blue = 14

rg_red = re.compile("[0-9]+ red")
rg_green = re.compile("[0-9]+ green")
rg_blue = re.compile("[0-9]+ blue")

with open("data/input_02.txt", 'r') as d:
   for l in d.readlines():
      game_id = int(l.split(":")[0][5:])
      draws = [d.strip() for d in l.split(":")[1].strip().split(";")]
      possible = True
      red = 0
      green = 0
      blue = 0
      for draw in draws:
         m = [int(s.split(" ")[0]) for s in rg_red.findall(draw)]
         if m and m[0] > max_red:
            possible = False
         if m:
            red = max(red, m[0])
         m = [int(s.split(" ")[0]) for s in rg_green.findall(draw)]
         if m and m[0] > max_green:
            possible = False
         if m:
            green = max(green, m[0])
         m = [int(s.split(" ")[0]) for s in rg_blue.findall(draw)]
         if m and m[0] > max_blue:
            possible = False
         if m:
            blue = max(blue, m[0])
      if possible:
         sum_a += game_id
      sum_b += red*green*blue

print("Day 02 - Star 1:", sum_a)
print("Day 02 - Star 2:", sum_b)