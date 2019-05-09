import math


def f(x):
    return 2 ** x + x ** 2 - 2


def f_diff(x):
    return math.log(2) * 2 ** x + 2 * x


def phi(x):
    # return 1 - math.log(x ** 2, 2)
    return (2 - 2 ** x) ** 0.5


a, b = 0.0001, 3
eps = float(input())


def newton(x0):
    x_prev = x0
    x = x0
    x = x - f(x) / f_diff(x)
    iter_count = 0
    while abs(x_prev - x) > eps:
        x_prev = x
        x = x - f(x) / f_diff(x)
        iter_count += 1
    return x, iter_count


def simple_iter(x0):
    x_prev = x0
    x = phi(x0)
    iter_count = 0
    while abs(x_prev - x) > eps:
        x_prev = x
        x = phi(x)
        iter_count += 1
    return x, iter_count


print("Корень на отрезке ({} ; {})".format(a, b))
print()
x, iter_count = newton(a)
print("Метод Ньютона", x)
print("Количество итераций: ", iter_count)
print()
x, iter_count = simple_iter(a)
print("Метод простых итераций", x)
print("Количество итераций: ", iter_count)
