from tnnp.maths.matrix import Matrix, multiply

m = Matrix(3, 2)
if not m.matrix == [[0, 0], [0, 0], [0, 0]]:
    raise Exception("Initialization failed!", m.matrix)


m.add(5)
if not m.matrix == [[5, 5], [5, 5], [5, 5]]:
    raise Exception(".add function not working with number", m.matrix)

m.multiply(3)
if not m.matrix == [[15, 15], [15, 15], [15, 15]]:
    raise Exception(".multiply function not working", m.matrix)


n = Matrix(3, 2)
n.randomize()
if n.matrix == [[0, 0], [0, 0], [0, 0]]:
    raise Exception(".randomize function not working", n.matrix)

n.matrix = [[1 for col in range(len(n.matrix[row]))]
            for row in range(len(n.matrix))]
n.add(m)
if not n.matrix == [[16, 16], [16, 16], [16, 16]]:
    raise Exception(".add function not working with matrix", n.matrix)

a = Matrix(2, 3)
a.matrix = [[7, 7, 8], [5, 9, 4]]
b = Matrix(3, 2)
b.matrix = [[21, 19], [17, 18], [18, 23]]
c = multiply(a, b)
if not c.matrix == [[410, 443], [330, 349]]:
    raise Exception("multiply function not working", c.matrix)

print("No errors were found!")
