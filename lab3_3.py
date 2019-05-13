import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def n_degree_polynom(x, y, n):
    N = len(x)
    max_pow = 0
    for _ in range(n):
        max_pow += 2

    xpow = [N] + [0 for _ in range(max_pow)]

    b = [0 for _ in range(n + 1)]

    for i in range(N):
        for k in range(1, len(xpow)):
            xpow[k] += x[i] ** (k)
        for k in range(len(b)):
            b[k] += y[i] * (x[i] ** k)

    shift = 0
    system = []
    for _ in range(n + 1):
        system.append([xpow[i + shift] for i in range(n + 1)])
        shift += 1

    a = np.linalg.solve(system, b)

    def f(x):
        return a[0] + sum(a[i] * (x ** i) for i in range(1, len(a)))

    return a, f


def sum_square_error(x, y, f):
    return sum(
        (f(x[i]) - y[i]) ** 2 for i in range(len(x)))


def func_printer(x, f):
    n = len(x)

    def print_line(x):
        for i in range(n):
            print("{:7.4f}".format(x[i]), end=" | ")
        print()

    print_line(x)
    print_line([f(x[i]) for i in range(n)])


def show_plot(f, x, y, step=0.1):
    X = np.arange(x[0], x[-1], step)
    Y = []
    for i in range(len(f)):
        Y.append([f[i](val) for val in X])

    fig, ax = plt.subplots()
    for i in range(len(Y)):
        ax.plot(X, Y[i], label=f'degree={i}')

    ax.plot(x, y, label='original')
    ax.legend(loc='upper right')

    ax.grid()

    plt.show()


def main():
    x = [float(num) for num in input().split(' ')]
    y = [float(num) for num in input().split(' ')]
    f = []
    for degree in [1, 2, 3, 4, 5, 6]:
        print(f"degree {degree}")
        a, ft = n_degree_polynom(x, y, degree)
        f.append(ft)
        func_printer(x, ft)
        print("sum square error: {:f}\n"
              .format(sum_square_error(x, y, ft)))
    show_plot(f, x, y)


if __name__ == '__main__':
    main()
