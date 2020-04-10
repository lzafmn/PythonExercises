import numpy as np
def MCint_area(f, a, b, n, fmax):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, fmax, n)
    below = y[y <= f(x)].size
    area = below/n*(b-a)*fmax
    return area
print(MCint_area(lambda x:x**2, 1, 2, 100000, 4))
