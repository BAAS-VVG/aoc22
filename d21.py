def d21():
    print("D21")
    with open('d21.txt') as file:
        text = file.read().strip().splitlines()

    for line in text:
        exec("def " + line.split(': ')[0] + "(): return " + (
            line.split(': ')[1] if line.split(': ')[1].isnumeric() else line.split(': ')[1].split(' ')[0] + "() " +
                                                                        line.split(': ')[1].split(' ')[1] + ' ' +
                                                                        line.split(': ')[1].split(' ')[2] + "()"),
             globals())

    print(int(root()))

    inverse = {'+': '-', '-': '+', '*': '/', '/': '*'}
    target = "humn"
    while target != "root":
        for line in text:
            name, f = line.split(': ')
            if f.isnumeric():
                continue
            f = f.split(' ')

            if target in [f[0], f[2]]:
                exec("def " + target + "(): return " + (
                    '-' if f[2] == target and f[1] == '-' else '1 /' if f[2] == target and f[
                        1] == '/' else '') + (name + "() " + inverse[f[1]] if name != "root" else "") +
                     [x for x in [f[0], f[2]] if x != target][0] + "()", globals())
                target = name

    print(int(humn()))
