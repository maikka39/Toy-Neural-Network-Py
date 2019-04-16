from random import randint

import matplotlib.pyplot as plt

from tnnp import activation
from tnnp import nn as tnnp

res = 20


def vmap(n, start1, stop1, start2, stop2):
    return (n - start1) / (stop1 - start1) * (stop2 - start2) + start2


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


class Point:
    def __init__(self, x, y, c, thickness=50):
        self.x = x
        self.y = y
        self.scatter = ax.scatter(
            self.x, self.y, s=thickness, c=c)

    def change_color(self, c):
        self.scatter.set_color(c)


fig, ax = plt.subplots()
ax.axis([0, 1, 0, 1])
ax.set(xlabel='X', ylabel='Y',
       title='XOR')
ax.grid()

nn = tnnp.NeuralNetwork(2, 2, 1)
nn.setActivationFunction(activation.tanh)

points = []
for x in range(res + 1):
    for y in range(res + 1):
        points.append(Point(x / res, y / res, "0"))

while True:
    for i in range(100):
        data = [randint(0, 1), randint(0, 1)]
        nn.train(data, formula(data))

    for data in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        output = nn.guess(data)
        print([(round(output[0]))], output)

    for point in points:
        color = nn.guess([point.x, point.y])[0]
        color = vmap(color, -1, 1, 0, 1)
        point.change_color(str(color))

    print("")
    plt.pause(0.05)


plt.show()
