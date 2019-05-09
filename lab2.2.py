import math
from matrix_class import Matrix
import matrix_class as mc

param_a = 2


# функции
def f1(x1, x2):
    return x1 ** 2 + x2 ** 2 - param_a ** 2


def f2(x1, x2):
    return x1 - math.e ** x2 + param_a


def f1_diff_x1(x1, x2):
    return 2 * x1


def f1_diff_x2(x1, x2):
    return 2 * x2


def f2_diff_x1(x1, x2):
    return 1


def f2_diff_x2(x1, x2):
    return - math.e ** x2


eps = float(input())

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

bound_a, bound_b = -1, -1  # начальные значения
x = Matrix([[bound_a], [bound_b]])

while True:
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

print("Найденное значение: \n", x)
