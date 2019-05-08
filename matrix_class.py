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

    def __init__(self, A):
        assert isinstance(A, list)
        self.matrix = A

    def __add__(self, other):
        assert isinstance(other, Matrix)
        return Matrix(mt.add(self.matrix, other.matrix))

    def __sub__(self, other):
        assert isinstance(other, Matrix)
        return Matrix(mt.subtract(self.matrix, other.matrix))

    def __mul__(self, other):
        assert isinstance(other, Matrix)
        return Matrix(mt.mul(self.matrix, other.matrix))

    @property
    def __str__(self):
        return mt.format(self.matrix).__str__

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
