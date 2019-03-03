from random import randint

import matplotlib.pyplot as plt

# Otherwise my beautifier somehow f*cks it up
if True:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))

    import tnnp.tnnp as nn

canvas_width_min = -10
canvas_width_max = 10
canvas_height_min = -10
canvas_height_max = 10


fig, ax = plt.subplots()
ax.axis([canvas_width_min, canvas_width_max,
         canvas_height_min, canvas_height_max])

ax.set(xlabel='X', ylabel='Y',
       title='NeuralNetwork Test')
ax.grid()


def formula(x):
    # return 1 * x
    return 1 * x + 1


class Point:
    def __init__(self, color="red", thickness=2, train_point=False):
        self.x = randint(canvas_width_min, canvas_width_max)
        self.y = randint(canvas_height_min, canvas_height_max)

        self.thickness = thickness
        # self.x = 0
        # self.y = 0

        if self.y >= formula(self.x):
            self.label = 1
        else:
            self.label = -1

        if train_point:
            return

        ax.scatter(self.x, self.y, s=self.thickness * 50, c=color)

    def change_color(self, color):
        ax.scatter(self.x, self.y, s=self.thickness * 50, c=color)


formula_line_x = []
formula_line_y = []
for x in range(canvas_width_min, canvas_width_max + 1):
    formula_line_x.append(x)
    formula_line_y.append(formula(x))
ax.plot(formula_line_x, formula_line_y, linewidth=3)


perceptron = nn.Perceptron()
points = [Point("red") for i in range(100)]

while True:
    for train_point in [Point(train_point=True) for i in range(100)]:
        perceptron.train((train_point.x, train_point.y), train_point.label)

    for point in points:
        if perceptron.guess((point.x, point.y)) == point.label:
            point.change_color("green")

    plt.pause(0.50)


plt.show()
