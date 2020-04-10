import numpy as np

def g(x):
    return np.sin(np.pi*x/2)


def interp(x):
    return g(0)*(x-1)*(x-3)/3 + g(1)*x*(x-3)/(-2) + g(3)*x*(x-1)/(3*2)

x = np.linspace(-2, 5)
y = interp(x)
delta = abs(g(x) - y)
maxi = max(delta)
print(maxi)

kesi = 1
Delta = abs(np.pi**3/48*x*(x-1)*(x-3))
Maxi = max(Delta)
print(Maxi)
