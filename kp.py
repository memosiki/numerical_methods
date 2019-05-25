import sys


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
    max_iter = 10 ** 6

    # проверка на симметричность
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                raise TypeError('Матрица не симметрична')

    b_product = scalar_product(b, b)
    # начальное приближение
    x = [0.2] * n
    #  Задаем начальное значение r и z.
    # r = b - A * x
    r = sub(b, mul(A, x))
    # z = r
    z = r.copy()
    iter_count = 0
    while True:
        iter_count += 1
        # alpha = (r,r)/(A*z,z)
        alpha = scalar_product(r, r) / scalar_product(mul(A, z), z)
        # новое приближение: x = x + alpha * z
        x = add(x, mul(alpha, z))
        # вектор невязки: r = r - alpha * A * z
        r_prev = r
        r = sub(r, mul(alpha, mul(A, z)))
        # коэфф бета
        beta = scalar_product(r, r) / scalar_product(r_prev, r_prev)
        # вектор спуска: z = r+ beta * z-1
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
        A = [[4, 1],
             [1, 3]]

        b = [1, 2]
    else:
        A = SparseMatrix(10)
        for line in sys.stdin:
            [i, j, val] = line.split()
            i, j, val = int(i), int(j), float(val)
            A[i][j] = val
        b = [1, 1]
    try:
        x = conjugate_gradient(A, b)
    except ZeroDivisionError:
        print("Заданная система не совместна")
    else:
        print(x)


if __name__ == '__main__':
    main(False)
