def find_marker(text, length):
    return next(i for i in range(length, len(text) + 1) if len(set(text[i - length: i])) > length - 1)


def d6():
    print("D6")
    with open('d6.txt') as f:
        text = f.read()
    print(find_marker(text, 4))
    print(find_marker(text, 14))
