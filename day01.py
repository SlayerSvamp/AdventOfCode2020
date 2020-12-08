lines = [int(x) for x in open('data/day01.txt').readlines()]

for x in lines:
    for y in lines:
        if x + y == 2020:
            print(f'{x} * {y} = {x*y}')
            break
    else:
        continue
    break

for x in lines:
    for y in lines:
        for z in lines:
            if x + y + z == 2020:
                print(f'{x} * {y} * {z} = {x*y*z}')
                break
        else:
            continue
        break
    else:
        continue
    break
