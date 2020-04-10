#test unifom
import random
N = 100
s1 = 0
s2 = 0
for i in range(N):
    a = random.uniform(1,3)
    if a<2:
        s1 += 1
    else:
        s2 += 1

print(s2/s1)
