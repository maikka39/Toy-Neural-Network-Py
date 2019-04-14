import random

from tnnp import nn as tnnp

nn = tnnp.NeuralNetwork(2, 2, 1)
if nn is None:
    raise Exception("Initialization failed!", m.matrix)

nn = tnnp.NeuralNetwork(2, 2, 1)
input = [1, 0]
output = nn.feedforward(input)
if output < [-1] or output > [1]:
    raise Exception("feedforward function failed!", m.matrix)


training_data = [
    {
        "inputs": [0, 0],
        "targets": [0]
    },
    {
        "inputs": [0, 1],
        "targets": [1]
    },
    {
        "inputs": [1, 0],
        "targets": [1]
    },
    {
        "inputs": [1, 1],
        "targets": [0]
    }
]
nn = tnnp.NeuralNetwork(2, 2, 1)
for i in range(100000):
    data = random.choice(training_data)
    nn.train(data.get("inputs"), data.get("targets"))
values = []
for data in training_data:
    output = nn.feedforward(data.get("inputs"))
    values.append(round(output[0]))
if not values == [0, 1, 1, 0]:
    raise Exception(
        "train function failed! You might want to try running this script again.", values)

print("No errors were found!")
