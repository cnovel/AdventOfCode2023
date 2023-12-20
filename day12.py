from day_processing import Day
import re
import queue


class Day12(Day):
    def _name(self):
        return "--- Day 12: Hot Springs ---"

    def _file(self):
        return "data/input_12.txt"

    @staticmethod
    def _can_be_valid(pattern, start_pattern, corruption_size):
        if start_pattern + corruption_size > len(pattern):
            return False  # Can't overflow!
        # Can't have a . in the middle of the rule
        return all([c == "?" or c == "#" for c in pattern[start_pattern:start_pattern+corruption_size]])

    def _count_patterns(self, pattern, start_pattern, rules, rule_id):
        if (pattern[start_pattern:], rule_id) in self.remember:
            return self.remember[(pattern[start_pattern:], rule_id)]
        r = 0
        for i in range(start_pattern, len(pattern)):
            if pattern[i] in ["#", "?"] and self._can_be_valid(pattern, i, rules[rule_id]):
                if rule_id == len(rules) - 1:  # Last rule, valid if we can fill with .
                    r += 1 if all([c in '.?' for c in pattern[i + rules[rule_id]:]]) else 0
                elif i + rules[rule_id] + 1 < len(pattern) and pattern[i + rules[rule_id]] != "#":
                    next_pattern = list(pattern)
                    for j in range(start_pattern, i):
                        next_pattern[j] = '.'
                    for j in range(i, i + rules[rule_id]):
                        next_pattern[j] = "#"
                    next_pattern = ''.join(next_pattern)
                    r += self._count_patterns(next_pattern, i + rules[rule_id] + 1, rules, rule_id + 1)
            if pattern[i] == "#":
                break  # Rules are broken for this branch, since it cannot be valid
        self.remember[(pattern[start_pattern:], rule_id)] = r
        return r

    def _process(self):
        self.remember = {}
        patterns = []
        rules = []
        rg_num = re.compile("(\d+)")
        for line in self.lines:
            patterns.append(line.split(" ")[0])
            rules.append([int(i) for i in rg_num.findall(line)])

        count = 0
        for p, r in zip(patterns, rules):
            self.remember = {}
            count += self._count_patterns(p, 0, r, 0)
        self.prnt_a(count)

        count = 0
        for p, r in zip(patterns, rules):
            self.remember = {}
            count += self._count_patterns('?'.join([p]*5), 0, r*5, 0)
        self.prnt_b(count)


if __name__ == "__main__":
    Day12().run()
