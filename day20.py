from day_processing import Day
import collections
from functools import reduce
from utils import ppcm

HIGH_PULSE = 1
LOW_PULSE = 0


class Broadcaster:
    def __init__(self, name: str, followers: list):
        self.is_on = False
        self.followers = followers
        self.name = name

    def get_signals(self, signal, _):
        return [(self.name, x, signal) for x in self.followers]


class FlipFlop:
    def __init__(self, name: str, followers: list):
        self.is_on = False
        self.followers = followers
        self.name = name

    def get_signals(self, signal, _):
        if signal == HIGH_PULSE:
            return []
        self.is_on = not self.is_on
        pulse = HIGH_PULSE if self.is_on else LOW_PULSE
        return [(self.name, x, pulse) for x in self.followers]


class Conjunction:
    def __init__(self, name: str, followers: list):
        self.followers = followers
        self.name = name
        self.predecessors = {}

    def set_predecessors(self, names: list):
        for n in names:
            self.predecessors[n] = LOW_PULSE

    def get_signals(self, signal, from_name):
        self.predecessors[from_name] = signal
        tmp = list(set(self.predecessors.values()))
        pulse = HIGH_PULSE
        if len(tmp) == 1 and tmp[0] == HIGH_PULSE:
            pulse = LOW_PULSE
        return [(self.name, x, pulse) for x in self.followers]


class Day20(Day):
    def _name(self):
        return "--- Day 20: Pulse Propagation ---"

    def _file(self):
        return "data/input_20.txt"

    def _get_nodes(self):
        nodes = {}
        predecessors = {}
        for line in self.lines:
            line = line.strip("\n")
            split = line.split(" -> ")
            followers = split[1].split(", ")
            if split[0] == "broadcaster":
                nodes[split[0]] = Broadcaster(split[0], followers)
                continue
            t = split[0][0]
            name = split[0][1:]
            for f in followers:
                if f in predecessors.keys():
                    predecessors[f].append(name)
                else:
                    predecessors[f] = [name]
            if t == "%":
                nodes[name] = FlipFlop(name, followers)
            else:
                nodes[name] = Conjunction(name, followers)

        for k in nodes.keys():
            if type(nodes[k]) == Conjunction:
                nodes[k].set_predecessors(predecessors[k])
        return nodes, predecessors

    def _process(self):
        nodes, _ = self._get_nodes()
        c = collections.Counter({LOW_PULSE: 0, HIGH_PULSE: 0})
        for _ in range(1000):
            q = collections.deque()
            q.append(("button", "broadcaster", LOW_PULSE))
            while q:
                from_name, node, pulse = q.pop()
                c[pulse] += 1
                if node not in nodes:
                    continue
                signals = nodes[node].get_signals(pulse, from_name)
                for s in signals:
                    q.appendleft(s)

        self.prnt_a(c[LOW_PULSE] * c[HIGH_PULSE])

        nodes, predecessors = self._get_nodes()
        button_press = 0
        preds = predecessors[predecessors['rx'][0]]  # This is assuming these are flipflop nodes
        cycles_preds = {x: -1 for x in preds}
        cycles_found = False
        while not cycles_found:
            q = collections.deque()
            q.append(("button", "broadcaster", LOW_PULSE))
            button_press += 1
            while q:
                from_name, node, pulse = q.pop()
                if from_name in cycles_preds.keys() and cycles_preds[from_name] == -1 and pulse == HIGH_PULSE:
                    cycles_preds[from_name] = button_press
                if node not in nodes:
                    continue
                signals = nodes[node].get_signals(pulse, from_name)
                for s in signals:
                    q.appendleft(s)
            if -1 not in cycles_preds.values():
                cycles_found = True

        self.prnt_b(int(reduce(lambda x, y: ppcm(x, y), cycles_preds.values())))


if __name__ == "__main__":
    Day20().run()
