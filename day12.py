lines = open('data/day12.txt').read().splitlines()

cardinal = 'ESWN'
cardinal_diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Part 1
y1, x1 = 0, 0
direction = 0
# Part 2
y2, x2 = 0, 0
wy, wx = -1, 10  # waypoint

for action, *value in lines:
    value = int(''.join(value))
    if action in cardinal:
        dy, dx = cardinal_diff[cardinal.index(action)]
        # Part 1
        y1 += dy * value
        x1 += dx * value
        # Part 2
        wy += dy * value
        wx += dx * value
    elif action in 'LR':
        diff = value // 90 * [3, 1][action == 'R'] % 4
        # Part 1
        direction = (direction + diff) % 4
        # Part 2
        wy, wx = [(wy, wx), (wx, -wy), (-wy, -wx), (-wx, wy)][diff]
    else:  # action == 'F'
        # Part 1
        dy, dx = cardinal_diff[direction]
        y1 += dy * value
        x1 += dx * value
        # Part 2
        y2 += wy * value
        x2 += wx * value


print(f'Part 1: {abs(y1) + abs(x1)}')
print(f'Part 2: {abs(y2) + abs(x2)}')
