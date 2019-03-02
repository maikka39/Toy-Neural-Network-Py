"""
Created by: Maik de Kruif (maikka39)
"""
from random import randint


def sign(n):
    """The activation function"""
    if n >= 0:
        return 1
    else:
        return -1


class Perceptron:
    """docstring for Perceptron."""

    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate

        # Initialize with random weights
        self.weights = [randint(-1, 1) for i in range(2)]

    def guess(self, inputs):
        """Function to predict the output"""
        # Sum all the inputs multiplied by their weights
        sum = 0
        for input, weight in zip(inputs, self.weights):
            sum += input * weight

        return sign(sum)

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        # Tune all weights
        self.weights = [weight + error * input * self.learning_rate for weight,
                        input in zip(self.weights, inputs)]
