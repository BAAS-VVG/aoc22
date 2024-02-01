from queue import Queue


def passtime(rows, cols, stormsn, stormse, stormss, stormsw):
    newstorms = set()
    for storm in stormsn:
        if storm[1] == 0:
            newstorms.add((storm[0], rows - 1))
        else:
            newstorms.add((storm[0], storm[1] - 1))
    stormsn = newstorms

    newstorms = set()
    for storm in stormsw:
        if storm[0] == 0:
            newstorms.add((cols - 1, storm[1]))
        else:
            newstorms.add((storm[0] - 1, storm[1]))
    stormsw = newstorms

    newstorms = set()
    for storm in stormse:
        if storm[0] == cols - 1:
            newstorms.add((0, storm[1]))
        else:
            newstorms.add((storm[0] + 1, storm[1]))
    stormse = newstorms

    newstorms = set()
    for storm in stormss:
        if storm[1] == rows - 1:
            newstorms.add((storm[0], 0))
        else:
            newstorms.add((storm[0], storm[1] + 1))
    stormss = newstorms

    return stormsn, stormse, stormss, stormsw


def solve(rows, cols, stormsn, stormse, stormss, stormsw, start, goal):
    q = Queue()
    visited = set()

    q.put((start[0], start[1], 1))
    t = 1
    while True:
        (x, y, time) = q.get()

        if (x, y, time) in visited:
            continue

        visited.add((x, y, time))

        if t == time:
            t += 1
            stormsn, stormse, stormss, stormsw = passtime(rows, cols, stormsn, stormse, stormss, stormsw)
            q.put((start[0], start[1], t))

        if x == goal[0] and y == goal[1]:
            return t, stormsn, stormse, stormss, stormsw

        pos = (x, y)
        if pos in stormsn:
            continue
        if pos in stormse:
            continue
        if pos in stormss:
            continue
        if pos in stormsw:
            continue

        q.put((x, y, t))
        if x + 1 < cols:
            q.put((x + 1, y, t))
        if x > 0:
            q.put((x - 1, y, t))
        if y + 1 < rows:
            q.put((x, y + 1, t))
        if y > 0:
            q.put((x, y - 1, t))


def d24():
    print("D24")
    with open('d24.txt') as f:
        text = f.read()

    stormsn = set()
    stormse = set()
    stormss = set()
    stormsw = set()

    lines = [line[1: -1] for line in text.splitlines()[1: -1]]

    cols = len(lines[0])
    rows = len(lines)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '^':
                stormsn.add((x, y))
            elif char == '>':
                stormse.add((x, y))
            elif char == 'v':
                stormss.add((x, y))
            elif char == '<':
                stormsw.add((x, y))

    t1, stormsn, stormse, stormss, stormsw = solve(rows, cols, stormsn, stormse, stormss, stormsw, (0, 0), (cols - 1, rows - 1))
    print(t1)
    stormsn, stormse, stormss, stormsw = passtime(rows, cols, stormsn, stormse, stormss, stormsw)
    t2, stormsn, stormse, stormss, stormsw = solve(rows, cols, stormsn, stormse, stormss, stormsw, (cols - 1, rows - 1), (0, 0))
    stormsn, stormse, stormss, stormsw = passtime(rows, cols, stormsn, stormse, stormss, stormsw)
    t3, stormsn, stormse, stormss, stormsw = solve(rows, cols, stormsn, stormse, stormss, stormsw, (0, 0), (cols - 1, rows - 1))

    print(t1 + t2 + t3)
