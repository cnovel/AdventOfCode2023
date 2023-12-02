from day_processing import Day

class Day01(Day):
   def _process(self):
      digits = "0123456789"

      sum = 0
      for l in self.lines:
         line_digits = [x for x in l if x in digits]
         number_str = line_digits[0] + line_digits[-1]
         number = int(number_str)
         sum += number
      print("Day 01 - Star 1:", sum)

      sum = 0
      digits_word_to_digits = {"zero": "0", "one": "1", "two": "2", "three": "3",
                              "four": "4", "five": "5", "six": "6", "seven": "7",
                              "eight": "8", "nine": "9"}
      for l in self.lines:
         line_digits = []
         for i in range(0, len(l)):
            line = l[i:len(l)]
            if line[0] in digits:
               line_digits.append(line[0])
            word = [digits_word_to_digits[k] for k in digits_word_to_digits.keys() if line.startswith(k)]
            if word:
               line_digits.append(word[0])

         number_str = line_digits[0] + line_digits[-1]
         number = int(number_str)
         sum += number
      print("Day 01 - Star 2:", sum)

