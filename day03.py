rows = open('data/day03.txt').read().splitlines()

angles = [
    (1, 1),
    (3, 1),  # part 1
    (5, 1),
    (7, 1),
    (1, 2),
]

part1 = 0
part2 = 1

for (ax, ay) in angles:
    y, x, trees = 0, 0, 0
    while y < len(rows):
        if rows[y][x] == '#':
            trees += 1
        x += ax
        x %= len(rows[y])
        y += ay

    if (ax, ay) == angles[1]:
        part1 = trees
    part2 *= trees


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
