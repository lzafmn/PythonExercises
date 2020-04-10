##import numpy as np
##import matplotlib.pyplot as plt
##import math
##class Y:
##    def __init__(self, v0):
##        self.v0 = v0
##        self.g  = 9.81
##    def value(self, t):
##        return self.v0*t - 0.5*self.g*t**2
##def table(f, tstop, n):
##    x = np.linspace(0, tstop, n)
##    for t in x:
##        print(t, f(t))
##    plt.plot(x, f(x))
##    plt.show()
##y = Y(6.5)
##table(y.value, 2*math.pi, 101)
##


class SelfExplorer:
    def __init__(self, a ):
        self.__a = a
##        print('init: a = %f, id(self) = %d'% (self.a, id(self)))
    def get_a(self):
        return self.__a
    def value(self, x):
        print('value: a = %g, id(self) = %d' % (self.a, id(self)))
        return(self.a*x)
s1 = SelfExplorer(1)
print(s1.get_a())

