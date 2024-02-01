from queue import Queue


def neighbours(coord):
    yield tuple((coord[0] - 1, coord[1], coord[2]))
    yield tuple((coord[0] + 1, coord[1], coord[2]))
    yield tuple((coord[0], coord[1] - 1, coord[2]))
    yield tuple((coord[0], coord[1] + 1, coord[2]))
    yield tuple((coord[0], coord[1], coord[2] - 1))
    yield tuple((coord[0], coord[1], coord[2] + 1))


def d18():
    print("D18")
    with open('d18.txt') as f:
        text = f.read().strip().split('\n')

    coords = [tuple([int(char) for char in line.split(',')]) for line in text]

    total = sum([2 for i1, c1 in enumerate(coords) for i2, c2 in enumerate(coords) if
                 i1 < i2 and abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2]) == 1])

    surface = len(coords) * 6 - total
    print(surface)

    mnc = coords[1]
    mxc = coords[1]
    for c in coords:
        if c[0] < mnc[0]:
            mnc = (c[0], mnc[1], mnc[2])
        if c[1] < mnc[1]:
            mnc = (mnc[0], c[1], mnc[2])
        if c[2] < mnc[2]:
            mnc = (mnc[0], mnc[1], c[2])
        if c[0] > mxc[0]:
            mxc = (c[0], mxc[1], mxc[2])
        if c[1] > mxc[1]:
            mxc = (mxc[0], c[1], mxc[2])
        if c[2] > mxc[2]:
            mxc = (mxc[0], mxc[1], c[2])

    mnc = tuple(map(lambda i, j: i - j, mnc, (1, 1, 1)))
    mxc = tuple(map(lambda i, j: i + j, mxc, (1, 1, 1)))

    q = Queue()
    q.put(mnc)
    outerair = set()
    while not q.empty():
        c = q.get()
        if c in outerair:
            continue
        if c[0] < mnc[0] or c[1] < mnc[1] or c[2] < mnc[2] or c[0] > mxc[0] or c[1] > mxc[1] or c[2] > mxc[2]:
            continue

        outerair.add(c)

        for n in neighbours(c):
            if n not in coords:
                q.put(n)

    surface = 0
    for c in coords:
        for n in neighbours(c):
            if n in outerair:
                surface += 1

    print(surface)
