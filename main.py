import time
from day01 import Day01
from day02 import Day02
from day03 import Day03
from day04 import Day04


days = [Day01(), Day02(), Day03(), Day04()]

s = time.perf_counter()
for d in days:
    d.run()
e = time.perf_counter()
print(f"It took {e - s:0.4f} seconds to process {len(days)} days.")