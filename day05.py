codes = open('data/day05.txt').read().splitlines()


def seat(code):
    ID = 0
    for c in code:
        ID <<= 1
        ID += ~ord(c) >> 2 & 1  # 1 if c in 'BR' else 0
    return ID


*IDs, last = sorted([seat(code) for code in codes])
current = IDs[0]
while current in IDs:
    current += 1

print(f'Part 1: {last}')
print(f'Part 2: {current}')
