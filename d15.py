import re
import sys
from multiprocessing import Pool

from shapely import Polygon, LineString, geometry
from shapely.ops import unary_union


def solve1(args):
    (x, sensors, trow) = args
    world = set()
    for key, v in sensors.items():
        if abs(key[0] - x) + abs(key[1] - trow) <= v:
            world.add((x, trow))
    return world


def part1(sensors, beacons, minx, maxx, trow):
    world = set()
    args = [(x, sensors, trow) for x in range(minx, maxx + 1)]
    with Pool(12) as p:
        res = p.map(solve1, args)

    for w in res:
        world |= w

    world = world - beacons
    print(len([coord for coord in world if coord[1] == trow]))


def part2(sensors, maxval):
    possible_locations = set()

    for key, v in sensors.items():
        for d1 in range(v + 1):
            d2 = v + 1 - d1
            if key[0] + d1 <= maxval and key[1] + d2 <= maxval:
                possible_locations.add((key[0] + d1, key[1] + d2))
            if key[0] + d2 <= maxval and key[1] - d1 >= 0:
                possible_locations.add((key[0] + d2, key[1] - d1))
            if key[0] - d1 >= 0 and key[1] - d2 >= 0:
                possible_locations.add((key[0] - d1, key[1] - d2))
            if key[0] - d2 >= 0 and key[1] + d1 <= maxval:
                possible_locations.add((key[0] - d2, key[1] + d1))

    for coord in possible_locations:
        for key, v in sensors.items():
            if abs(key[0] - coord[0]) + abs(key[1] - coord[1]) <= v:
                break
        else:
            print(coord[0] * 4000000 + coord[1])
            break


def d15():
    print("D15 (slow)")
    with open('d15.txt') as f:
        text = f.read()

    trow = 2000000
    maxval = 4000000
    sensors = {}
    beacons = set()
    minx = sys.maxsize
    maxx = -sys.maxsize - 1
    for line in text.split('\n'):
        line = line.split(' ')
        sensor = (int(line[2].strip('x=,')), int(line[3].strip('y=:')))
        beacon = (int(line[-2].strip('x=,')), int(line[-1].strip('y=:')))
        beacons.add(beacon)

        maxdist = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        sensors[sensor] = maxdist

        if sensor[0] - maxdist < minx:
            minx = sensor[0] - maxdist
        if sensor[0] + maxdist > maxx:
            maxx = sensor[0] + maxdist

    part1(sensors, beacons, minx, maxx, trow)

    part2(sensors, maxval)


def d15_2():
    print("D15 (fast)")
    with open('d15.txt') as f:
        text = f.read()

    text = [int(x) for x in re.findall('-?\d+', text)]

    sensorx = text[0::4]
    sensory = text[1::4]
    beaconx = text[2::4]
    beacony = text[3::4]

    coverage = []
    maxdist = 0

    for sx, sy, bx, by in zip(sensorx, sensory, beaconx, beacony):
        xrange = max(sx, bx) - min(sx, bx)
        yrange = max(sy, by) - min(sy, by)
        dist = xrange + yrange
        maxdist = max(maxdist, dist)
        coverage.append(Polygon([(sx + dist, sy), (sx, sy - dist), (sx - dist, sy), (sx, sy + dist)]))

    minx = min([c.bounds[0] for c in coverage]) - maxdist
    maxx = max([c.bounds[2] for c in coverage]) + maxdist + 1
    trow = 2000000
    bonline = set([beaconx[i] for i, b in enumerate(beacony) if b == trow])
    notbeacons = LineString([(minx, trow), (maxx, trow)]).intersection(unary_union(coverage))

    print(int(notbeacons.length) + 1 - len(bonline))

    maxval = 4000000
    box = geometry.box(0, 0, maxval, maxval)
    answer = box.difference(unary_union(coverage))
    print(int((answer.bounds[0] + 1) * maxval + answer.bounds[1] + 1))
