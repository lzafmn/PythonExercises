from math import pi
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-pi, pi, 200)

def mtpow(x):
    return x*mtpow(x-1) if x>0 else 1

def SIN(x0, N):
    n = 0
    y = 0
    while (2*n + 1) <= N:
        y += (-1)**n*(x-x0)**(2*n+1)/mtpow(2*n +1)
        plt.plot(x, y, label=str(2*n+1))
        n += 1
    plt.show()
def EXP(x0, min, max):
    n = 0
    y = np.zeros(len(x))
    while n <= max:
        y += ((x-x0)**n)/mtpow(n)
        if n >= min and n <= max:
            plt.plot(x, y, label=str(n))
        else:
            pass
        n += 1
    plt.legend()
    plt.show()
EXP(1, 1, 5)