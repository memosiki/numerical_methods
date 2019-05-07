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
    return [([0.] * m).copy() for i in range(n)]


def mul(A, B):
    # произведение двух матриц
    assert len(A[0]) == len(B)
    l = len(A)
    m = len(A[0])
    n = len(B[0])
    C = zeroes(l, n)
    for i in range(l):
        for j in range(n):
            summ = 0
            for r in range(m):
                summ += A[i][r] * B[r][j]
            C[i][j] = summ
    return C


def transpose(A):
    # транспонирование матрицы
    height = len(A)
    width = len(A[0])
    return [[A[row][col] for row in range(0, height)] for col in range(0, width)]


def norm(A):
    # с-норма матрицы
    n = len(A)
    m = len(A[0])
    ret = 0
    for i in range(n):
        summ = 0
        for j in range(m):
            summ += abs(A[i][j])
        ret = max(ret, summ)
    return ret


def norm2(A):
    # 2-норма матрицы
    n = len(A)
    m = len(A[0])
    summ = 0
    for i in range(n):
        for j in range(m):
            summ += A[i][j] ** 2
    return summ ** 0.5
