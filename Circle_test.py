class Circle:
    def __init__(self, x0, y0, R):
        self.x0, self.y0, self.R  = x0, y0, R
    def circumference(self):
        return 2*pi*self.R
    def area(self):
        return pi*self.R**2

from math import pi
def tes_Circle():
    R = 2.5
    c = Circle(74, -8.1, R)
    expected_area = pi*R**2
    computed_area = c.area()
    diff = abs(expected_area - computed_area)
    tol = 1E-14
    assert diff < tol, 'bug in Circle.area, diff=%s' % diff
    expected_circumference = 2*pi*R
    computed_circumference = c.circumference()
    diffc = abs(expected_circumference - computed_circumference)
    assert diffc < tol, 'bug in Circle.area, diff=%s' % diffc
    
               
