def d4():
    print("D4")
    with open('d4.txt') as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        total = 0
        for line in lines:
            sets = sorted([set(range(int(vals.split('-')[0]), int(vals.split('-')[1]) + 1)) for vals in line], key=len)
            if sets[0] <= sets[1]:
                total += 1
    print(total)

    with open('d4.txt') as f:
        print(len([1 for line in f.readlines() if sorted(
            [set(range(int(vals.split('-')[0]), int(vals.split('-')[1]) + 1)) for vals in line.strip().split(',')],
            key=len)[0] & sorted(
            [set(range(int(vals.split('-')[0]), int(vals.split('-')[1]) + 1)) for vals in line.strip().split(',')],
            key=len)[1]]))
