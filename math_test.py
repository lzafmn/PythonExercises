from math import *
res = 0

for i in range(4,10000000):
    res += -log(1-pi/i)
print(res)
