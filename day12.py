from day_processing import Day
import re
import queue

class Day12(Day):
    def _name(self):
        return "--- Day 12: Hot Springs ---"

    def _file(self):
        return "data/input_12.txt"

    def _check_pattern(self, p, r):
        split = [s for s in p.split(".") if len(s) > 0]
        for i in range(len(split)):
            if i >= len(r):
                return False
            if "?" in split[i]:
                return True
            if len(split[i]) != r[i]:
                return False

        if "?" in p:
            return True

        if len(split) != len(r):
            return False
        for s,t in zip(split, r):
            if len(s) != t:
                return False
        return True

    def _get_all_possible_patterns(self, p, r):
        res = []
        q = queue.Queue()
        q.put(p)
        while not q.empty():
            np = q.get()
            if "?" not in np:
                res.append(np)
                continue
            a = np.replace("?", ".", 1)
            b = np.replace("?", "#", 1)
            if self._check_pattern(a, r):
                q.put(a)
            if self._check_pattern(b, r):
                q.put(b)
        return len(res)

    def _get_all_possible_patterns_repeated(self, p, r):
        res = []
        q = queue.Queue()
        p = '?'.join([p for _ in range(5)])
        print(p)
        r = r*5
        print(r)
        q.put(p)
        while not q.empty():
            np = q.get()
            if "?" not in np:
                res.append(np)
                continue
            a = np.replace("?", ".", 1)
            b = np.replace("?", "#", 1)
            if self._check_pattern(a, r):
                q.put(a)
            if self._check_pattern(b, r):
                q.put(b)
        return len(res)

    def _process(self):
        patterns = []
        rules = []
        rg_num = re.compile("(\d+)")
        for l in self.lines:
            patterns.append(l.split(" ")[0])
            rules.append([int(i) for i in rg_num.findall(l)])
        count = 0
        for p,r in zip(patterns, rules):
            count += self._get_all_possible_patterns(p, r)
        print("Day 12 - Star 1:", count)


if __name__ == "__main__":
    Day12().run()
