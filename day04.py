import re
from day_processing import Day

class Day04(Day):
   def _name(self):
      return "--- Day 4: Scratchcards ---"

   def _file(self):
      return "data/input_04.txt"

   def _process(self):
      sum_a = 0
      
      numbers_and_sep_rg = re.compile("(\d+|\|)")
      card_id_to_number_of_card = {}
      for i in range(0, len(self.lines)):
         card_id_to_number_of_card[i+1] = 1

      for l in self.lines:
         hits = numbers_and_sep_rg.findall(l)
         after_sep = False
         winning_nb = set()
         count = 0
         cid = int(hits[0])
         for n in hits[1:]:
            if n == "|":
               after_sep = True
               continue
            if not after_sep:
               winning_nb.add(int(n))
            elif int(n) in winning_nb:
               count += 1
         if count > 0:
            sum_a += pow(2, count - 1)
         nb_c = card_id_to_number_of_card[cid]
         for next_card_id in range(cid + 1, cid + 1 + count):
            card_id_to_number_of_card[next_card_id] += nb_c

      print("Day 04 - Star 1:", sum_a)
      print("Day 04 - Star 2:", sum(card_id_to_number_of_card.values()))

if __name__ == "__main__":
   Day04().run()
