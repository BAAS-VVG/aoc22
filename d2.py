def d2():
    print("D2")
    with open('d2.txt') as f:
        score = 0
        for line in f.readlines():
            moves = line.split()
            if moves[1] == 'X':
                score += 1
                if moves[0] == 'A':
                    score += 3
                elif moves[0] == 'C':
                    score += 6
            elif moves[1] == 'Y':
                score += 2
                if moves[0] == 'A':
                    score += 6
                elif moves[0] == 'B':
                    score += 3
            else:
                score += 3
                if moves[0] == 'B':
                    score += 6
                elif moves[0] == 'C':
                    score += 3
        print(score)

    with open('d2.txt') as f:
        score = 0
        for line in f.readlines():
            moves = line.split()
            if moves[0] == 'A' and moves[1] == 'X':
                score += 3
            elif moves[0] == 'A' and moves[1] == 'Y':
                score += 4
            elif moves[0] == 'A' and moves[1] == 'Z':
                score += 8
            elif moves[0] == 'B' and moves[1] == 'X':
                score += 1
            elif moves[0] == 'B' and moves[1] == 'Y':
                score += 5
            elif moves[0] == 'B' and moves[1] == 'Z':
                score += 9
            elif moves[0] == 'C' and moves[1] == 'X':
                score += 2
            elif moves[0] == 'C' and moves[1] == 'Y':
                score += 6
            elif moves[0] == 'C' and moves[1] == 'Z':
                score += 7
        print(score)
