lines = [x.replace('-', ' ').replace(':', '').split(' ')
         for x in open('data/day02.txt').readlines()]

part1 = 0
part2 = 0
for [low, high, char, password] in lines:
    low = int(low)
    high = int(high)
    count = sum(1 for x in password if x == char)
    if count >= low and count <= high:
        part1 += 1
    if (password[low-1] == char) is not (password[high-1] == char):
        part2 += 1


print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
