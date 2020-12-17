lines = open('data/day17.txt').read().splitlines()

def run(is_part2=False):
    dimension = {(x, y, 0, 0)
                 for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#'}

    def neighbors(pos):
        close = {-1, 0, 1}
        x, y, z, w = pos
        return {(x + dx, y + dy, z + dz, w + is_part2* dw)
                for dx in close for dy in close for dz in close for dw in close
                if dx or dy or dz or (dw and is_part2)}

    for _ in range(6):
        next_state = set(dimension)
        neighbors_by_pos = {}
        for pos in dimension:
            count = 0
            for neighbor in neighbors(pos):
                neighbors_by_pos[neighbor] = neighbors_by_pos.get(neighbor, 0) + 1
                if neighbor in dimension:
                    count += 1
            if count not in {2, 3}:
                next_state.remove(pos)
        for pos, count in neighbors_by_pos.items():
            if pos not in next_state and count == 3:
                next_state.add(pos)

        dimension = next_state

    return len(dimension)


print(f'Part 1: {run()}')
print(f'Part 2: {run(True)}')
