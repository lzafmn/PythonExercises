# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 02:42:31 2020

@author: 83937
"""
import numpy as np
import random
def simulate_one_path(N, x0, p0, M, m):
    '''N:月数，X0:初始投资，p0:初始利率,M:利率变化平均月数，m：利率变化额'''
    x = np.zeros(N+1)
    p = np.zeros(N+1)
    index_set = range(0, N+1)
    x[0] = x0
    p[0] = p0
    for n in index_set[1:]:
        x[n] = x[n-1] + p[n-1]/(100.0*12)*x[n-1]
        # update interest rate p:
        r = random.randint(1, M)
        if r == 1:
            # adjust gamma:
            r = random.randint(1, 2)
            gamma = m if r == 1 else -m
        else:
            gamma = 0
        pn = p[n-1] + gamma
        p[n] = pn if 1 <= pn <= 15 else p[n-1]
    return x, p

def simulate_n_paths(n, N, L, p0, M, m):
    x=[];p=[]
    for i in range(n):
        x_,p_=simulate_one_path(N, L, p0, M, m)
        x_,p_ = x_/N,p_/N
        x.append(x_);p.append(p_)
    return x,p

x0 = 1 # initial investment
p0 = 5 # initial interest rate
N = 10*12 # number of months
M = 3 # p changes (on average) every M months
n = 1000 # number of simulations
m = 0.5 # adjustment of p
import matplotlib.pyplot as plt
#x,p=simulate_one_path(N, x0, p0, M, m)
x,p=simulate_n_paths(n, N, x0, p0, M, m)
plt.plot(x,p)
plt.show()

