class Polynomial:
    """多项式计算"""
    def __init__(self, coefficients):
        self.coeff = coefficients
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            coeffsum = self.coeff[:]
            for i in range(len(other.coeff)):
                coeffsum[i] += other.coeff[i]
        else:
            coeffsum = other.coeff[:]
            for i in range(len(self.coeff)):
                coeffsum[i] += self.coeff[i]
        return Polynomial(coeffsum)


    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            coeffsub = self.coeff[:]
            for i in range(len(other.coeff)):
                coeffsub[i] -= other.coeff[i]
        else:
            coeffsub = other.coeff[:]
            for i in range(len(self.coeff)):
                coeffsub[i] -= self.coeff[i]
            for j in range(len(coeffsub)):
                coeffsub[j] = -coeffsub[j]
        return Polynomial(coeffsub)


    def __mul__(self, other):
        coeff = [0]*(len(self.coeff)+(len(other.coeff))-1)
        for i in range(len(self.coeff)):
            for j in range(len(other.coeff)):
                coeff[i+j] = self.coeff[i]*other.coeff[j]
        return Polynomial(coeff)

        
    def __repr__(self):  # 可以在命令行输出也可以print输出
        s = ''
        for i in range(len(self.coeff)):
            if self.coeff[i] !=0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        s = s.replace('+ -', '- ')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^0', '1')
        s = s.replace('x^1', 'x')
        if s[0:3] == ' + ':
            s = s[3:]
        if s[0:3] == ' - ':
            s = '-' + s[3:]
        return s
    
##    def __str__(self):
##        s = ''
##        for i in range(len(self.coeff)):
##            if self.coeff[i] !=0:
##                s += ' + %g*x^%d' % (self.coeff[i], i)
##        s = s.replace('+ -', '- ')
##        s = s.replace(' 1*', ' ')
##        s = s.replace('x^0', '1')
##        s = s.replace('x^1', 'x')
##        if s[0:3] == ' + ':
##            s = s[3:]
##        if s[0:3] == ' - ':
##            s = '-' + s[3:]
##        return s

    
p = Polynomial([1,2,3])
P = Polynomial([2,3,2,4])
g = p + P
print(g.coeff)
print(g)
print(g(2))

##minus = p - P
minus = Polynomial.__add__(p,P)
print(minus.coeff)
print(minus)
print(P*p)

