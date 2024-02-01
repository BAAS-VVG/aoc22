from anytree import Node, PostOrderIter


def d7():
    print("D7")
    with open('d7.txt') as f:
        text = f.read().strip()
    root = Node("root", size=0)
    for line in text.split('\n'):
        line = line.split(' ')
        if line[0] != '$':
            if not next((c for c in node.children if c.name == line[1]), None):
                Node(line[1], parent=node, size=0 if line[0] == "dir" else int(line[0]))
        elif line[1] == 'cd':
            if line[2] == '/':
                node = root
            elif line[2] == '..':
                node = node.parent
            else:
                node = next(c for c in node.children if c.name == line[2])

    for node in [node for node in PostOrderIter(root) if not node.is_leaf]:
        node.size = sum([c.size for c in node.children])

    print(sum([node.size for node in PostOrderIter(root) if not node.is_leaf and node.size <= 100000]))
    print(min([node.size for node in PostOrderIter(root) if
               not node.is_leaf and node.size >= 30000000 + root.size - 70000000]))
