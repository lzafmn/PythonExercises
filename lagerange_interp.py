import numpy as np
import matplotlib.pyplot as plt
def interp(x):
    return -1.0*x*(x-3)/(1-3)+9.0*(x-1)*x/(3*(3-1))
x = np.linspace(-10, 20 , 101)
y = interp(x)
plt.plot(x, y, 'b-')
plt.show()
