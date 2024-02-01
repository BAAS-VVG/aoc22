import itertools
from queue import LifoQueue as Stack


def d5():
    print("D5")
    with open('d5.txt') as f:
        config, tasks = f.read().split("\n\n", 1)

    stacks1, stacks2 = [Stack()], [Stack()]
    text = [list(line) for line in config.split('\n')]
    for col in [col for col in itertools.zip_longest(*reversed(text), fillvalue=' ') if col[0] != ' ']:
        stack1, stack2 = Stack(), Stack()
        for i in range(1, len(text)):
            if col[i] == ' ':
                break
            stack1.put(col[i])
            stack2.put(col[i])
        stacks1.append(stack1)
        stacks2.append(stack2)

    for task in tasks.strip().split('\n'):
        for _ in range(int(task.split()[1])):
            stacks1[int(task.split()[5])].put(stacks1[int(task.split()[3])].get())  # part 1
            stacks2[0].put(stacks2[int(task.split()[3])].get())  # part 2
        for _ in range(int(task.split()[1])):
            stacks2[int(task.split()[5])].put(stacks2[0].get())  # part 2
    print(''.join([stack.get() for stack in stacks1 if not stack.empty()]))
    print(''.join([stack.get() for stack in stacks2 if not stack.empty()]))
