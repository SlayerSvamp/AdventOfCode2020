codes = open('data/day05.txt').read().splitlines()


def seat(code):
    col, row = 0, 0
    x, y = 4, 64
    for c in code:
        if c in 'BF':
            if c == 'B':
                row += y
            y /= 2
        else:
            if c == 'R':
                col += x
            x /= 2
    return int(row*8 + col)


*IDs, last = sorted([seat(code) for code in codes])
current = IDs[0]

while current in IDs:
    current += 1


print(f'Part 1: {last}')
print(f'Part 2: {current}')
