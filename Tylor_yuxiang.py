from math import e
import numpy as np
import matplotlib.pyplot as plt

def mtpow(x):
    return x*mtpow(x-1) if x>0 else 1
error = 1
res = 0
n = 0
while error > 1E-5:
    res += 2**n/mtpow(n)
    error = abs(res - e**2)
    n += 1
print(n-1)

 