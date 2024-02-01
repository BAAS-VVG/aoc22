def make_list(it):
    res = []
    while True:
        char = next(it)
        if char == ']':
            break
        if char == '[':
            res.append(make_list(it))
        elif char.isnumeric():
            res.append(int(char))
        elif char == 'a':
            res.append(10)
    return res


def convert_lists(left, right):
    for idx in range(min(len(left), len(right))):
        if type(left[idx]) is int and type(right[idx]) is int:
            continue
        if type(right[idx]) is int:
            right[idx] = [right[idx]]
        if type(left[idx]) is int:
            left[idx] = [left[idx]]

        convert_lists(left[idx], right[idx])


def compare_lists(left, right):
    for idx in range(min(len(left), len(right))):
        if type(left[idx]) is int and type(right[idx]) is int:
            if left[idx] < right[idx]:
                return 1
            elif right[idx] < left[idx]:
                return -1
            continue
        if type(right[idx]) is int:
            res = compare_lists(left[idx], [right[idx]])
        elif type(left[idx]) is int:
            res = compare_lists([left[idx]], right[idx])
        else:
            res = compare_lists(left[idx], right[idx])
        if res != 0:
            return res

    if len(left) < len(right):
        return 1
    if len(right) < len(left):
        return -1
    return 0


def d13():
    print("D13")
    with open('d13.txt') as f:
        text = f.read()

    text = text.replace("10", "a")
    res = []
    lines = [[[2]], [[6]]]
    for idx, pair in enumerate(text.split('\n\n')):
        left = make_list(iter(pair.split('\n')[0][1:]))
        right = make_list(iter(pair.split('\n')[1][1:]))

        convert_lists(left, right)
        lines.append(left)
        lines.append(right)
        original = [left, right]
        check = sorted(original)
        if original == check:
            res.append(idx + 1)

    print(sum(res))

    for idx1 in range(len(lines) - 1):
        for idx2 in range(idx1, len(lines)):
            if compare_lists(lines[idx1], lines[idx2]) < 0:
                dummy = lines[idx1]
                lines[idx1] = lines[idx2]
                lines[idx2] = dummy

    print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
