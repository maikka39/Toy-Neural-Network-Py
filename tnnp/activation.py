from math import exp


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
