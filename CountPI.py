import numpy as np
class CountPI:
    def __init__(self):
        self.N = 100000000
        dots = np.random.uniform(0,2, (2,self.N))
        self.x = dots[0]
        self.y = dots[1]
        r = np.zeros(1)
        r[0] = 1  
        self.r = r

    def __str__(self):
        d = np.sqrt((self.x-1)**2 + (self.y-1)**2)
        success = d < self.r
        return '%f' % (np.sum(success)/self.N*4)
        
