class Y:
    def __init__(self, v0):
        self.v0 = v0
        self.g = 9.81
    def __call__(self, t):
        return self.v0 * t -0.5*self.g*t**2
##    def __str__(self):
##        return 'v0*t - 0.5*g*t**2; v0 = %g' % self.v0
    def __repr__(self):
        return 'v0*t - 0.5*g*t**2; v0 = %g' % self.v0
y = Y(1)
print(y)
