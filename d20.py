from collections import deque


def solve(key=1, times=1):
    with open('d20.txt') as f:
        dq = deque([(i, v * key) for i, v in enumerate([int(x) for x in f])])

    for _ in range(times):
        for i in range(len(dq)):
            while dq[0][0] != i:
                dq.rotate()
            old_i, n = dq.popleft()
            dq.rotate(-(n % len(dq)))
            dq.appendleft((old_i, n))

    while dq[0][1] != 0:
        dq.rotate()

    print(sum([dq[1000 % len(dq)][1], dq[2000 % len(dq)][1], dq[3000 % len(dq)][1]]))


def d20():
    print("D20")
    solve()
    solve(811589153, 10)
