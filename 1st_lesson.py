##class Y:
##    def __init__(self, v0):
##        self.v0 = v0
##        self.g = 9.81
##    def value(self, t):
##        return self.v0*t - 0.5*self.g*t**2
##y1 = Y(0.2)
##y2 = Y(0.5)
##print("y1 %.4f"% (y1.value(0.1)))
##print("y2 %.4f"% (y2.value(0.1)))

class VelocityProfile:
    def __init__(self, beta, mu0, n, R):
        self.beta = beta
        self.mu0 = mu0
        self.n = n
        self.R = R
    def __cal__
