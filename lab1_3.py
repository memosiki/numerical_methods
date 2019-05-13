from math import log

import matrix_transformations as mt

n = int(input())
eps = float(input())  # точность
A = [[float(elem) for elem in input().split(' ')] for i in range(n)]
b = [[float(elem) for elem in input().split(' ')]]
# если на диагонали стоят нулевые элементы следует поменять эту строку с другой
b = mt.transpose(b)  # столбец из строки


MAX_ITER = 10**5  # максимальное число итераций (предупреждение возможного бесконечного цикла)


def seidel(A, b, eps):
    beta = mt.zeroes(n, 1)
    for i in range(n):
        beta[i][0] = b[i][0] / A[i][i]
    # print("Столбец бета:\n", mt.format(beta))
    alpha = mt.zeroes(n, n)  # пустая матрица
    for i in range(n):
        for j in range(n):
            if i != j:
                alpha[i][j] = -A[i][j] / A[i][i]
    # print("Матрица альфа:\n", mt.format(alpha))
    iter = 0
    norm = mt.norm(alpha)

    x = mt.copy(beta)
    while iter < MAX_ITER:
        x_prev = mt.copy(x)
        for i in range(n):
            summ = beta[i][0]
            for j in range(0, i):
                summ += alpha[i][j] * x[j][0]
            for j in range(i, n):
                summ += alpha[i][j] * x_prev[j][0]
            x[i][0] = summ
        iter += 1
        # проверка условия завершения
        if norm / (1 - norm) * mt.norm2(mt.subtract(x, x_prev)) < eps:
            break

    print("Метод Зейделя выполнялся {} итераций".format(iter))
    return x


def simple_iter(A, b, eps):
    beta = mt.zeroes(n, 1)
    for i in range(n):
        beta[i][0] = b[i][0] / A[i][i]
    print("Столбец бета:\n", mt.format(beta))

    alpha = mt.zeroes(n, n)  # пустая матрица
    for i in range(n):
        for j in range(n):
            if i != j:
                alpha[i][j] = -A[i][j] / A[i][i]
    print("Матрица альфа:\n", mt.format(alpha))

    iter = 0
    norm = mt.norm(alpha)

    pred = (log(eps) - log(mt.norm2(beta)) + log(1 - norm)) / log(norm)
    print("Верхняя оценка количества итераций: ", pred)

    x = mt.copy(beta)
    x_prev = mt.zeroes(1, n)
    while iter < MAX_ITER:
        x_prev = mt.copy(x)
        x = mt.add(beta, mt.mul(alpha, x_prev))
        iter += 1
        # проверка условия завершения
        if norm / (1 - norm) * mt.norm2(mt.subtract(x, x_prev)) < eps:
            break

    print("Метод простых итераций выполнялся {} итераций".format(iter))
    return x


# получаем вектор решений
x = simple_iter(A, b, eps)
x_sied = seidel(A, b, eps)
print("Значения х методом простых итераций:\n", mt.format(x))

print("Значения х методом Зейделя:\n", mt.format(x_sied))
