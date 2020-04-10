import matplotlib.pyplot as plt
import math 
import numpy as np
x1 = np.linspace(0, math.pi, 1000)

y1 = np.cos(x1)**3
y2 = np.sin(x1)**3

##x2 = np.linspace(1.001,3.142, 1000)
##y2 = (np.sin(x2)/(1- x2))
##plt.xlim(0,11)
plt.plot(y1,y2)

##plt.plot(x1,np.sqrt(1/2)*x1/x1)
##plt.plot(x2, y2)
##plt.plot(y,x)
##plt.plot(x, 0*x)
##plt.plot(0*x, x)
plt.show()
