from random import randint


def sign(n):
    """The activation function"""
    if n >= 0:
        return 1
    else:
        return -1


class Perceptron:
    """docstring for Perceptron."""

    def __init__(self, amount_of_inputs):
        self.amount_of_inputs = amount_of_inputs + 1  # Add 1 to the amount for the bias
        # TODO: Make learning_rate dynamic
        self.learning_rate = 0.01

        # Initialize with random weights
        self.weights = [randint(-1, 1) for i in range(self.amount_of_inputs)]
        self.bias = 1

    def guess(self, inputs):
        """Function to predict the output"""
        # Add a bias to the input
        inputs = list(inputs)
        inputs.append(self.bias)

        # Sum all the inputs multiplied by their weights
        sum = 0
        for input, weight in zip(inputs, self.weights):
            sum += input * weight

        return sign(sum)

    def train(self, inputs, target):
        inputs = list(inputs)

        guess = self.guess(inputs)
        error = target - guess

        # Tune all weights
        self.weights = [weight + error * input * self.learning_rate for weight,
                        input in zip(self.weights, inputs + [self.bias])]
        return self.weights

    def guessY(self, x):
        # w0 + w1 * x + w2 * b
        try:
            return -(self.weights[2] / self.weights[1]) - (self.weights[0] / self.weights[1]) * x
        except ZeroDivisionError:
            return 0
