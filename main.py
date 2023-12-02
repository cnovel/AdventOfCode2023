import time
from day01 import Day01
from day02 import Day02


days = [Day01("data/input_01.txt"),
        Day02("data/input_02.txt")]

s = time.perf_counter()
for d in days:
    d.run()
e = time.perf_counter()
print(f"It took {e - s:0.4f} seconds to process {len(days)} days.")