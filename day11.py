from common import timeit
from PIL import ImageDraw, Image


class Chair:
    chairs = {}
    max_y = 0
    people_limit = 0

    @staticmethod
    def get(coords):
        return Chair.chairs.get(coords)

    def __init__(self, coords):
        self.coords = coords
        self.y, self.x = coords
        Chair.max_y = max(Chair.max_y, self.y)
        self.adjacent = set()
        self.occupied = False
        self.people = 0
        self.mod = 0
        Chair.chairs[coords] = self

    def act(self):
        change = 0
        if self.occupied:
            if self.people >= Chair.people_limit:
                change = -1
        elif self.people == 0:
            change = 1

        if not change:
            return False

        self.occupied ^= True
        for adj in self.adjacent:
            adj.mod += change
        return True

    def apply(self):
        self.people += self.mod
        self.mod = 0

    @staticmethod
    def setup(line_of_sight):
        Chair.people_limit = 5 if line_of_sight else 4

        for y, x in sorted(Chair.chairs):
            chair: Chair = Chair.get((y, x))
            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1)]:
                ny, nx = y+dy, x+dx
                neighbor = None
                while not neighbor:
                    neighbor = Chair.get((ny, nx))
                    ny += dy
                    nx += dx
                    if not line_of_sight or ny < 0 or ny > Chair.max_y or nx < 0:
                        break

                if neighbor:
                    chair.adjacent.add(neighbor)
                    neighbor.adjacent.add(chair)

    @staticmethod
    @timeit
    def tick():
        change = True
        ticks = 0
        while change:
            change = False
            for chair in Chair.chairs.values():
                change |= chair.act()
            for chair in Chair.chairs.values():
                chair.apply()
            ticks += 1
        return ticks-1

    @staticmethod
    def print_grid():
        height = len(rows)
        width = len(rows[0])
        dot_size = 4
        image_size = (height*dot_size, width * dot_size)
        background = (200, 200, 255, 255)
        occupied = (100, 50, 60, 255)
        vacant = (50, 100, 60, 255)

        img = Image.new('RGBA', image_size, background)
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                chair = Chair.get((y, x))
                if chair:
                    color = [vacant, occupied][chair.occupied]
                    for dy in range(dot_size):
                        for dx in range(dot_size):
                            pixels[y*dot_size + dy, x*dot_size + dx] = color
        img.show()

    @staticmethod
    def count_occupied():
        return sum(c.occupied for c in Chair.chairs.values())

    @staticmethod
    def reset():
        for chair in Chair.chairs.values():
            chair.occupied = False
            chair.people = 0
            chair.mod = 0
            chair.adjacent.clear()


rows = open('data/day11.txt').read().splitlines()
grid = [(y, x) for y, row in enumerate(rows)
        for x, cell in enumerate(row) if cell == 'L']

for coords in grid:
    Chair(coords)


@timeit
def _part1():
    Chair.setup(False)
    ticks1 = Chair.tick()
    part1 = Chair.count_occupied()
    # Chair.print_grid()
    print(f'Ticks 1: {ticks1}')
    print(f'Part 1: {part1}')

@timeit
def _part2():
    print()
    Chair.reset()
    Chair.setup(True)
    ticks2 = Chair.tick()
    part2 = Chair.count_occupied()
    # Chair.print_grid()
    print(f'Ticks 2: {ticks2}')
    print(f'Part 2: {part2}')

_part1()
_part2()