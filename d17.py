from collections import defaultdict


class Rock:
    def __init__(self, shape, height):
        self.coords = [(coord[0], coord[1] + height) for coord in shape]

    def move_right(self, world):
        for coord in self.coords:
            if coord[0] + 1 > 6 or world[coord[1]][coord[0] + 1] == '#':
                return

        self.coords = [(coord[0] + 1, coord[1]) for coord in self.coords]

    def move_left(self, world):
        for coord in self.coords:
            if coord[0] - 1 < 0 or world[coord[1]][coord[0] - 1] == '#':
                return

        self.coords = [(coord[0] - 1, coord[1]) for coord in self.coords]

    def move_down(self, world):
        for coord in self.coords:
            if coord[1] - 1 < 0 or world[coord[1] - 1][coord[0]] == '#':
                for pos in self.coords:
                    world[pos[1]] = world[pos[1]][:pos[0]] + '#' + world[pos[1]][pos[0] + 1:]
                return False

        self.coords = [(coord[0], coord[1] - 1) for coord in self.coords]
        return True

    def max_y(self):
        return max([coord[1] for coord in self.coords]) + 1


def solve(shapes, text, num_rocks):
    shape = 0
    max_h = 0

    visited = {}

    height_skipped = 0
    w = defaultdict(lambda: ".......")
    rock = Rock(shapes[shape % 5], max_h)
    while True:
        for char in range(len(text)):
            if text[char] == '>':
                rock.move_right(w)
            else:
                rock.move_left(w)
            if rock.move_down(w):
                continue

            if rock.max_y() > max_h:
                max_h = rock.max_y()

            if height_skipped == 0:
                point_list = []
                for y, v in w.items():
                    if y + 18 > max_h:
                        for x, c in enumerate(v):
                            if c == '#':
                                point_list.append((x, y - max_h))

                key = (shape % 5, char, frozenset(point_list))

                if key in visited.keys():
                    height_skipped = (max_h - visited[key][0]) * ((num_rocks - shape) // (shape - visited[key][1]))
                    shape = num_rocks - (num_rocks - shape) % (shape - visited[key][1])
                else:
                    visited[key] = (max_h, shape)

            shape += 1
            if shape == num_rocks:
                print(max_h + height_skipped)
                return

            rock = Rock(shapes[shape % 5], max_h)


def d17():
    print("D17")
    with open('d17.txt') as f:
        text = f.read().strip()

    shapes = [[(2, 3), (3, 3), (4, 3), (5, 3)], [(2, 4), (3, 3), (3, 4), (3, 5), (4, 4)],
              [(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)], [(2, 3), (2, 4), (2, 5), (2, 6)],
              [(2, 3), (2, 4), (3, 3), (3, 4)]]

    solve(shapes, text, 2022)
    solve(shapes, text, 1000000000000)
