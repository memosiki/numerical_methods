import matrix_transformations as mt


###########
# методы

def eye(n):
    return Matrix(mt.eye(n))


def zeroes(n, m):
    return Matrix(mt.zeroes(n, m))


##########
# классы
class Matrix(object):
    """docstring for Matrix"""
    matrix = [[0]]

    def __init__(self, matrix: list = None, rows: int = 0, cols: int = 0):
        # создать матрицу из 2д списка
        # создать нулевую матрицу размера n*m

        if matrix is None:
            assert isinstance(rows, int)
            assert isinstance(cols, int)
            self.matrix = mt.zeroes(rows, cols)
        else:
            assert isinstance(matrix, list)
            self.matrix = matrix

    def __add__(self, other):
        assert isinstance(other, Matrix)
        return Matrix(mt.add(self.matrix, other.matrix))

    def __sub__(self, other):
        assert isinstance(other, Matrix)
        return Matrix(mt.subtract(self.matrix, other.matrix))

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # умножение матриц
            return Matrix(mt.mul(self.matrix, other.matrix))
        else:
            # умножение матрицы на число
            assert isinstance(other, (float, int))
            n = len(self.matrix)
            m = len(self.matrix[0])
            A = zeroes(n, m)
            for i in range(n):
                for j in range(m):
                    A[i][j] = self.matrix[i][j] * other
            return A

    def __str__(self):
        return str(mt.format(self.matrix))

    def __getitem__(self, key):
        return self.matrix[key]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.matrix == other.matrix

    def copy(self):
        return Matrix(mt.copy(self.matrix))

    def transpose(self):
        return Matrix(mt.transpose(self.matrix))
