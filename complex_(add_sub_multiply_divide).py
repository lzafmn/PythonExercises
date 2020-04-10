from math import sqrt
class MyComplex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i
    def __add__(self, other):
        if isinstance(other,(int, float)):
            return MyComplex(self.real + other, self.imag)
        if isinstance(other, (MyComplex, complex)):
            return MyComplex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        if isinstance(other,(int, float)):
            return MyComplex(self.real - other, self.imag)
        if isinstance(other, (MyComplex, complex)):
            return MyComplex(self.real - other.real, self.imag - other.imag)
    def __abs__(self):
        return sqrt((self.real)**2 + (self.imag)**2)
    def __mul__(self, other):
        if isinstance(other,(int, float)):
            return MyComplex(self.real * other, self.imag * other.real)
        if isinstance(other, (MyComplex, complex)):
            return MyComplex(self.real * other.real - self.imag * other.imag, self.real*other.imag + self.imag*other.real)
    def __div__(self, other):
        if isinstance(other,(int, float)):
            return MyComplex(self.real / other, self.imag / other)
        if isinstance(other, (MyComplex, complex)):
            return MyComplex((self * other).real / (abs(other)**2), (self * other).imag / (abs(other)**2))
    def __str__(self):
        return str(self.real) + '+' + str(self.imag) + 'j'
a = MyComplex(1, 2)
b = MyComplex(1, 2)
print(a / b)

