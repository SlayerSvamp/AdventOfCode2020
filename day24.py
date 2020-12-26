lines = open('data/day24.txt').read().splitlines()
black = set()
directions = {
    'e': (0, 2),
    'se': (1, 1),
    'sw': (1, -1),
    'w': (0, -2),
    'nw': (-1, -1),
    'ne': (-1, 1),
}

for line in lines:
    y, x = 0, 0
    while line:
        count = (line[0] in 'sn') + 1
        direction, line = line[:count], line[count:]
        dy, dx = directions[direction]
        y += dy
        x += dx
    tile = y, x
    if tile in black:
        black.remove(tile)
    else:
        black.add(tile)
part1 = len(black)


for _ in range(100):
    adjacent = dict.fromkeys(black, 0)
    for y, x in black:
        for dy, dx in directions.values():
            tile = y + dy, x + dx
            adjacent.setdefault(tile, 0)
            adjacent[tile] += 1
    last = set(black)
    for tile, count in adjacent.items():
        if tile in last:
            if count not in [1, 2]:
                black.remove(tile)
        elif count == 2:
            black.add(tile)
part2 = len(black)


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
