from math import exp

import tnnp.maths.matrix as matrix

# from tnnp.maths.matrix import Matrix, multiply, transpose


class ActivationFunction(object):
    """Activation Function."""

    def __init__(self, func, dfunc):
        self.func = func
        self.dfunc = dfunc


sigmoid = ActivationFunction(
    lambda n: 1 / (1 + exp(-n)),
    lambda n: n * (1 - n)
)

tanh = ActivationFunction(
    lambda n: (1 - exp(-2 * n)) / (1 + exp(-2 * n)),
    lambda n: 1 - (n * n)
)


class NeuralNetwork(object):
    """Multi Layer NeuralNetwork."""

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.setLearningRate()
        self.setActivationFunction()

        self.weights_ih = matrix.Matrix(self.hidden_nodes, self.input_nodes)
        self.weights_ho = matrix.Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = matrix.Matrix(self.hidden_nodes, 1)
        self.bias_o = matrix.Matrix(self.output_nodes, 1)
        self.bias_h.fill(1)
        self.bias_o.fill(1)

    def setLearningRate(self, learning_rate=0.1):
        self.learning_rate = learning_rate

    def setActivationFunction(self, fn=sigmoid):
        self.activation_function = fn

    def feedforward(self, input_array):
        """Returns the guessed output from the input"""
        inputs = matrix.from_array(input_array)

        hidden = matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(self.activation_function.func)

        outputs = matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(self.activation_function.func)

        return outputs.to_array()

    def train(self, input_array, target_array):
        inputs = matrix.from_array(input_array)

        hidden = matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(self.activation_function.func)

        outputs = matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(self.activation_function.func)

        targets = matrix.from_array(target_array)

        output_errors = matrix.substract(targets, outputs)

        gradients = matrix.map(outputs, self.activation_function.dfunc)
        gradients.multiply(output_errors)
        gradients.multiply(self.learning_rate)

        hidden_t = matrix.transpose(hidden)
        weights_ho_deltas = matrix.multiply(gradients, hidden_t)

        self.weights_ho.add(weights_ho_deltas)
        self.bias_o.add(gradients)

        weights_ho_t = matrix.transpose(self.weights_ho)
        hidden_errors = matrix.multiply(weights_ho_t, output_errors)

        hidden_gradients = matrix.map(hidden, self.activation_function.dfunc)
        hidden_gradients.multiply(hidden_errors)
        hidden_gradients.multiply(self.learning_rate)

        inputs_t = matrix.transpose(inputs)
        weights_ih_deltas = matrix.multiply(hidden_gradients, inputs_t)

        self.weights_ih.add(weights_ih_deltas)
        self.bias_h.add(hidden_gradients)

        # print(outputs.matrix)
        # print(targets.matrix)
        # print(error.matrix)

    # Set aliasses
    guess = feedforward
