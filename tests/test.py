"""
Created by: Maik de Kruif (maikka39)
"""
import time
from random import randint
from tkinter import Canvas, Tk

# Otherwise my beautifier somehow f*cks it up
if True:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))

    import tnnp.tnnp as nn


class Point:
    def __init__(self, canvas, color, train_point=False):
        self.x = randint(0, canvas_width)
        self.y = randint(0, canvas_height)
        # self.x = 0
        # self.y = 0

        self.canvas = canvas

        if self.y >= formula(self.x):
            self.label = 1
            outline_color = "green"
        else:
            self.label = -1
            # outline_color = "red"
            outline_color = "green"

        if train_point:
            return

        self.id = canvas.create_oval(-8, -8, 8, 8,
                                     fill=color, outline=outline_color, width=3)
        self.canvas.move(self.id, self.x, self.y)

    def change_color(self, color):
        self.canvas.itemconfig(self.id, fill=color)


def formula(x):
    # return 1 * x
    return 1 * x + 100


def draw_once():
    y = 0
    last_x = 0
    for x in range(canvas_width):
        last_y = y
        y = formula(x)
        canvas.create_line(last_x, last_y, x, y, fill="#000000", width=4)
        last_x = x

    # canvas.create_line(0, 0, canvas_width, canvas_height, fill="#000000")


def draw():
    for train_point in [Point(canvas, "white", train_point=True) for i in range(1000)]:
        perceptron.train((train_point.x, train_point.y), train_point.label)

    for point in points:
        if perceptron.guess((point.x, point.y)) == point.label:
            point.change_color("green")
        else:
            point.change_color("red")

    canvas.after(int(1000 / fps), draw)  # Loop every X ms


if __name__ == '__main__':
    window = Tk()
    window.title("NeuralNetwork Testing")
    window.resizable(0, 0)
    window.wm_attributes("-topmost", 1)  # Always keep window on top of others
    canvas_width = 400
    canvas_height = 400
    canvas = Canvas(window, width=canvas_width,
                    height=canvas_height, bd=0, highlightthickness=0)
    canvas.pack()

    perceptron = nn.Perceptron()

    points = [Point(canvas, "white") for i in range(1000)]
    fps = 60

    draw_once()
    draw()
    window.mainloop()
