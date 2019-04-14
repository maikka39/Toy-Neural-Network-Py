from tnnp.maths.matrix import (Matrix, add, from_array, map, multiply,
                               substract, transpose)

m = Matrix(3, 2)
if not m.matrix == [[0, 0], [0, 0], [0, 0]]:
    raise Exception("Initialization failed!", m.matrix)

m = Matrix(3, 2)
m.fill(1)
if not m.matrix == [[1, 1], [1, 1], [1, 1]]:
    raise Exception(".fill function not working", m.matrix)

m = Matrix(3, 2)
m.add(5)
if not m.matrix == [[5, 5], [5, 5], [5, 5]]:
    raise Exception(".add function not working with number", m.matrix)

m = Matrix(3, 2)
m.fill(10)
m.substract(5)
if not m.matrix == [[5, 5], [5, 5], [5, 5]]:
    raise Exception(".substract function not working with number", m.matrix)

m = Matrix(3, 2)
m.fill(5)
m.multiply(3)
if not m.matrix == [[15, 15], [15, 15], [15, 15]]:
    raise Exception(".multiply function not working", m.matrix)

m = Matrix(3, 2)
m.randomize()
if m.matrix == [[1, 1], [1, 1], [1, 1]]:
    raise Exception(".randomize function not working", m.matrix)

m = Matrix(3, 2)
m.fill(2)
m.map(lambda a: a * 2 + 1)
if not m.matrix == [[5, 5], [5, 5], [5, 5]]:
    raise Exception(".map function not working", m.matrix)

m = Matrix(3, 2)
m.fill(1)
n = m.to_array()
if not n == [1, 1, 1, 1, 1, 1]:
    raise Exception(".to_array function not working", n)


m = Matrix(3, 2)
m.fill(1)
n = Matrix(3, 2)
n.fill(15)
m.add(n)
if not m.matrix == [[16, 16], [16, 16], [16, 16]]:
    raise Exception(".add function not working with matrix", m.matrix)

m = Matrix(3, 2)
m.fill(1)
n = Matrix(3, 2)
n.fill(15)
m.substract(n)
if not m.matrix == [[-14, -14], [-14, -14], [-14, -14]]:
    raise Exception(".substract function not working with matrix", m.matrix)

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

m = from_array([1, 2, 3, 4])
if not m.matrix == [[1], [2], [3], [4]]:
    raise Exception("from_array function not working", m.matrix)

m = Matrix(3, 2)
m.fill(1)
n = Matrix(3, 2)
n.fill(15)
o = add(m, n)
if not o.matrix == [[16, 16], [16, 16], [16, 16]]:
    raise Exception("add function not working with matrix", o.matrix)

m = Matrix(3, 2)
m.fill(1)
n = Matrix(3, 2)
n.fill(15)
o = substract(m, n)
if not o.matrix == [[-14, -14], [-14, -14], [-14, -14]]:
    raise Exception("substract function not working with matrix", o.matrix)


m = Matrix(3, 2)
m.fill(2)
n = map(m, lambda n: n * 2 + 1)
if not n.matrix == [[5, 5], [5, 5], [5, 5]]:
    raise Exception("map function not working", n.matrix)


print("No errors were found!")
