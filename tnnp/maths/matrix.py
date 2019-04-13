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
