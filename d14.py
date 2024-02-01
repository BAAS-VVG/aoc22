def read_world():
    with open('d14.txt') as f:
        text = f.read().strip()

    world = set()

    for line in text.split('\n'):
        coords = [(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in line.split(' -> ')]

        for idx in range(len(coords) - 1):
            if coords[idx][0] == coords[idx + 1][0]:
                for y in range(coords[idx][1], coords[idx + 1][1], -1 if coords[idx + 1][1] < coords[idx][1] else 1):
                    world.add((coords[idx][0], y))
            if coords[idx][1] == coords[idx + 1][1]:
                for x in range(coords[idx][0], coords[idx + 1][0], -1 if coords[idx + 1][0] < coords[idx][0] else 1):
                    world.add((x, coords[idx][1]))

        world.add(coords[-1])
    return world


def simulate(world, floor, max_depth):
    sand = set()
    while True:
        if (500, 0) in sand:
            break
        x = 500
        for d in range(0, max_depth + 2):
            if (x, d + 1) not in world and (x, d + 1) not in sand and (x, d + 1) not in floor:
                continue
            if (x - 1, d + 1) not in world and (x - 1, d + 1) not in sand and (x - 1, d + 1) not in floor:
                x -= 1
                continue
            if (x + 1, d + 1) not in world and (x + 1, d + 1) not in sand and (x + 1, d + 1) not in floor:
                x += 1
                continue
            sand.add((x, d))
            break
        else:
            break

    print(len(sand))


def d14():
    print("D14")
    world = read_world()

    max_depth = sorted(world, key=lambda x: x[1])[-1][1]
    simulate(world, set(), max_depth)

    floor = set([(x, max_depth + 2) for x in range(500 - max_depth - 4, 500 + max_depth + 5)])
    simulate(world, floor, max_depth)
