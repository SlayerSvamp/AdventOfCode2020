from common import timeit

card_key = 8421034  # my input
door_key = 15993936  # my input

mod = 20201227


def transform(loop_size, subject=7):
    value = 1
    for _ in range(loop_size):
        value *= subject
        value %= mod
    return value


def reverse(key):
    loop = 0
    while key != 1:
        if key % 7:
            key += mod * int('0531642'[key % 7])
        key //= 7
        loop += 1
    return loop


@timeit()
def part1(sender, reciever):
    sender_loop = reverse(sender)
    print(f'Part 1: {transform(sender_loop, reciever)}')


part1(card_key, door_key)

print("Part 2: I'm done!! yaay! :D")
