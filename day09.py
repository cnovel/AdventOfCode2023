from day_processing import Day


class Day09(Day):
    def _name(self):
        return "--- Day 9: Mirage Maintenance ---"

    def _file(self):
        return "data/input_09.txt"

    def _process(self):
        sum_a = 0
        for l in self.lines:
            nums = [int(n) for n in l.strip().split(" ")]
            while set(nums) != {0}:
                sum_a += nums[-1]
                nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        print("Day 09 - Star 1:", sum_a)

        sum_b = 0
        for l in self.lines:
            nums = [int(n) for n in l.strip().split(" ")]
            nums.reverse()
            while set(nums) != {0}:
                sum_b += nums[-1]
                nums = [nums[i] - nums[i-1] for i in range(1, len(nums))]
        print("Day 09 - Star 2:", sum_b)


if __name__ == "__main__":
    Day09().run()
