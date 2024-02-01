import math
import re
from multiprocessing import Pool
from queue import PriorityQueue


def solve2(args):
    (bp, timelimit) = args
    maximum = 0

    time = 0
    ore = 0
    clay = 0
    obs = 0
    geode = 0
    orebots = 1
    claybots = 0
    obsbots = 0
    geobots = 0
    q = PriorityQueue()
    visited = set()
    q.put((0, time, ore, clay, obs, geode, orebots, claybots, obsbots, geobots))
    while not q.empty():
        curr = q.get()
        if curr in visited:
            continue
        (prio, time, ore, clay, obs, geode, orebots, claybots, obsbots, geobots) = curr

        if maximum < geode:
            maximum = geode

        if time >= timelimit:
            continue

        if (timelimit - time) * ((timelimit - time - 1) / 2 + geobots) + geode < maximum:
            continue

        maxorebots = max(bp[0], bp[1], bp[2], bp[4]) - ore // (timelimit - time)
        maxclaybots = bp[3] - clay // (timelimit - time)
        maxobsbots = bp[5] - obs // (timelimit - time)

        if obsbots > 0:
            t = min(max(math.ceil((bp[4] - ore) / orebots), math.ceil((bp[5] - obs) / obsbots)) + 1, timelimit - time)
            q.put((prio - geobots * t, time + t, ore + orebots * t - bp[4], clay + claybots * t,
                   obs + obsbots * t - bp[5], geode + geobots * t, orebots, claybots, obsbots, geobots + 1))
        if obsbots <= maxobsbots and claybots > 0:
            t = min(max(math.ceil((bp[2] - ore) / orebots), math.ceil((bp[3] - clay) / claybots)) + 1, timelimit - time)
            q.put((prio - geobots * t, time + t, ore + orebots * t - bp[2], clay + claybots * t - bp[3],
                   obs + obsbots * t, geode + geobots * t, orebots, claybots, obsbots + 1, geobots))
        if claybots <= maxclaybots:
            t = min(math.ceil((bp[1] - ore) / orebots) + 1, timelimit - time)
            q.put((prio - geobots * t, time + t, ore + orebots * t - bp[1], clay + claybots * t,
                   obs + obsbots * t, geode + geobots * t, orebots, claybots + 1, obsbots, geobots))
        if orebots <= maxorebots:
            t = min(math.ceil((bp[0] - ore) / orebots) + 1, timelimit - time)
            q.put((prio - geobots * t, time + t, ore + orebots * t - bp[0], clay + claybots * t,
                   obs + obsbots * t, geode + geobots * t, orebots + 1, claybots, obsbots, geobots))
        visited.add(curr)
    return maximum


def solve(args):
    (bp, timelimit) = args
    maximum = 0

    time = 0
    ore = 0
    clay = 0
    obsidian = 0
    geode = 0
    orebots = 1
    claybots = 0
    obsidianbots = 0
    geodebots = 0
    q = PriorityQueue()
    visited = set()
    q.put((0, time, ore, clay, obsidian, geode, orebots, claybots, obsidianbots, geodebots))
    while not q.empty():
        curr = q.get()
        if curr in visited:
            continue
        (prio, time, ore, clay, obsidian, geode, orebots, claybots, obsidianbots, geodebots) = curr

        if maximum < geode:
            maximum = geode

        if time == timelimit:
            continue

        if (timelimit - time) * ((timelimit - time - 1) / 2 + geodebots) + geode < maximum:
            continue

        maxorebots = max(bp[0], bp[1], bp[2], bp[4]) - ore // (timelimit - time)
        maxclaybots = bp[3] - clay // (timelimit - time)
        maxobsbots = bp[5] - obsidian // (timelimit - time)

        if bp[4] <= ore and bp[5] <= obsidian:
            q.put((prio - geodebots, time + 1, ore + orebots - bp[4], clay + claybots, obsidian + obsidianbots - bp[5],
                   geode + geodebots, orebots, claybots, obsidianbots, geodebots + 1))
        elif bp[2] <= ore and bp[3] <= clay and obsidianbots < maxobsbots:
            q.put((prio - geodebots, time + 1, ore + orebots - bp[2], clay + claybots - bp[3],
                   obsidian + obsidianbots, geode + geodebots, orebots, claybots, obsidianbots + 1, geodebots))
        else:
            q.put((prio - geodebots, time + 1, ore + orebots, clay + claybots, obsidian + obsidianbots,
                   geode + geodebots, orebots, claybots, obsidianbots, geodebots))

            if bp[0] <= ore and orebots < maxorebots:
                q.put((prio - geodebots, time + 1, ore + orebots - bp[0], clay + claybots, obsidian + obsidianbots,
                       geode + geodebots, orebots + 1, claybots, obsidianbots, geodebots))

            if bp[1] <= ore and claybots < maxclaybots:
                q.put((prio - geodebots, time + 1, ore + orebots - bp[1], clay + claybots, obsidian + obsidianbots,
                       geode + geodebots, orebots, claybots + 1, obsidianbots, geodebots))
        visited.add(curr)
    return maximum


def d19():
    print("D19")
    with open('d19.txt') as f:
        text = f.read().strip().split('\n')

    blueprints = {}
    for line in text:
        line = [int(x) for x in re.findall('\d+', line)]
        blueprints[line[0]] = tuple(line[1:])

    args = [(v, 24) for v in blueprints.values()]

    with Pool(12) as pool:
        lst = pool.map(solve, args)

    print(sum([(i + 1) * v for i, v in enumerate(lst)]))

    args = [(v, 32) for k, v in blueprints.items() if k < 4]
    with Pool(12) as pool:
        lst = pool.map(solve, args)

    print(lst[0] * lst[1] * lst[2])
