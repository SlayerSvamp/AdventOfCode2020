class Adapter:
    def __init__(self, joltage):
        self.joltage = joltage
        self.out = set()
        self.paths = 0

    def longest_path(self, state=[0, 0, 0]):
        if not self.out:
            return state

        lowest = min(self.out, key=lambda x: x.joltage)
        state[lowest.joltage - self.joltage - 1] += 1
        return lowest.longest_path(state)

    def count_paths(self):
        if not self.paths:
            if not self.out:
                self.paths = 1
            for adapter in self.out:
                self.paths += adapter.count_paths()

        return self.paths

    @staticmethod
    def setup(values):
        adapters = [Adapter(value) for value in sorted(values)]
        outlet = adapters[0]
        while adapters:
            cur, *adapters = adapters
            for adapter in adapters:
                if adapter.joltage - cur.joltage <= 3:
                    cur.out.add(adapter)
                    continue
                break
        return outlet


values = [int(x) for x in open('data/day10.txt').read().splitlines()]
outlet = Adapter.setup([0] + values + [max(values) + 3])

one, _, three = outlet.longest_path()

print(f'Part 1: {one * three}')
print(f'Part 2: {outlet.count_paths()}')
