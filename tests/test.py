import tnnp.tnnp as nn
from tnnp.maths.matrix import Matrix

# neuralnetwork = nn.NeuralNetwork(3, 3, 1)

m = Matrix(3, 2)

print(m.matrix)

m.add(5)
print(m.matrix)
m.multiply(3)
print(m.matrix)

n = Matrix(3, 2)
n.randomize()
print(n.matrix)
n.add(m)
print(n.matrix)
