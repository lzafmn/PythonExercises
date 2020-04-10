import numpy as np
from math import sin, cos
class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()
    def construct_method(self):
        raise NotImplementedError('no rule in class %s' % self.__class__.__name__)
    def integrate(self, f):
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s
    def vectorized_integrate(self, f):
        return np.dot(self.weights, f(self.points))
class Trapezoidal(Integrator):
    def construct_method(self):
        h = (self.b -self.a)/float(self.n - 1)
        x = np.linspace(self.a, self.b, self.n)
        w = np.zeros(len(x))
        w[1:-1] += h
        w[0] = h/2; w[-1] = h/2
        return x, w
class Simpson(Integrator):
    def construct_method(self):
        h = (self.b - self.a)*2/(self.n - 1)
        x = np.linspace(self.a, self.b, self.n)
        w = np.zeros(len(x))
        w[1:-1:2] += h*2/3
        w[2:-1:2] += h/3
        w[0] = h/6
        w[-1] = h/6
        return x, w
def f(x):
    return x**2
s = Simpson(0, 2, 100)
print(s.integrate(f))
t = Trapezoidal(0, 2, 100)
print(t.integrate(f))
