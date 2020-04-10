from numpy import *
class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0, self.c1, self.c2 = c0, c1, c2
    def __call__(self, x):
        return self.c0 + self.c1*x + self.c2*x**2
    def table(self, L, R, n):
        s = ''
        for x in linspace(L, R ,n):
            y = self(x)
            s += '%3g %3g\n' % (x, y)
        return s
class Line(Parabola):
    def __init__(self, c0, c1):
        Parabola.__init__(self, c0, c1, 0)
    def __call__(self, x):
        return self.c0 + self.c1*x


p = Line(1,-2)
print(p.table(0, 1, 3))
print(p(1))
