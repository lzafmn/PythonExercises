import numpy as np
def 3D_integrade(R, r, N=1000000):
    V = 4*R**3*np.pi/3
    X = np.array(-R, R, N)
    x = np.array(0, r, N)
    y = np.array(-r/2, r/2, N)
    
