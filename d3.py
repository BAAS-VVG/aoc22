def d3():
    print("D3")
    with open('d3.txt') as f:
        print(sum([v - 58 if v > 52 else v for v in
                   [ord(set(l[len(l) // 2:]).intersection(l[:len(l) // 2]).pop()) - 38 for l in f.readlines()]]))

    with open('d3.txt') as f:
        print(sum([v - 58 if v > 52 else v for v in [ord(set(l[0].strip()).intersection(l[1], l[2]).pop()) - 38 for l in
                                                     zip(*[iter(f.readlines())] * 3)]]))
