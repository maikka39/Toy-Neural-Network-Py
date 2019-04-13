from random import randint


class Matrix(object):
    """Matrix object."""

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.matrix = [[0 for col in range(self.cols)]
                       for row in range(self.rows)]

    def multiply(self, n):
        """Multiply all values in the matrix by a number."""
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

    def randomize(self, smallest=1, biggest=10):
        """Randomize all values in the matrix."""
        self.matrix = [[randint(smallest, biggest) for value in self.matrix[row]]
                       for row in range(len(self.matrix))]


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
