def runge_romberg(h1, h2, y1, y2):
    return abs((y1 - y2) / ((h2 / h1) ** 2 - 1.0))


def f(x):
    return 1 / (3 * (x ** 2) + 4 * x + 2)


def arange(x0, xk, step=0.1):
    x = x0
    r = []
    while x <= xk:
        r.append(x)
        x += step
    return r


def rectangle(h, x, f):
    return h * sum(
        f((x[i - 1] + x[i]) / 2) for i in range(1, len(x)))


def trapezium(h, x, f):
    return h * (
            f(x[0]) / 2 + sum(
        f(x[i]) for i in range(1, len(x) - 1)) + f(x[len(x) - 1]))


def simpson(h, x, f):
    # https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0_%D0%A1%D0%B8%D0%BC%D0%BF%D1%81%D0%BE%D0%BD%D0%B0
    n = len(x)
    return (h / 3) * (f(x[0]) +
                      sum(4 * f(x[i]) for i in range(1, n - 1, 2)) +
                      sum(2 * f(x[i]) for i in range(2, n - 1, 2)) +
                      f(x[n - 1]))


def main():
    x0 = float(input())
    xk = float(input())
    h1 = float(input())
    h2 = float(input())

    val = 1.85742  # точное значение
    # https://www.wolframalpha.com/input/?i=int+1+%2F+(3+*+(x+**+2)+%2B+4+*+x+%2B+2)+from+-2+to+2

    x_h1 = arange(x0, xk, h1)
    x_h2 = arange(x0, xk, h2)
    print("Метод прямоугольников")
    first = rectangle(h1, x_h1, f)
    second = rectangle(h2, x_h2, f)
    print("для h1:", first)
    print("для h2:", second)
    print("Погрешность:")
    print("Рунге-Ромберга        ", runge_romberg(h1, h2, first, second))
    print("Разница с точным реш. ", abs(first - val))
    print()

    x_h1 = arange(x0, xk, h1)
    x_h2 = arange(x0, xk, h2)
    print("Метод трапеций")
    first = trapezium(h1, x_h1, f)
    second = trapezium(h2, x_h2, f)
    print("для h1:", first)
    print("для h2:", second)
    print("Погрешность:")
    print("Рунге-Ромберга        ", runge_romberg(h1, h2, first, second))
    print("Разница с точным реш. ", abs(first - val))
    print()

    x_h1 = arange(x0, xk, h1)
    x_h2 = arange(x0, xk, h2)
    print("Метод Симпсона")
    first = simpson(h1, x_h1, f)
    second = simpson(h2, x_h2, f)
    print("для h1:", first)
    print("для h2:", second)
    print("Погрешность:")
    print("Рунге-Ромберга        ", runge_romberg(h1, h2, first, second))
    print("Разница с точным реш. ", abs(first - val))
    print()


if __name__ == '__main__':
    main()
