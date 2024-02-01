import re
import numpy as np

dirs = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]

rx90 = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
rx270 = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
ry90 = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
ry270 = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])


def wrapcube(world, d, i, pos, size):
    f = (pos[0] // size, pos[1] // size)
    n = np.array([0, 0, -1])
    d = np.array(d)
    q = [(d, n, i, f)]
    while q:
        (d, n, i, f) = q.pop(0)

        if tuple(d) == (0, 0, 1):
            nd = dirs.index(tuple(n))

            return nd, (-2 * abs(i[0]) + size - 1) * ((nd % 3 + 1) // 2) + abs(i[0]) + f[0] * size, nd // 2 * (
                        -2 * abs(i[1]) + size - 1) + abs(i[1]) + f[1] * size

        if f[0] > 0 and world[f[1] * size][(f[0] - 1) * size] != ' ':
            q.append((ry270.dot(d), ry270.dot(n), ry270.dot(i), (f[0] - 1, f[1])))
        if f[1] > 0 and f[0] * size < len(world[(f[1] - 1) * size]) and world[(f[1] - 1) * size][(f[0]) * size] != ' ':
            q.append((rx270.dot(d), rx270.dot(n), rx270.dot(i), (f[0], f[1] - 1)))
        if (f[0] + 1) * size != len(world[f[1] * size]) and world[f[1] * size][(f[0] + 1) * size] != ' ':
            q.append((ry90.dot(d), ry90.dot(n), ry90.dot(i), (f[0] + 1, f[1])))
        if (f[1] + 1) * size != len(world) and f[0] * size < len(world[(f[1] + 1) * size]) and \
                world[(f[1] + 1) * size][(f[0]) * size] != ' ':
            q.append((rx90.dot(d), rx90.dot(n), rx90.dot(i), (f[0], f[1] + 1)))


def findnewpos2(world, pos, d, edgelen):
    (x, y) = pos
    nd = d

    x += dirs[d][0]
    y += dirs[d][1]

    if x < 0 or y < 0 or y == len(world) or x >= len(world[y]) or world[y][x] == ' ':  # wrap
        (nd, x, y) = wrapcube(world, dirs[d], np.array(
            [-dirs[d][1] * (pos[0] + d % 3) % edgelen, dirs[d][0] * (pos[1] + d // 2) % edgelen, 0]), pos, edgelen)

    if world[y][x] == '#':
        return pos, d
    return (x, y), nd


def findnewpos1(world, pos, d):
    (xpos, ypos) = pos
    newd = d
    if d == 0:
        xpos += 1
        if xpos == len(world[ypos]) or world[ypos][xpos] == ' ':
            for xpos in range(len(world[ypos])):
                if world[ypos][xpos] != ' ':
                    break
    if d == 1:
        ypos += 1
        if ypos == len(world) or xpos >= len(world[ypos]) or world[ypos][xpos] == ' ':
            for ypos in range(len(world)):
                if xpos < len(world[ypos]) and world[ypos][xpos] != ' ':
                    break
    if d == 2:
        xpos -= 1
        if xpos < 0 or world[ypos][xpos] == ' ':
            for xpos in range(len(world[ypos]) - 1, 0, -1):
                if world[ypos][xpos] != ' ':
                    break
    if d == 3:
        ypos -= 1
        if ypos < 0 or xpos >= len(world[ypos]) or world[ypos][xpos] == ' ':
            for ypos in range(len(world) - 1, 0, -1):
                if xpos < len(world[ypos]) and world[ypos][xpos] != ' ':
                    break

    if world[ypos][xpos] == '#':
        return pos, d
    return (xpos, ypos), newd


def solve(text):
    grid, instr = text.split('\n\n')
    world = []
    for line in grid.splitlines():
        world.append(list(line))

    edgelen = max(len(world), max(map(len, world))) // 4

    d = 0  # right
    pos = (world[0].index('.'), 0)

    numbers = [int(x) for x in re.findall('\d+', instr)]
    directions = [1 if x == 'R' else -1 for x in re.findall('[RL]', instr)]
    directions.append(0)

    for item in zip(numbers, directions):
        for _ in range(item[0]):
            pos, d = findnewpos1(world, pos, d)

        d += item[1]
        d %= 4

    print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + d)

    d = 0  # right
    pos = (world[0].index('.'), 0)
    for item in zip(numbers, directions):
        for _ in range(item[0]):
            pos, d = findnewpos2(world, pos, d, edgelen)

        d += item[1]
        d %= 4

    print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + d)


def d22():
    print("D22")
    # with open('test.txt') as f:
    #     solve(f.read())
    with open('d22.txt') as f:
        solve(f.read())
