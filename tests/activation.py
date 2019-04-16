from tnnp.activation import ActivationFunction, sigmoid, tanh

a = ActivationFunction(
    lambda n: 1,
    lambda n: 0
)
if not a:
    raise Exception("Initialization failed!", a)

a = ActivationFunction(
    lambda n: 1,
    lambda n: 0
)
if not a.func(3) == 1 or not a.dfunc(8) == 0:
    raise Exception("Initialization failed!", a.func, a.dfunc)

if not round(sigmoid.func(1) * 10000) == 7311:
    raise Exception("sigmoid.func function failed!", sigmoid.func)

if not sigmoid.dfunc(2) == -2:
    raise Exception("sigmoid.dfunc function failed!", sigmoid.dfunc)

if not round(tanh.func(1) * 10000) == 7616:
    raise Exception("tanh.func function failed!", tanh.func)

if not tanh.dfunc(2) == -3:
    raise Exception("tanh.dfunc function failed!", tanh.dfunc)


print("No errors were found!")
