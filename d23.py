import sys
from collections import defaultdict


def neighbours(tpl):
    yield tpl[0] - 1, tpl[1] - 1
    yield tpl[0] - 1, tpl[1]
    yield tpl[0] - 1, tpl[1] + 1
    yield tpl[0], tpl[1] - 1
    yield tpl[0], tpl[1] + 1
    yield tpl[0] + 1, tpl[1] - 1
    yield tpl[0] + 1, tpl[1]
    yield tpl[0] + 1, tpl[1] + 1


def north(tpl):
    yield tpl[0] - 1, tpl[1] - 1
    yield tpl[0], tpl[1] - 1
    yield tpl[0] + 1, tpl[1] - 1


def south(tpl):
    yield tpl[0] - 1, tpl[1] + 1
    yield tpl[0], tpl[1] + 1
    yield tpl[0] + 1, tpl[1] + 1


def west(tpl):
    yield tpl[0] - 1, tpl[1] - 1
    yield tpl[0] - 1, tpl[1]
    yield tpl[0] - 1, tpl[1] + 1


def east(tpl):
    yield tpl[0] + 1, tpl[1] - 1
    yield tpl[0] + 1, tpl[1]
    yield tpl[0] + 1, tpl[1] + 1


def step1(world, rnd, prop):
    for k in world:
        if len(world.intersection(neighbours(k))) == 0:
            continue

        moves = [0, 1, 2, 3]  # N S W E
        for move in moves:
            move = (move + rnd) % 4

            if move == 0:
                if len(world.intersection(north(k))) == 0:
                    prop[(k[0], k[1] - 1)].append(k)
                    break
            if move == 1:
                if len(world.intersection(south(k))) == 0:
                    prop[(k[0], k[1] + 1)].append(k)
                    break
            if move == 2:
                if len(world.intersection(west(k))) == 0:
                    prop[(k[0] - 1, k[1])].append(k)
                    break
            if move == 3:
                if len(world.intersection(east(k))) == 0:
                    prop[(k[0] + 1, k[1])].append(k)
                    break


def solve(text, part1=False):
    world = set()
    for y, line in enumerate(text.splitlines()):
        for x, char in enumerate(list(line)):
            if char == '#':
                world.add((x, y))

    rnd = 0
    while True:
        if part1 and rnd == 10:
            minx = sys.maxsize
            maxx = -sys.maxsize
            miny = sys.maxsize
            maxy = -sys.maxsize

            for (x, y) in world:
                minx = min(minx, x)
                maxx = max(maxx, x)
                miny = min(miny, y)
                maxy = max(maxy, y)

            print((1 + maxx - minx) * (1 + maxy - miny) - len(world))
            return

        prop = defaultdict(lambda: [])
        step1(world, rnd, prop)

        if len(prop) == 0:
            print(rnd + 1)
            break

        for k, v in prop.items():
            if len(v) > 1:
                continue
            world.remove(v[0])
            world.add(k)

        rnd += 1


def d23():
    print("D23")
    with open('d23.txt') as f:
        text = f.read()

    solve(text, True)
    solve(text)

