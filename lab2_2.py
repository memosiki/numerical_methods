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

def phi1(x1, x2):
    return (math.e ** x2) - 2
    # return math.log(x1-2)

def phi2(x1, x2):
    return x2 + ( x1 ** 2 +x2**2-4 ) /100


def phi1_diff_x1(x1, x2):
    return 0.


def phi1_diff_x2(x1, x2):
    return math.e ** x2


def phi2_diff_x1(x1, x2):
    return - x1 / (4 - x1 ** 2) ** 0.5


def phi2_diff_x2(x1, x2):
    return 0.

# другой вариант системы
def ph1(x1, x2):
    return math.cos(x2) + 2


def ph2(x1, x2):
    return math.sin(x1) + 2


def dph1_dx1(x1, x2):
    return 0


def dph1_dx2(x1, x2):
    return -math.sin(x2)


def dph2_dx1(x1, x2):
    return math.cos(x1)


def dph2_dx2(x1, x2):
    return 0


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


def norm(x, x_prev):
    return max(x[0] - x_prev[0], x[1] - x_prev[1])


def simple_iter_system(x0, phi1, phi2, phi1_diff_x1, phi1_diff_x2, phi2_diff_x1, phi2_diff_x2):
    x1, x2 = x0[0][0], x0[1][0]
    # q = max(
    #     abs(phi1_diff_x1(x1, x2)) + abs(phi1_diff_x2(x1, x2)),
    #     abs(phi2_diff_x1(x1, x2)) + abs(phi2_diff_x2(x1, x2)))
    #
    # if q >= 1:
    #     print("В заданной области не выполняется условие сходимости итерационного процесса")
    #     print('q = ', q)
    #     return mc.zeroes(2, 1), 0

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
bound_a, bound_b = 1.54, 1.26  # начальные значения
x0 = Matrix([[bound_a], [bound_b]])
x, iter_count = newton_system(x0)
print("Найденное значение Методом Ньютона: \n", x)
print("Количество итераций: ", iter_count)
print()

print("Метод простой итерации ")
x, iter_count = simple_iter_system(x0, phi1, phi2, phi1_diff_x1, phi1_diff_x2, phi2_diff_x1, phi2_diff_x2)
print(x,iter_count)
print("Для задачи из следующего варианта")
x, iter_count = simple_iter_system(x0, ph1, ph2, dph1_dx1, dph1_dx2, dph2_dx1, dph2_dx2)
print("Значение х \n", x)
print("Количество итераций: ", iter_count)
