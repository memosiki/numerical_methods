import math
from matrix_class import Matrix
import matrix_class as mc

n = int(input())
eps = float(input())  # точность

A = [[float(elem) for elem in input().split(' ')] for i in range(n)]
A = Matrix(A)
# проверка на то что матрица симметрическая
B = A.transpose()
assert A == B

MAX_ITER = 10 ** 4  # максимальное число итераций (предупреждение возможного бесконечного цикла)

U = mc.eye(n)
iter_count = 0
summ = 0
Ak = A.copy()
while iter_count < MAX_ITER:
    iter_count += 1
    # находим максимальный по модулю недиагональный элемент
    max_elem = abs(Ak[0][1])
    i, j = 0, 1
    for l in range(n):
        for m in range(n):
            if l < m and max_elem < abs(Ak[l][m]):  #
                max_elem = abs(Ak[l][m])
                i, j = l, m

    # угол вращения
    if Ak[i][i] == Ak[j][j]:
        phi = math.pi / 4
    else:
        phi = 0.5 * math.atan(2 * Ak[i][j] / (Ak[i][i] - Ak[j][j]))
    Uk = mc.eye(n)
    Uk[i][i] = Uk[j][j] = math.cos(phi)
    Uk[j][i] = math.sin(phi)
    Uk[i][j] = -math.sin(phi)
    # новое А
    Ak = Uk.transpose() * Ak * Uk
    # сохраняем произведение U
    U *= Uk

    # проверка условия завершения
    # корень суммы квадратов поддиагональны элементов < eps
    summ = 0
    for l in range(n):
        for m in range(n):
            if l < m:
                summ += Ak[l][m] ** 2
    if summ ** 0.5 < eps:
        break

print("Количество итераций :", iter_count)
print("Точность последней итерации: ", summ ** 0.5)
print("Найденная матрица U:\n", U)
print("Собственные значения: ")
for i in range(n):
    print(Ak[i][i], end=' ')
print()
print("Собственные векторы: ")
for i in range(n):
    print(U.transpose()[i])
