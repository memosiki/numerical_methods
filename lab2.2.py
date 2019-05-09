import math
from matrix_class import Matrix
import matrix_class as mc


# функции
def f1(x1, x2):
    return x1 ** 2 + x2 ** 2 - 4


def f2(x1, x2):
    return x1 - math.e ** x2 + 2


def f1_diff_x1(x1, x2):
    return 2 * x1


def f1_diff_x2(x1, x2):
    return 2 * x2


def f2_diff_x1(x1, x2):
    return 1


def f2_diff_x2(x1, x2):
    return - math.e ** x2


# чтобы было удобнее выражать x1 и x2
# поменяет равенства местами в исходной системе
def phi2(x1, x2):
    return (4 - x1 ** 2)**0.5


def phi1(x1, x2):
    return (math.e ** x2) - 2


def newton_system(x0):
    x = x0.copy()
    # матрица функций
    F = Matrix([
        [f1],
        [f2],
    ])
    # Матрица Якоби из функций
    J = Matrix([
        [f1_diff_x1, f1_diff_x2],
        [f2_diff_x1, f2_diff_x2],
    ])

    iter_count = 0
    while True:
        iter_count += 1
        x_prev = x.copy()

        # делаем список аргмуентов ф-ии из столбца значений x
        args = x.transpose()[0]  # [x1, x2]

        # Найдем обратную матрицу
        [[a, b],
         [c, d]] = J(*args).matrix
        J_inv = Matrix([
            [d, -b],
            [-c, a],
        ])
        J_inv = J_inv * (1 / (a * d - b * c))

        x = x - J_inv * F(*args)
        # условие завершения
        if mc.norm2(x_prev - x) < eps:
            break
    return x, iter_count


def simple_iter_system(x0):
    # Матрица функций
    phi = Matrix([
        [phi1],
        [phi2]
    ])
    x = x0.copy()
    iter_count = 0
    while True:
        iter_count += 1
        x_prev = x
        args = x.transpose()[0]  # [x1, x2]

        x = phi(*args)

        if mc.norm2(x - x_prev) < eps:
            break

    return x, iter_count


eps = float(input())
bound_a, bound_b = 1, 1  # начальные значения
x0 = Matrix([[bound_a], [bound_b]])
x, iter_count = newton_system(x0)
print("Найденное значение Методом Ньютона: \n", x)
print("Количество итераций: ", iter_count)
print()
x, iter_count = simple_iter_system(x0)
print("Метод простой итераций", x)
print("Количество итераций: ", iter_count)
