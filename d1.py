def d1():
    print("D1")
    with open('d1.txt') as f:
        print(sorted([sum([int(n) for n in elf.split() if n.isnumeric()]) for elf in f.read().split("\n\n")])[-1])
    with open('d1.txt') as f:
        print(sum(sorted([sum([int(n) for n in elf.split() if n.isnumeric()]) for elf in f.read().split("\n\n")])[-3:]))
