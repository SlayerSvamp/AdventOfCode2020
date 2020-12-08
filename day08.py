lines = open('data/day08.txt').read().splitlines()


def generateCode():
    code = []
    for line in lines:
        action, value = line.split(' ')
        code.append((action, int(value)))
    return code


def run(code):
    infinite = False
    acc = 0
    pos = 0
    visited = set()

    while pos not in visited:
        visited.add(pos)
        key, value = code[pos]
        if key == 'acc':
            acc += value
            pos += 1
        elif key == 'jmp':
            pos += value
        elif key == 'nop':
            pos += 1

        if pos >= len(code):
            break

    else:
        infinite = True
    return (infinite, acc)


code = generateCode()
_, part1 = run(code)

for pos in range(len(lines)):
    code = generateCode()
    key, value = code[pos]
    if key == 'jmp':
        key = 'nop'
    elif key == 'nop':
        key = 'jmp'
    code[pos] = (key, value)
    infinite, acc = run(code)
    if not infinite:
        break

print(f'Part 1: {part1}')
print(f'Part 2: {acc}')
