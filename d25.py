import functools


def d25():
    print("D25")

    print((lambda f, n: f(f, n))(lambda f, n: f(f, (n + 2) // 5) + '=-012'[(n + 2) % 5] if n else '', sum(map(
        functools.partial((lambda f, n: f(f, n)), lambda f, n: f(f, n[:-1]) * 5 + '=-012'.find(n[-1]) - 2 if n else 0),
        open('d25.txt').read().split()))))
