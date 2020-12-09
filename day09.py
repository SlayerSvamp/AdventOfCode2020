values = [int(line) for line in open('data/day09.txt').read().splitlines()]


class XMAS:
    def __init__(self, code, preamble):
        self.preamble = code[:preamble]
        self.queue = code[preamble:]

    def left(self):
        return len(self.queue)

    def valid(self, value):
        for i, a in enumerate(self.preamble):
            for j, b in enumerate(self.preamble):
                if i != j:
                    if a+b == value:
                        return True
        return False

    def next(self):
        value, *self.queue = self.queue
        valid = self.valid(value)
        _, *self.preamble = self.preamble
        self.preamble.append(value)
        return valid

    def last(self):
        return self.preamble[-1]


xmas = XMAS(values, 25)

while xmas.queue:
    if not xmas.next():
        invalid = xmas.last()

ls = []
tot = 0
while tot != invalid:
    if tot < invalid:
        value, *values = values
        ls.append(value)
    else:
        ls = ls[1:]
    tot = sum(ls)

weakness = min(ls) + max(ls)


print(f'Part 1: {invalid}')
print(f'Part 2: {weakness}')
