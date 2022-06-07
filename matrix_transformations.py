import numpy as np


def add(A, B):
    # сумма двух матриц
    assert len(A) == len(B)
    assert len(A[0]) == len(B[0])

    n = len(A)
    m = len(A[0])

    C = zeroes(n, m)

    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    # разность двух матриц
    assert len(A) == len(B)
    assert len(A[0]) == len(B[0])

    n = len(A)
    m = len(A[0])

    C = zeroes(n, m)

    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] - B[i][j]
    return C


def zeroes(n):
    # список длинной n, заполенный нулями
    return [0.] * n


def zeroes(n, m):
    # нулевая матрица n*m
    return [([0.] * m).copy() for _ in range(n)]


def ident_matrix(n):
    # возвращает квадратную единичную матрицу
    A = zeroes(n, n)
    for i in range(n):
        A[i][i] = 1
    return A


def mul(A, B):
    # произведение двух матриц
    assert len(A[0]) == len(B)
    l = len(A)
    m = len(A[0])
    n = len(B[0])
    C = zeroes(l, n)
    for i in range(l):
        for j in range(n):
            summ = sum(A[i][r] * B[r][j] for r in range(m))
            C[i][j] = summ
    return C


def transpose(A):
    # транспонирование матрицы
    height = len(A)
    width = len(A[0])
    return [[A[row][col] for row in range(height)] for col in range(width)]


def norm(A):
    # с-норма матрицы
    # сумма элементов максимальной строки
    n = len(A)
    m = len(A[0])
    ret = 0
    for i in range(n):
        summ = sum(abs(A[i][j]) for j in range(m))
        ret = max(ret, summ)
    return ret


def norm1(A):
    # норма матрицы
    # сумма элементов максимального столбца
    n = len(A)
    m = len(A[0])
    ret = 0
    for i in range(m):
        summ = sum(abs(A[j][i]) for j in range(n))
        ret = max(ret, summ)
    return ret


def norm2(A):
    # евклидова норма матрицы
    # (2 - норма
    n = len(A)
    m = len(A[0])
    summ = 0
    for i in range(n):
        for j in range(m):
            summ += A[i][j] ** 2
    return summ ** 0.5


def vector_norm(v):
    # возвращает евклидову норму вектора
    summ = sum(elem ** 2 for elem in v)
    return summ ** 0.5


def format(A):
    # форматированный "красивый" вывод матрицы
    return np.array(A)


def copy(A):
    # возвращает копию матрицы
    return [x.copy() for x in A]
