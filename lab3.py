from math import log

import matrix_transformations as mt

A = [
    [29, 8, 9, -9],
    [-7, -25, 0, 9],
    [1, 6, 16, -2],
    [-7, 4, -2, 17]
]
# если на диагонали стоят нулевые элементы следует поменять эту строку с другой

b = [[197, -226, -95, -58]]
n = 4
eps = 0.0001  # точность

# столбец из строки
b = mt.transpose(b)


def simple_iter(A, b, eps):
    beta = mt.zeroes(n, 1)
    for i in range(n):
        beta[i][0] = b[i][0] / A[i][i]

    # пустая матрица

    alpha = mt.zeroes(n, n)

    for i in range(n):
        for j in range(n):
            if i != j:
                alpha[i][j] = -A[i][j] / A[i][i]

    iter = 0
    norm = mt.norm(alpha)

    pred = (log(eps) - log(mt.norm2(beta)) + log(1 - norm)) / log(norm)
    print("Верхняя оценка количества итераций: ", pred)

    x = beta
    x_prev = mt.zeroes(1, n)
    while iter < 10000:
        x_prev = x
        x = mt.add(beta, mt.mul(alpha, x_prev))
        iter += 1
        # проверка условия завершения
        if norm / (1 - norm) * mt.norm2(mt.subtract(x, x_prev)) < eps:
            break

    print("Получено за {} итераций".format(iter))
    return x


# получаем вектор решений
x = simple_iter(A, b, eps)
# преобразуем вектор в список
x = mt.transpose(x)[0]
print("Значения х методом простых итераций:\n", x)
