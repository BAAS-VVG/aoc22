def d9():
    print("D9")
    with open('d9.txt') as f:
        text = f.read().strip().split('\n')

    knots = [[0, 0]]
    for i in range(1, 10):
        knots.append([0, 0])
    visited1, visited2 = set(), set()
    visited1.add(tuple(knots[1]))
    visited2.add(tuple(knots[-1]))
    for line in text:
        line = line.split(' ')
        for i in range(int(line[1])):
            if line[0] == 'R':
                knots[0][0] += 1
            elif line[0] == 'L':
                knots[0][0] -= 1
            elif line[0] == 'U':
                knots[0][1] += 1
            else:
                knots[0][1] -= 1

            for knot in range(1, len(knots)):
                distsq = (knots[knot - 1][0] - knots[knot][0]) * (knots[knot - 1][0] - knots[knot][0]) + (
                        knots[knot - 1][1] - knots[knot][1]) * (knots[knot - 1][1] - knots[knot][1])
                if distsq > 4:
                    if knots[knot - 1][1] > knots[knot][1]:
                        knots[knot][1] += 1
                    elif knots[knot - 1][1] < knots[knot][1]:
                        knots[knot][1] -= 1
                    if knots[knot - 1][0] > knots[knot][0]:
                        knots[knot][0] += 1
                    elif knots[knot - 1][0] < knots[knot][0]:
                        knots[knot][0] -= 1
                elif distsq > 3:
                    if knots[knot - 1][0] > knots[knot][0]:
                        knots[knot][0] += 1
                    elif knots[knot - 1][0] < knots[knot][0]:
                        knots[knot][0] -= 1
                    elif knots[knot - 1][1] > knots[knot][1]:
                        knots[knot][1] += 1
                    else:
                        knots[knot][1] -= 1

            visited1.add(tuple(knots[1]))
            visited2.add(tuple(knots[-1]))
    print(len(visited1))
    print(len(visited2))
