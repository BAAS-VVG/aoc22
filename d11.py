from queue import Queue


class Monkey:
    def __init__(self, part2):
        self.items = Queue()
        self.operator = ""
        self.opvalue = ""
        self.test = 0
        self.true = 0
        self.false = 0
        self.inspections = 0
        self.part2 = part2

    def inspect(self, monkeys):
        while not self.items.empty():
            item = self.items.get()
            val = item if self.opvalue == "old" else int(self.opvalue)
            item = item + val if self.operator == "+" else item * val
            if not self.part2:
                item //= 3

            item %= 9699690
            monkey = self.true if item % self.test == 0 else self.false
            monkeys[monkey].items.put(item)
            self.inspections += 1


def d11():
    print("D11")
    with open('d11.txt') as f:
        text = f.read()

    monkeys1, monkeys2 = [], []
    for line in text.split('\n'):
        if line == '':
            continue
        line = [x.strip(" :,") for x in line.split(' ') if len(x) > 0]
        if line[0] == 'Monkey':
            monkeys1.append(Monkey(False))
            monkeys2.append(Monkey(True))
            monkey = int(line[1])
        elif line[0] == 'Starting':
            for item in line[2:]:
                monkeys1[monkey].items.put(int(item))
                monkeys2[monkey].items.put(int(item))
        elif line[0] == 'Operation':
            monkeys1[monkey].operator = line[4]
            monkeys2[monkey].operator = line[4]
            monkeys1[monkey].opvalue = line[5]
            monkeys2[monkey].opvalue = line[5]
        elif line[0] == 'Test':
            monkeys1[monkey].test = int(line[-1])
            monkeys2[monkey].test = int(line[-1])
        elif line[1] == 'true':
            monkeys1[monkey].true = int(line[-1])
            monkeys2[monkey].true = int(line[-1])
        else:
            monkeys1[monkey].false = int(line[-1])
            monkeys2[monkey].false = int(line[-1])

    for _ in range(20):
        for monkey in monkeys1:
            monkey.inspect(monkeys1)

    inspections = sorted([monkey.inspections for monkey in monkeys1])
    print(inspections[-2] * inspections[-1])

    for _ in range(10000):
        for monkey in monkeys2:
            monkey.inspect(monkeys2)

    inspections = sorted([monkey.inspections for monkey in monkeys2])
    print(inspections[-2] * inspections[-1])
