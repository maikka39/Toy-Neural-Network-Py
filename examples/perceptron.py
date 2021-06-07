from random import randint

import matplotlib.pyplot as plt

import tnnp.perceptron as pct

canvas_width_min = -10
canvas_width_max = 10
canvas_height_min = -10
canvas_height_max = 10


fig, ax = plt.subplots()
ax.axis([canvas_width_min, canvas_width_max,
         canvas_height_min, canvas_height_max])

ax.set(xlabel='X', ylabel='Y',
       title='Perceptron Test')
ax.grid()


def formula(x):
    # f(x) = mx + b
    return 2 * x + 4


class Point:
    def __init__(self, x=None, y=None, color="red", thickness=2, train_point=False):
        self.x = x
        self.y = y

        if not x:
            self.x = randint(canvas_width_min, canvas_width_max)
        if not y:
            self.y = randint(canvas_height_min, canvas_height_max)
        # self.x = 0
        # self.y = 0

        if self.y >= formula(self.x):
            self.label = 1
        else:
            self.label = -1

        if train_point:
            return

        self.thickness = thickness

        self.scatter = ax.scatter(
            self.x, self.y, s=self.thickness * 50, c=color)

    def change_color(self, color):
        self.scatter.set_color(color)


formula_line_x = []
formula_line_y = []
for x in range(canvas_width_min, canvas_width_max + 1):
    formula_line_x.append(x)
    formula_line_y.append(formula(x))
ax.plot(formula_line_x, formula_line_y, linewidth=3, c="black")


perceptron = pct.Perceptron(2)
points = [Point(color="red") for _ in range(200)]

# Plot guessed line
guess_line = ax.plot(
    (canvas_width_min, canvas_width_max),
    (perceptron.guessY(canvas_width_min), perceptron.guessY(canvas_width_max)),
    linewidth=3, c="blue")

while True:
    for train_point in [Point(train_point=True) for _ in range(15)]:
        perceptron.train((train_point.x, train_point.y), train_point.label)

    for point in points:
        if perceptron.guess((point.x, point.y)) == point.label:
            point.change_color("green")
        else:
            point.change_color("red")

    # Plot guessed line
    guess_line.pop().remove()  # Remove previous guess
    guess_line = ax.plot(
        (canvas_width_min, canvas_width_max),
        (perceptron.guessY(canvas_width_min), perceptron.guessY(canvas_width_max)),
        linewidth=3, c="blue")

    plt.pause(0.05)
