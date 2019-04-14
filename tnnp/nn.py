from math import exp

import tnnp.maths.matrix as matrix

# from tnnp.maths.matrix import Matrix, multiply, transpose


class NeuralNetwork(object):
    """Multi Layer NeuralNetwork."""

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = matrix.Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = matrix.Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = matrix.Matrix(self.hidden_nodes, 1)
        self.bias_o = matrix.Matrix(self.output_nodes, 1)
        self.bias_h.fill(1)
        self.bias_o.fill(1)

    def feedforward(self, input_arr):
        """Returns the guessed output from the input"""
        input = matrix.from_array(input_arr)

        hidden = matrix.multiply(self.weights_ih, input)
        hidden.add(self.bias_h)
        hidden.map(sign)

        output = matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(sign)

        return output.to_array()

    # Set aliasses
    guess = feedforward


def sign(n):
    """The activation function"""
    return 1 / (1 + exp(-n))
