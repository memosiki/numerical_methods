import sys
import numpy as np


class SparseMatrix:
    # инициализирует нулевую квадратную матрицу размером n на n
    def __init__(self, n):
        self.rows = [SparseRow() for i in range(n)]

    def __getitem__(self, key):
        return self.rows[key]


class SparseRow(dict):
    # Обёртка на стандартным словарём
    # Словарь работает на основе хэш-таблицы, поэтому проверка принадлежности ключа и оступ к элементу О(1)

    # Обращение к элементу -- вызов get со стандартным значением
    def __getitem__(self, key):
        return dict.get(self, key, 0.)


def scalar_product(a, b):
    ret = 0
    for elem_a, elem_b in zip(a, b):
        ret += elem_a * elem_b
    return ret


def add(v1, v2):
    return [elem1 + elem2 for elem1, elem2 in zip(v1, v2)]


def sub(v1, v2):
    return [elem1 - elem2 for elem1, elem2 in zip(v1, v2)]


def mul(A, v):
    if isinstance(A, (SparseMatrix, list)):
        # умножение матрицы на вектор
        n = len(v)
        ret = []
        for i in range(n):
            sum_line = 0
            for j in range(n):
                sum_line += A[i][j] * v[j]
            ret.append(sum_line)
        return ret
    elif isinstance(A, (int, float, complex)):
        # умножение числа на вектор
        return [A * elem for elem in v]
    return None


def conjugate_gradient(A, b, eps=0.01):
    n = len(b)
    max_iter = 10 ** 4

    # проверка на симметричность
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                raise TypeError('Матрица не симметрична')

    b_product = scalar_product(b, b)
    # начальное приближение
    x = [0.2] * n
    #  Задаем начальное значение r и z.
    # r = b - A * x      r - градиент
    r = sub(b, mul(A, x))
    # z = r
    z = r.copy()
    iter_count = 0
    while True:
        iter_count += 1
        # alpha = (r,r)/(A*z,z) скалярный шаг -- смещение по заданному направлению
        alpha = scalar_product(r, r) / scalar_product(mul(A, z), z)
        # новое приближение: x = x + alpha * z
        x = add(x, mul(alpha, z))
        # градиент: r = r - alpha * A * z
        r_prev = r
        r = sub(r, mul(alpha, mul(A, z)))
        # коэфф бета для нового вектора спуска
        beta = scalar_product(r, r) / scalar_product(r_prev, r_prev)
        # вектор спуска  z = r+ beta * z-1
        z = add(r, mul(beta, z))
        # Поскольку минимизируемый функционал квадратичный, то процесс должен дать ответ на n-й итерации,
        # однако при реализации метода на компьютере существует погрешность представления вещественных чисел,
        # в результате чего может потребоваться и больше итераций
        if scalar_product(r, r) / b_product < eps \
                or iter_count > max_iter:
            break
    return x


def main(from_stdin=True):
    if not from_stdin:
        A = [[1, 0, 0],
             [0, 2, 0],
             [0, 0, 3]]
        A1 = A
        b = [1, 2, 3]
    else:
        n = int(input())
        A1 = np.zeros((n, n))
        A = SparseMatrix(n)
        for line in sys.stdin:
            [i, j, val] = line.split()
            if i == '-1':
                break
            i, j, val = int(i), int(j), float(val)
            A[i][j] = val
            A1[i][j] = val
        b = []
        for line in sys.stdin:
            b.append(float(line))
    try:
        x = conjugate_gradient(A, b)
    except ZeroDivisionError:
        print("Заданная система не совместна")
    else:
        print("Решение методом сопряжённых градиентов")
        # print(x)
        # print("Решение с помощью numpy:")
        # x = np.linalg.solve(A1, np.transpose([b]))
        # print(np.transpose(x))


if __name__ == '__main__':
    main()
