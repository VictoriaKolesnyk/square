def square(a):
    p = 4 * a
    s = a ** 2
    diag = a * 4 ** (1 / 2)
    k = (p, s, diag)

    print(k)


a = int(input('введите число  '))
square(a)