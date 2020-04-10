from math import *

class Integral:
    def __init__(self, f, a, n):
        self.a = a
        self.g = f
        self.n = n
    def __call__(self, b):
        self.b = b 
        s = 0
        h = (self.b - self.a)/self.n
        for i in range(1, self.n):
            s += self.g(self.a + i*h)
        return '%.4f' % (h*(0.5*self.g(self.a) + s + 0.5*self.g(self.b)))


def f(x):
    return exp(-x**2)*sin(10*x)
