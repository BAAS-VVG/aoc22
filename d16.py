from collections import defaultdict
from queue import Queue


def read_input():
    with open('d16.txt') as f:
        text = f.read().strip()

    connections = {}
    valves = {}
    for line in text.split('\n'):
        line = line.split(' ')
        curr = line[1]
        val = int(line[4].split('=')[1][:-1])
        if val > 0:
            valves[curr] = val

        others = [dest.strip(',') for dest in line[9:]]
        for other in others:
            connections[(curr, other)] = 1

    return valves, connections


def build_paths(valves, connections):
    paths = {}
    q = Queue()
    for source in list(valves) + ["AA"]:
        q.put((source, 1))
        while not q.empty():
            curr = q.get()
            for connection in connections:
                if connection[0] != curr[0]:
                    continue
                if connection[1] == source:
                    continue
                if (source, connection[1]) in paths:
                    continue
                q.put((connection[1], curr[1] + 1))
                paths[(source, connection[1])] = curr[1] + 1

    keys = [key for key in paths if key[1] not in valves]

    for key in keys:
        del paths[key]
    return paths


def solve(paths, valves, time):
    q = Queue()
    visited = defaultdict(lambda: 0)

    q.put(("AA", time, 0, []))

    while not q.empty():
        curr = q.get()
        if curr[0] != "AA":
            curr[3].append(curr[0])

        idx = frozenset(curr[3])
        if visited[idx] < curr[2]:
            visited[idx] = curr[2]

        for path in paths:
            if path[0] != curr[0]:
                continue
            if path[1] in curr[3]:
                continue
            if curr[1] - paths[path] <= 0:
                continue
            lst = curr[3].copy()

            q.put((path[1], curr[1] - paths[path], curr[2] + (curr[1] - paths[path]) * valves[path[1]], lst))
    return visited


def d16():
    print("D16")
    valves, connections = read_input()
    paths = build_paths(valves.keys(), connections)

    print(max(solve(paths, valves, 30).values()))

    res = solve(paths, valves, 26)
    print(max(v1 + v2 for k1, v1 in res.items() for k2, v2 in res.items() if k1.isdisjoint(k2)))
