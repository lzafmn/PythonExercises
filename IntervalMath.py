class IntervalMath:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return IntervalMath(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return IntervalMath(self.a - other.b, self.b - other.a)
    def __mul__(self, other):
        alist = [self.a*other.a, self.a*other.b, self.b*other.a, self.b*other.b]
        return IntervalMath(min(alist), max(alist))
    def __truediv__(self, other):
        if other.b ==0 and other.a ==0:
            return None
        elif other.a == 0:
            blist = [self.a/other.b, self.b/other.b]
        elif other.b == 0:
            blist = [self.a/other.a, self.b/other.a]
        else:
            blist = [self.a/other.a, self.b/other.a, self.a/other.b, self.b/other.b]
        return IntervalMath(min(blist), max(blist))
    
    def __str__(self):
        return '[%.1f, %.1f]' % (self.a, self.b)


I = IntervalMath # 缩写
for l in [-4, -3]:
    for u in [-3, -2]:
        a = I(l,u)
        b = I(4,5)
        expr = 'a+b', 'a-b', 'a*b', 'a/b'
        for e in expr:
            print(e, '=', eval(e))
