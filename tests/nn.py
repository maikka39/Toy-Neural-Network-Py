from random import randint

from tnnp import nn as tnnp

nn = tnnp.NeuralNetwork(2, 2, 1)
if nn is None:
    raise Exception("Initialization failed!", m.matrix)

nn = tnnp.NeuralNetwork(2, 2, 1)
input = [1, 0]
output = nn.feedforward(input)
if output < [-1] or output > [1]:
    raise Exception(".feedforward function failed!", m.matrix)


def formula(x):
    # f(x) = mx + b
    if x == [0, 0]:
        return [-1]
    if x == [0, 1]:
        return [1]
    if x == [1, 0]:
        return [1]
    if x == [1, 1]:
        return [-1]


nn = tnnp.NeuralNetwork(2, 2, 1)
for i in range(50000):
    data = [randint(0, 1), randint(0, 1)]
    nn.train(data, formula(data))
values = []
for data in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    output = nn.feedforward(data)
    values.append(round(output[0]))
if not values == [-1, 1, 1, -1]:
    raise Exception(
        ".train function failed! You might want to try running this script again.", values)

nn = tnnp.NeuralNetwork(2, 2, 1)
cp = nn.copy()
if not cp:
    raise Exception(".copy function failed!", cp)

nn = tnnp.NeuralNetwork(2, 2, 1)
nn.mutate(lambda n: n * 2)

nn = tnnp.NeuralNetwork(2, 2, 1)
nn.save("test.pkl")
nn2 = tnnp.load("test.pkl")
if nn2.hidden_nodes != 2:
    raise Exception(".save/.load function failed!", nn2)

print("No errors were found!")
