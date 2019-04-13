from tnnp.maths.matrix import Matrix, multiply, transpose

m = Matrix(3, 2)
if not m.matrix == [[0, 0], [0, 0], [0, 0]]:
    raise Exception("Initialization failed!", m.matrix)

m.add(5)
if not m.matrix == [[5, 5], [5, 5], [5, 5]]:
    raise Exception(".add function not working with number", m.matrix)

m.multiply(3)
if not m.matrix == [[15, 15], [15, 15], [15, 15]]:
    raise Exception(".multiply function not working", m.matrix)

m.fill(1)
if not m.matrix == [[1, 1], [1, 1], [1, 1]]:
    raise Exception(".fill function not working", m.matrix)

m.randomize()
if m.matrix == [[1, 1], [1, 1], [1, 1]]:
    raise Exception(".randomize function not working", m.matrix)

m.fill(1)
m.map(lambda a: a * 2 + 1)
if not m.matrix == [[3, 3], [3, 3], [3, 3]]:
    raise Exception(".map function not working", m.matrix)


m.fill(1)
n = Matrix(3, 2)
n.fill(15)
m.add(n)
if not m.matrix == [[16, 16], [16, 16], [16, 16]]:
    raise Exception(".add function not working with matrix", m.matrix)

m = Matrix(2, 3)
m.matrix = [[7, 7, 8], [5, 9, 4]]
n = Matrix(3, 2)
n.matrix = [[21, 19], [17, 18], [18, 23]]
o = multiply(m, n)
if not o.matrix == [[410, 443], [330, 349]]:
    raise Exception("multiply function not working", o.matrix)

m = Matrix(2, 3)
m.matrix = [[1, 1, 1], [2, 2, 2]]
n = transpose(m)
if not n.matrix == [[1, 2], [1, 2], [1, 2]]:
    raise Exception("transpose function not working", n.matrix)


print("No errors were found!")
