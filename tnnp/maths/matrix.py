from random import random


class Matrix(object):
    """Matrix object."""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.matrix = [[0 for col in range(self.cols)]
                       for row in range(self.rows)]

    def fill(self, n):
        """Set all values to a number."""
        self.matrix = [[n for value in self.matrix[row]]
                       for row in range(len(self.matrix))]

    def multiply(self, n):
        """Multiply all values in the matrix by a number."""
        if isinstance(n, Matrix):
            self.matrix = multiply(self, n).matrix
            return

        self.matrix = [[value * n for value in self.matrix[row]]
                       for row in range(len(self.matrix))]

    def add(self, n):
        """Add a number or matrix to all values in the matrix."""
        if isinstance(n, Matrix):
            self.matrix = [[value + n.matrix[row][column] for column, value in enumerate(self.matrix[row])]
                           for row in range(len(self.matrix))]
            return

        self.matrix = [[value + n for value in self.matrix[row]]
                       for row in range(len(self.matrix))]

    def substract(self, n):
        """Substract a number or matrix from all values in the matrix."""
        if isinstance(n, Matrix):
            self.matrix = [[value - n.matrix[row][column] for column, value in enumerate(self.matrix[row])]
                           for row in range(len(self.matrix))]
            return

        self.matrix = [[value - n for value in self.matrix[row]]
                       for row in range(len(self.matrix))]

    def randomize(self, smallest=1, biggest=10):
        """Randomize all values in the matrix."""
        self.matrix = [[random() * 2 - 1 for value in self.matrix[row]]
                       for row in range(len(self.matrix))]

    def map(self, fn):
        """Run a function over every value in the matrix."""
        self.matrix = [[fn(value) for value in self.matrix[row]]
                       for row in range(len(self.matrix))]

    def to_array(self):
        """Convert a matrix to an array"""
        arr = []

        for row in range(len(self.matrix)):
            for value in self.matrix[row]:
                arr.append(value)

        return arr


def multiply(a, b):
    """Matrix product of two matrices."""
    if a.cols != b.rows:
        raise Exception(
            "Amount of rows of b must match amount of columns of a")

    result = Matrix(a.rows, b.cols)

    for i in range(result.rows):
        for j in range(result.cols):
            sum = 0
            for k in range(a.cols):
                sum += a.matrix[i][k] * b.matrix[k][j]
            result.matrix[i][j] = sum

    return result


def transpose(m):
    """Transpose a matrix."""
    result = Matrix(m.cols, m.rows)

    for i in range(result.rows):
        for j in range(result.cols):
            result.matrix[i][j] = m.matrix[j][i]

    return result


def from_array(arr):
    """Create a matrix from an array"""
    m = Matrix(len(arr), 1)

    m.matrix = [[arr[row] for index in m.matrix[row]]
                for row in range(len(m.matrix))]

    return m


def add(m1, m2):
    """Add a matrix to a matrix."""
    output = Matrix(m1.rows, m1.cols)
    output.matrix = [[value + m2.matrix[row][column] for column, value in enumerate(m1.matrix[row])]
                     for row in range(len(m1.matrix))]
    return output


def substract(m1, m2):
    """Substract a matrix from a matrix."""
    output = Matrix(m1.rows, m1.cols)
    output.matrix = [[value - m2.matrix[row][column] for column, value in enumerate(m1.matrix[row])]
                     for row in range(len(m1.matrix))]
    return output


def map(m, fn):
    """Run a function over every value in the matrix."""
    output = Matrix(m.rows, m.cols)
    output.matrix = [[fn(value) for value in m.matrix[row]]
                     for row in range(len(m.matrix))]
    return output
