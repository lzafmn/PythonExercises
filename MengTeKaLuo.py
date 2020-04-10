import random
N = 100000
M = 0
for i in range(N):
    black = random.randint(1,6)
    green = random.randint(1,6)
    if black > green:
        M += 1
print('probability : %.6g' % (M/N))


import numpy as np

N = 100000000
r = np.random.randint(1, 7, (2, N))
print(r)
black = r[0][:]
green = r[1][:]
success = black > green
print('success',success)
M = np.sum(success)
print('probability: %.6f' % (M/N))
##
##success = [(black > green) for black in range(1,7) for green in range(1, 7)]
##print(success)
##M = sum(success)
##print('probability: %f' % (M/36))

##def new_hat():
##    for color in ['black', 'red', 'blue']
##        for i in range(4):
##            hat.append(color)
##    return hat
##def draw_ball(hat):
##    index = random.randint(0, len(hat)-1)
##    color = hat[index]
##    del hat[index]
##    return color, hat
##n = int(input('How many balls are to be drawn? '))
