import math
from matrix_class import Matrix
import matrix_class as mc
import matrix_transformations as mt


def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1


n = int(input())
eps = float(input())  # точность

A = [[float(elem) for elem in input().split(' ')] for i in range(n)]
A = Matrix(A)


def QR_decomp(A):
    # возвращает R, Q разложение
    v = Matrix(rows=n, cols=1)
    Q = mc.ident_matrix(n)
    Hk = Matrix(rows=n, cols=n)
    Ak = A.copy()
    for k in range(n - 1):

        for i in range(n):
            if i < k:
                v[i][0] = 0
            elif i == k:
                v[i][0] = Ak[i][i] + sign(Ak[i][i]) * \
                          mt.vector_norm(Ak.transpose()[k][i:])
                # евклидова норма столбца
            else:
                v[i][0] = Ak[i][k]

        v_vt = v * v.transpose()
        vt_v = v.transpose() * v
        vt_v = vt_v[0][0]
        coef = 2 / vt_v
        Hk = mc.ident_matrix(n) - (v_vt * coef)
        Ak = Hk * Ak
        Q *= Hk
    R = Ak
    return Q, R


Q, R = QR_decomp(A)
print("QR разложение исходной матрицы.")
print('Q: ', Q)
print('R: ', R)

iter_count = 0
ITER_MAX = 10 ** 3  # максимальное число итераций (предупреждение возможного бесконечного цикла)

Ak = A.copy()
while iter_count < ITER_MAX:
    iter_count += 1
    Q, R = QR_decomp(Ak)
    Ak = R * Q

    # проверка условия завершения
    # корень суммы квадратов поддиагональны элементов < eps
    summ = 0
    for m in range(0, n):
        for l in range(m + 2, n):
            summ += Ak[l][m] ** 2
    if summ ** 0.5 <= eps:
        break
print("Количество итераций: ", iter_count)
print("Полученная матрица А^k\n", Ak)
# TODO: сделать вывод собственных значений
print('Собственные значения:')
j = 0
while j < n:
    # если элемент под диагональю не нулевой -- это комплексная пара
    if j < n - 1 and abs(Ak[j + 1][j]) > 1:
        # собств. значения -- решение уравнения
        # y^2  - y(Ak[jj] + Ak[j+1,j+1]) + Ak[j,j]*Ak[j+1,j+1] - Ak[j,j+1]*Ak[j+1,j]
        # D = b^2 - 4 a c
        b = Ak[j][j] + Ak[j + 1][j + 1]
        c = (Ak[j][j] * Ak[j + 1][j + 1] - Ak[j][j + 1] * Ak[j + 1][j])
        D = b ** 2 - 4 * c
        y1 = (-b + D ** 0.5) / 2
        y2 = (-b - D ** 0.5) / 2
        print(y1)
        print(y2)
        j += 2
    else:
        print(Ak[j][j])
        j += 1
