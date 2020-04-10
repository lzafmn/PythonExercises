import numpy as np
import random
import matplotlib.pyplot as plt
def oneD_walk(ns):
    x =range(ns)
    y = np.zeros(ns)
    for i in x[1:]:
        coin = random.randint(1,2)
        if coin == 1:
            y[i] = y[i-1]-1
        else:
            y[i] = y[i-1]+1
    return y[-1]
def twoD_walk(np=1000, ns=100):
    X = []
    Y = []
    for i in range(np):
        x = 0
        y = 0
        for j in range(1,ns+1):
            tool = random.randint(1,2)
            if tool == 1:
                x += oneD_walk(2)
            else:
                y += oneD_walk(2)
        X.append(x)
        Y.append(y)
    return X,Y
x,y = twoD_walk()
plt.plot(x,y,'+')
plt.show()
                
            
