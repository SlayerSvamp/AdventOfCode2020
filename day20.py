from functools import reduce
from re import search as re_search
raw = [*map(str.splitlines, open('data/day20.txt').read().split('\n\n'))]


def main():
    assembler = ImageAssembler(raw)
    finder = MonsterFinder(assembler.image)
    # Common.draw(assembler.image) # draw sea before monsters are found
    # Common.draw(finder.image) # draw sea with monsters
    # Common.draw({key: value & 2 for key, value in finder.image.items()}) # draw only sea monsters, no roughness

    part1 = reduce(lambda x, y: x * y.id, assembler.corners, 1)
    part2 = sum(x == 1 for x in finder.image.values())

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


class Common:
    @staticmethod
    def draw(data):
        pixel = ['  ', '██', '()']
        y1, x1 = max(data.keys())
        for y in range(y1 + 1):
            line = ''
            for x in range(x1 + 1):
                line += pixel[data[y, x]]
            print(line)

    @staticmethod
    def flip(data):
        new = {}
        y1, x1 = max(data.keys())
        for y in range(y1 + 1):
            for x in range(x1 + 1):
                new[y1 - y, x] = data[y, x]
        return new

    @staticmethod
    def rotate(data):
        new = {}
        y1, x1 = max(data.keys())
        for y in range(y1 + 1):
            for x in range(x1 + 1):
                new[x, y1 - y] = data[y, x]
        return new


class ImageAssembler:
    def __init__(self, raw):
        self.tiles = {}
        self.tile_size = len(raw[0][1])
        self.corners = []
        self.leftmost = None
        self.image = {}
        self.load(raw)

    def load(self, raw):
        for lines in raw:
            tile = Tile(lines, self.tile_size)
            self.tiles[tile.id] = tile

        tiles = set(self.tiles.values())
        current = tiles.pop()
        current.connect(tiles)

        self.find_corners()
        self.combine()

    def find_corners(self):
        for tile in self.tiles.values():
            if len(tile.connections) == 2:
                self.corners.append(tile)
                if 2 not in tile.connections and 3 not in tile.connections:
                    self.leftmost = tile

    def combine(self):
        leftmost = self.leftmost
        offset_y = 0
        while leftmost:
            tile = leftmost
            offset_x = 0
            while tile:
                for y in range(self.tile_size - 2):
                    for x in range(self.tile_size - 2):
                        self.image[y+offset_y, x +
                                   offset_x] = tile.data[y + 1, x + 1]
                tile = tile.connections.get(0)
                offset_x += self.tile_size - 2
            leftmost = leftmost.connections.get(1)
            offset_y += self.tile_size - 2


class Tile:
    def __init__(self, lines, size):
        id_raw, *lines = lines
        self.id = int(re_search(r'\d+', id_raw)[0])
        self.rotated = 0
        self.flipped = 0
        self.connections = {}
        self.data = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                self.data[y, x] = char == '#'
        self.sides = [
            [self.data[i, size - 1] for i in range(size)],
            [self.data[size - 1, i] for i in range(size)],
            [self.data[i, 0] for i in range(size)],
            [self.data[0, i] for i in range(size)],
        ]

    def flip_sides(self):
        self.flipped ^= 1
        self.sides = [
            self.sides[0][::-1],
            self.sides[3],
            self.sides[2][::-1],
            self.sides[1],
        ]

    def rotate_sides(self):
        self.rotated += 1
        self.sides = [
            self.sides[3],
            self.sides[0][::-1],
            self.sides[1],
            self.sides[2][::-1],
        ]

    def apply_orientation(self):
        if self.flipped:
            self.data = Common.flip(self.data)
            self.flipped = 0
        while self.rotated % 4:
            self.data = Common.rotate(self.data)
            self.rotated -= 1

    def side(self, side):
        side = {'right': 0, 'down': 1, 'left': 2, 'up': 3}.get(side, side)
        return self.sides[side]

    def connect(self, tiles: set):
        def inner(side, tile_side):
            for tile in tiles:
                for _ in range(2):  # flip
                    for _ in range(4):  # rotate
                        if self.side(side) == tile.side(tile_side):
                            self.connections[side] = tile
                            tile.connections[tile_side] = self
                            tile.apply_orientation()
                            return tile
                        tile.rotate_sides()
                    tile.flip_sides()

        new_connections = []
        for side in range(4):
            if side in self.connections:
                continue
            tile_side = (side + 2) % 4
            tile = inner(side, tile_side)
            if tile:
                new_connections.append(tile)
        if self in tiles:
            tiles.remove(self)

        for side, tile in self.connections.items():
            if tile in new_connections:
                tile.connect(tiles)
                if tile in tiles:
                    tiles.remove(tile)


class MonsterFinder:
    def __init__(self, image):
        self.image = image
        self.sea_monster = [
            '                  # ',
            '#    ##    ##    ###',
            ' #  #  #  #  #  #   ',
        ]
        self.search()

    def sea_monster_at(self, y, x, draw=False):
        for dy, line in enumerate(self.sea_monster):
            for dx, char in enumerate(line):
                if char == '#':
                    if self.image.get((y+dy, x+dx), 0) in [0]:
                        return False
        return True

    def draw_monster(self, y, x):
        for dy, line in enumerate(self.sea_monster):
            for dx, char in enumerate(line):
                if char == '#':
                    self.image[y+dy, x+dx] = 2
        return True

    def search(self):
        y1, x1 = max(self.image)
        sm_height = len(self.sea_monster)
        sm_width = len(self.sea_monster[0])
        for _ in range(2):
            for _ in range(4):
                for y in range(y1 + 1 - sm_height):
                    for x in range(x1 + 1 - sm_width):
                        if self.sea_monster_at(y, x):
                            self.draw_monster(y, x)
                if 2 in self.image.values():
                    return
                self.image = Common.rotate(self.image)
            self.image = Common.flip(self.image)


main()
