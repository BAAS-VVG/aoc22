from queue import PriorityQueue as Pq


def putf(fringe, pos, cost, end):
    prio = cost + abs(end[0] - pos[0]) + abs(end[1] - pos[1])
    fringe.put([prio, pos, cost])


def read_grid():
    with open('d12.txt') as f:
        text = f.read().strip()

    grid = []
    y = 0

    for line in text.split('\n'):
        x = 0
        row = []
        for char in line:
            if char == 'S':
                row.append(1)
                start = (x, y)
            elif char == 'E':
                row.append(26)
                goal = (x, y)
            else:
                row.append(ord(char) - 96)
            x += 1
        grid.append(row)
        y += 1
    return grid, start, goal


def solve(f, grid, goal):
    visited = []
    while not f.empty():
        curr = f.get()
        pos = curr[1]
        cost = curr[2]
        if pos in visited:
            continue
        visited.append(pos)
        if pos == goal:
            print(cost)
            break

        h = grid[pos[1]][pos[0]]
        if pos[0] < len(grid[pos[1]]) - 1 and h - grid[pos[1]][pos[0] + 1] > -2:
            putf(f, (pos[0] + 1, pos[1]), cost + 1, goal)
        if pos[0] > 0 and h - grid[pos[1]][pos[0] - 1] > -2:
            putf(f, (pos[0] - 1, pos[1]), cost + 1, goal)
        if pos[1] < len(grid) - 1 and h - grid[pos[1] + 1][pos[0]] > -2:
            putf(f, (pos[0], pos[1] + 1), cost + 1, goal)
        if pos[1] > 0 and h - grid[pos[1] - 1][pos[0]] > -2:
            putf(f, (pos[0], pos[1] - 1), cost + 1, goal)


def d12():
    print("D12")
    grid, start, goal = read_grid()

    f = Pq()
    putf(f, start, 0, goal)
    solve(f, grid, goal)

    f = Pq()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == 1:
                putf(f, (x, y), 0, goal)
    solve(f, grid, goal)
