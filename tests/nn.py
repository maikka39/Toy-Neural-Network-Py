from tnnp import nn as tnnp

nn = tnnp.NeuralNetwork(2, 2, 1)
if nn is None:
    raise Exception("Initialization failed!", m.matrix)

nn = tnnp.NeuralNetwork(2, 2, 1)
input = [1, 0]
output = nn.feedforward(input)
print(output)
if output < [-1] or output > [1]:
    raise Exception("feedforward failed!", m.matrix)


print("No errors were found!")
