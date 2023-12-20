from day_processing import Day
import re
import queue


class Day12(Day):
    def _name(self):
        return "--- Day 12: Hot Springs ---"

    def _file(self):
        return "data/input_12.txt"

    @staticmethod
    def _check_pattern(p, r):
        blocks = [s for s in p.split(".") if len(s) > 0]
        for i in range(len(blocks)):
            b = blocks[i]
            if '?' in b:
                return True
            if i >= len(r):
                return False
            if len(b) != r[i]:
                return False
        if '?' in p:
            return True

        if len(blocks) != len(r):
            return False
        return True

    def _get_all_possible_patterns(self, p, r):
        c = 0
        q = queue.Queue()
        q.put(p)
        while not q.empty():
            np = q.get()
            if "?" not in np:
                c += 1
                continue
            a = np.replace("?", ".", 1)
            b = np.replace("?", "#", 1)
            if self._check_pattern(a, r):
                q.put(a)
            if self._check_pattern(b, r):
                q.put(b)
        return c

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
        for line in self.lines:
            patterns.append(line.split(" ")[0])
            rules.append([int(i) for i in rg_num.findall(line)])
        count = 0
        for p, r in zip(patterns, rules):
            count += self._get_all_possible_patterns(p, r)
        self.prnt_a(count)


if __name__ == "__main__":
    Day12().run()
