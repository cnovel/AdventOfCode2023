import re
from day_processing import Day


class Day04(Day):
    def _name(self):
        return "--- Day 4: Scratchcards ---"

    def _file(self):
        return "data/input_04.txt"

    def _process(self):
        sum_a = 0

        numbers_rg = re.compile(r"(\d+)")
        card_id_to_number_of_card = {}
        for i in range(0, len(self.lines)):
            card_id_to_number_of_card[i + 1] = 1

        for l in self.lines:
            split = l.split("|")
            cid_and_winning_nb = [int(n) for n in numbers_rg.findall(split[0])]
            winning_nb = set(cid_and_winning_nb[1:])
            cid = cid_and_winning_nb[0]
            count = len([n for n in numbers_rg.findall(split[1]) if int(n) in winning_nb])
            if count > 0:
                sum_a += pow(2, count - 1)
            for next_card_id in range(cid + 1, cid + 1 + count):
                card_id_to_number_of_card[next_card_id] += card_id_to_number_of_card[cid]

        print("Day 04 - Star 1:", sum_a)
        print("Day 04 - Star 2:", sum(card_id_to_number_of_card.values()))


if __name__ == "__main__":
    Day04().run()
