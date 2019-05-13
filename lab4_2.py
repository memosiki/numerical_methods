import math
from lab4_1 import runge_kutt
from lab1_2 import tridiagonal


def exact(x):
    return x + math.e ** (-2 * (x ** 2))


def f_1(x, y, z):
    return z


def g_1(x, y, z):
    return (-4 * x * z + 4 * y) / (2 * x + 1)
    # return math.e ** x + math.sin(y)


def p(x):
    return 4 * x / (2 * x + 1)
    # return -x


def q(x):
    return -4 / (2 * x + 1)
    # return -1


def f(x):
    return 0.


def shooting(xa, xb, ya, yb, h, f, g):
    n = int(math.ceil((xb - xa) / h) + 1)
    eta = [1, 0.8]  # некоторое значение тангенса угла наклона касательной
    # к решению в точке a из [a,b]

    eps = 0.000001
    F = []
    for et in eta:
        # решаем задачу коши методом Рунге - Кутта
        x, y, z, _ = runge_kutt(xa, ya, et, f, g, h, n)
        F.append(y[-1] - yb)
    k = 2
    while True:
        # вычисляем новую 'эта'
        eta.append(
            eta[k - 1] - (eta[k - 1] - eta[k - 2]) /
            (F[k - 1] - F[k - 2]) * F[k - 1]
        )

        x, y, z, _ = runge_kutt(xa, ya, eta[k], f, g, h, n)
        F.append(y[-1] - yb)
        # проверяем удовлетворение условия
        if abs(F[k]) < eps:
            break
        k += 1
    return x, y, eta, F


def finite_diff(x, za, fb, h, n):
    # составляем СЛАУ с неизвестными y[k]
    last = n - 1  # последний элемент
    a = [0.]
    b = [-1 / h]
    c = [1 / h]
    d = [za]
    for k in range(1, last):
        a += [1 - p(x[k]) * h / 2]
        b += [-2 + (h ** 2) * q(x[k])]
        c += [1 + p(x[k]) * h / 2]
        d += [(h ** 2) * f(x[k])]
    a += [-1 / h]
    b += [2 + 1 / h]
    c += [0.]
    d += [fb]
    # print("Полученная матрица ")
    # print('a ', a)
    # print('b ', b)
    # print('c ', c)
    # print('d ', d)
    y = tridiagonal(a, b, c, d, n)
    return y


def main():
    h = 0.1
    xa, xb = 0, 1
    za = -1
    fb = 3
    n = int(math.ceil((xb - xa) / h) + 1)

    ya, yb = exact(xa), exact(xb)
    # ya, yb = 1,2
    x, y, eta, F = shooting(xa, xb, ya, yb, h, f_1, g_1)
    print("Метод стрельбы")
    print('x       ', end='')
    for elem in x:
        print("{:5.5f}".format(elem), end=' ')
    print()
    print('y       ', end='')
    for elem in y:
        print("{:5.5f}".format(elem), end=' ')
    print()
    print('Погрешн.', end='')
    for i in range(n):
        val = abs(exact(x[i]) - y[i])
        print("{:5.5f}".format(val), end=' ')
    print()
    print("  эта     f".format(xb, yb))
    for i in range(len(eta)):
        print("{:+5.5f} {:5.5f}".format(eta[i], F[i] + yb))
    print()

    print("Конечно-разностный метод")
    x = [xa + i * h for i in range(n)]
    y = finite_diff(x, za, fb, h, n)
    print('x       ', end='')
    for elem in x:
        print("{:5.5f}".format(elem), end=' ')
    print()
    print('y       ', end='')
    for elem in y:
        print("{:5.5f}".format(elem), end=' ')
    print()
    print('Погрешн.', end='')
    for i in range(n):
        val = abs(exact(x[i]) - y[i])
        print("{:5.5f}".format(val), end=' ')
    print()


if __name__ == '__main__':
    main()
# TODO: Сделать в конечно разностном -- вычисление y1 yNвторым приближением
# придётся систему решать np.linalg.solve() или вычитать из первой строки вторую чтобы обнулить один из элементов
 
