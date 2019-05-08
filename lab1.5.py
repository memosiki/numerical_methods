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
    Q = mc.eye(n)
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
        Hk = mc.eye(n) - (v_vt * coef)
        Ak = Hk * Ak
        Q *= Hk
    R = Ak
    return Q, R


Q, R = QR_decomp(A)
print(Q)
print(R)
