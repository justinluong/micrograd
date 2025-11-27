class Module:

    def zero_grad(self):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError


class Neuron(Module):

    def __init__(self, nin, nonlin=True):
        raise NotImplementedError

    def __call__(self, x):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError


class Layer(Module):

    def __init__(self, nin, nout, **kwargs):
        raise NotImplementedError

    def __call__(self, x):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError


class MLP(Module):

    def __init__(self, nin, nouts):
        raise NotImplementedError

    def __call__(self, x):
        raise NotImplementedError

    def parameters(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
