import numpy as np

def find_x(l, u, b):
    L, U = l, u
    # список нулей
    z = [0] * n

    # находим значения z
    # Lz = b
    for i in range(n):
        z_sum = 0
        for j in range(i):
            z_sum += L[i][j] * z[j]
        z[i] = b[i] - z_sum

    x = [0] * n
    # находим x
    # Ux = z
    for i in range(n - 1, -1, -1):
        x[i] = z[i]
        x_sum = 0
        for j in range(i + 1, n):
            x_sum += U[i][j] * x[j]
        x[i] -= x_sum
        x[i] /= U[i][i]
    return x


A = [
    [1, -5, -7, 1],
    [1, -3, -9, -4],
    [-2, 4, 2, 1],
    [-9, 9, 5, 3],
]
b = [
    -75,
    -41,
    18,
    29,
]
n = 4

# приводим значения к типу float
A = [[float(x) for x in line] for line in A]

# копируем матрицу, чтобы не изменять входную
U = [x.copy() for x in A]

# единичная матрица
L = [[0.] * n for x in range(n)]
for k in range(n):
    L[k][k] = 1

for k in range(0, n - 1):
    # находим максимальный элемент в столбце ниже k и меняем эту строку с k-той
    max_elem = U[k][k]
    max_row = k
    for j in range(k + 1, n):
        if max_elem < U[j][k]:
            max_elem = U[j][k]
            max_row = j
    # меняем местами строки
    U[k], U[max_row] = U[max_row], U[k]
    for i in range(k + 1, n):
        mu = U[i][k] / U[k][k]
        L[i][k] = mu
        for j in range(k, n):
            U[i][j] -= mu * U[k][j]

x = find_x(L, U, b)
# вычисляем определитель
det = 1
for k in range(n):
    det *= U[k][k]

# вычисляем обратную матрицу
# ищем значения х(столбца неизвестных) для каждого из столбцов единичной матрицы

e = [0] * n
# нулевая матрица
A_inv = [[0.] * n for x in range(n)]
for k in range(n):
    e[k] = 1
    a_inv_col = find_x(L, U, e)
    for i in range(n):
        A_inv[i][k] = a_inv_col[i]
    e[k] = 0

# print(np.linalg.inv(A))
print("Значения х:", x)
print("Определитель: ", det)
# форматированный вывод матриц
A_inv = np.array(A_inv)
print("Обратная матрица:\n", A_inv)
print()
print("Произведение A на x:\n", np.matmul(A, x))
print("Произведение A на A^-1:\n", np.matmul(A, A_inv))
