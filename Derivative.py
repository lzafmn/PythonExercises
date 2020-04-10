from math import *

class Derivative:
    def __init__(self, g, x, h = 1E-6):
        self.g = g
        self.h = h
        self.x = x
    def __str__(self):
        return str((self.g(self.x + self.h) - g(self.x)) / self.h)
g = lambda x: x**3
df = Derivative(g, 1)
print(df)

