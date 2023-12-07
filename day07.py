import re
from day_processing import Day
from collections import Counter


cards = "23456789TJQKA"
cards_joker = "J23456789TQKA"


def hand_score(most_commons):
   if most_commons[0][1] == 5:
      return 6
   elif most_commons[0][1] == 4:
      return 5
   elif most_commons[0][1] == 3 and most_commons[1][1] == 2:
      return 4
   elif most_commons[0][1] == 3:
      return 3
   elif most_commons[0][1] == 2 and most_commons[1][1] == 2:
      return 2
   elif most_commons[0][1] == 2:
      return 1
   return 0


class Hand:
   def __init__(self, line) -> None:
      s = line.strip("\n").split(" ")
      self.bid = int(s[1])
      self.cards = s[0]
      most_commons = Counter(self.cards).most_common(2)
      self.score = hand_score(most_commons)

   def __lt__(self, other):
      if self.score != other.score:
         return self.score < other.score

      for c in zip(self.cards, other.cards):
         i = cards.index(c[0])
         j = cards.index(c[1])
         if i != j:
            return i < j
      return True

class JokerHand:
   def __init__(self, line) -> None:
      s = line.strip("\n").split(" ")
      self.bid = int(s[1])
      self.cards = s[0]
      most_commons = Counter(self.cards).most_common(5)
      best_letter = ''
      for c in most_commons:
         if c[0] == 'J' and c[1] == 5:
            best_letter = 'A'
            break
         if c[0] == 'J':
            continue
         best_letter = c[0]
         break
      cards_swap = s[0].replace("J", best_letter)
      most_commons = Counter(cards_swap).most_common(5)
      self.score = hand_score(most_commons)

   def __lt__(self, other):
      if self.score != other.score:
         return self.score < other.score

      for c in zip(self.cards, other.cards):
         i = cards_joker.index(c[0])
         j = cards_joker.index(c[1])
         if i != j:
            return i < j
      return True

class Day07(Day):
   def _name(self):
      return "--- Day 7: Camel Cards ---"

   def _file(self):
      return "data/input_07.txt"

   def _process(self):
      hands = sorted([Hand(l) for l in self.lines])
      res = 0
      for i in range(len(hands)):
         res += (i+1)*hands[i].bid
      print("Day 06 - Star 1:", res)

      hands = sorted([JokerHand(l) for l in self.lines])
      res = 0
      for i in range(len(hands)):
         res += (i+1)*hands[i].bid
      print("Day 06 - Star 2:", res)

if __name__ == "__main__":
   Day07().run()
