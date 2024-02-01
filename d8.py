import math


def helper8(lst, height):
    s = 0
    for t in lst:
        s += 1
        if t >= height:
            break
    return s


def d8():
    print("D8")
    with open('d8.txt') as f:
        text = f.read().strip()
    grid = [[int(char) for char in line] for line in text.split('\n')]

    print(sum([1 for r in range(len(grid)) for c in range(len(grid[0])) if not all(
        [any(1 for t in a if t >= grid[r][c]) for a in
         [grid[r][:c], grid[r][c + 1:], [l[c] for l in grid[:r]], [l[c] for l in grid[r + 1:]]]])]))

    print(max([math.prod([helper8(a, grid[r][c]) for a in
                          [reversed(grid[r][:c]), grid[r][c + 1:], reversed([l[c] for l in grid[:r]]),
                           [l[c] for l in grid[r + 1:]]]]) for r in range(len(grid)) for c in range(len(grid[0]))]))
