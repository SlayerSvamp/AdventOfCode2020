def play_memory_game(dinner_time):
    starting_numbers = [5, 2, 8, 16, 18, 0, 1]  # my input
    turn_spoken = {number: turn + 1 for turn, number in enumerate(starting_numbers)}
    most_recently_spoken = starting_numbers[-1]
    for turn in range(len(starting_numbers), dinner_time):
        spoken = turn - turn_spoken.get(most_recently_spoken, turn)
        turn_spoken[most_recently_spoken] = turn
        most_recently_spoken = spoken
    return spoken


print(f'Part 1: {play_memory_game(2020)}')
print(f'Part 2: {play_memory_game(30_000_000)}')
