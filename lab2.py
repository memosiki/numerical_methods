import numpy as np

B = [8, 4, 5, -7]
C = [15, -15, 11, 16, 8]  # главная диагональ
A = [2, 4, -3, 3]

F = [92, -84, -77, 15, -11]

n = 5
alpha = [0.] * n
beta = [0.] * n

alpha[1] = -B[0] / C[0]
beta[1] = F[0] / C[0]

for i in range(2, n-1):
    alpha[i+1] = -B[i]/(A[i]*alpha[i] + C[i])
    beta[i+1] = (F[i] - A[i]*beta[i])/(A[i]*alpha[i] + C[i])

