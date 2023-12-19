from day_processing import Day
import re
import collections

xmas_to_int = {"x": 0, "m": 1, "a": 2, "s": 3}


def get_next(part, rule):
    if '<' not in rule and '>' not in rule:
        return True, rule
    c = xmas_to_int[rule[0]]
    comp = rule[1]
    v = int(rule[2:].split(":")[0])
    k = rule[2:].split(":")[1]
    if comp == "<" and part[c] < v:
        return True, k
    elif comp == ">" and part[c] > v:
        return True, k
    return False, None


def get_next_interval(part, rule):
    if '<' not in rule and '>' not in rule:
        return [rule, part[1], part[2], part[3], part[4]], None
    c = xmas_to_int[rule[0]]
    comp = rule[1]
    v = int(rule[2:].split(":")[0])
    k = rule[2:].split(":")[1]
    c += 1
    interval = part[c]
    if comp == "<" and interval[0] < v:
        int_l = (interval[0], v-1)
        int_r = (v, interval[1])
        r = part.copy()
        r[0] = k
        r[c] = int_l
        s = part.copy()
        s[c] = int_r
        return r, s
    if comp == ">" and interval[1] > v:
        int_l = (interval[0], v)
        int_r = (v+1, interval[1])
        r = part.copy()
        r[0] = k
        r[c] = int_r
        s = part.copy()
        s[c] = int_l
        return r, s
    return None, part


class Day19(Day):
    def _name(self):
        return "--- Day 19: Aplenty ---"

    def _file(self):
        return "data/input_19.txt"

    def _process(self):
        rg_part = re.compile(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}")
        rg_rule = re.compile(r"(.+){(.*)}")

        rules = {}
        parts = []
        for line in self.lines:
            line = line.strip("\n")
            if len(line) == 0:
                continue
            m = rg_rule.findall(line)
            if m:
                rules[m[0][0]] = m[0][1].split(',')
            m = rg_part.findall(line)
            if m:
                parts.append([int(a) for a in m[0]])

        s = 0
        for p in parts:
            k = "in"
            while k not in ['A', 'R']:
                for r in rules[k]:
                    ok, nk = get_next(p, r)
                    if ok:
                        k = nk
                        break
            if k == "A":
                s += sum(p)
        print("Day 19 - Star 1:", s)

        part = ["in", (1, 4000), (1, 4000), (1, 4000), (1, 4000)]
        q = collections.deque()
        q.append(part)

        s = 0
        while q:
            part = q.pop()
            if part[0] == "R":
                continue
            if part[0] == "A":
                s += (part[1][1] - part[1][0] + 1) * (part[2][1] - part[2][0] + 1) * (part[3][1] - part[3][0] + 1) *\
                     (part[4][1] - part[4][0] + 1)
                continue
            rule = rules[part[0]]
            for r in rule:
                pr, pl = get_next_interval(part, r)
                if pr is not None:
                    q.append(pr)
                part = pl
        print("Day 19 - Star 2:", s)


if __name__ == "__main__":
    Day19().run()
