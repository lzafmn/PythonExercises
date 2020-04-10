from math import *
class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Backward1(Diff):
    def __call__(self, x):
        f, h =self.f, self.h
        return (f(x) - f(x-h))/h

class Central4(Diff):
    def __call__(self, x):
        f = self.f
        h = self.h
        return 4/3*(f(x+h) - f(x-h))/(2*h) - 1/3*(f(x+2*h) - f(x-2*h))/(4*h)

f = Central4(sin)
print(f(0.5))
