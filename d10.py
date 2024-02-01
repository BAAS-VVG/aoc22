def d10():
    print("D10")
    with open("d10.txt") as f:
        text = f.read().strip()

    res1 = []
    res2 = ""
    x = 1
    cycle = 1
    for line in text.split('\n'):
        if line == "noop":
            val = 0
            t = 1
        else:
            val = int(line.split(' ')[1])
            t = 2

        for _ in range(t):
            if (cycle + 20) % 40 == 0:
                res1.append(x * cycle)

            if abs(x - ((cycle - 1) % 40)) < 2:
                res2 += '#'
            else:
                res2 += '.'

            if cycle % 40 == 0:
                res2 += '\n'
            cycle += 1

        x += val

    print(sum(res1))
    print(res2)
