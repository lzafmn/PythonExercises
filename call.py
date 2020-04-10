from math import *
from sympy import *
g = lambda x:x**3
x = Symbol('t')
dgdt = diff(g(x), x)
print(dgdt)
dg = lambdify([x], dgdt)
print(dg(1))

def trapezoidal(f, a, x, n):
    h = (x - a)/n
    I = 0.5*f(a)
    for i in range(1,n):
        I += f(a + i*h)
    I += 0.5*f(x)
    I *= h
    return I

class Integral:
    def __init__(self, f, a ,n=100):
        self.f, self.a ,self.n = f, a, n
    def __call__(self, x):
        return trapezoidal(self.f, self.a, x, self.n)
i = Integral(g, 1)
print(i(3))

class test:
    def __init__(self):
        print('hello')
    def __call__(self,j):
        return 'hello'
t = test()
##print(t(1))
        
