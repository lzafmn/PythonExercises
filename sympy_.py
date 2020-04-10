import sympy as sp
x = sp.symbols('x')
y = sp.symbols('y')
##t = sp.symbols('u')
##y = sp.sin(x) + sp.exp(x)**2
##建立符号表达式
z = sp.sympify('x/2+exp(y)')
##print(y.subs(x, 2))
##s = y.subs(x, 2)
##print(s.evalf())
##print(y.evalf(subs={x:2}))
##带入求值
z = sp.sin(3*sp.pi/2*x)**2+sp.cos(3*sp.pi/2*y)**2
print(z.evalf(subs={x:1, y:-1}))
print(z.subs({x:1, y:-1}).evalf())
##符号归约与化简
##符号微分/偏微分
