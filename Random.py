##导入random模块
import random
##  numpy库中也有一个random模块\
import numpy as np 

"""
random:
random()
randint(a,b)
uniform(a,b)
seed(a)
choice(iter)
shuffle(iter)
randrange(a,b [,c])

"""

####调用random方法
##print(random.random())
##
####-- uniform(a, b) --生成a,b之间的随机浮点数，b可以小于a，也可以等于a
##rfloat = random.uniform(2.999999999999999999,3.00000000000000000
##                        )
##print(rfloat)
##
####随机均匀描点
####from matplotlib.pyplot import *
####N = 500
####x = range(N)
####y = [random.uniform(-1,1) for i in x]
####axis([0,N-1, -1.2, 1.2])
####plot(x, y, '+')
####show()
##
##R = np.random.random(); r = random.random()
##print("R = np.random.random()",R)
##print('r = random.random()',r)
###-- size --生成一个数组
##R1 = np.random.random(size=10)
####-- np --数组重载的==
##R2 = np.random.randint(1,7,10)#[1,7) withdraw 10 integers
##success = R2 == 6
##print('success',success,sum(success))
##print('R1=',R1)
##print('R2=',R2)
##
####-- (np.)random.randint(a, b) --random下闭区间[]，np下前闭后开[)
####-- np.random.random_integers(a, b, size) --闭区间 
##
##
##avg = 0
##for j in range(10):
##    s = 0
##    for i in range(10000):
##        a = random.randint(1, 6)
##        if a == 6:
##            s += 1
##    avg += s/10000
##print(avg/10)
##
####  可以设置随机种子，使随机数的生成序列固定random.seed(12) （参数是整数）
##random.seed(10)
##print(['%.3f' % random.random() for i in range(6)])
##print(['%.3f' % random.random() for i in range(6)])
##random.seed(10)
##print(['%.3f' % random.random() for i in range(6)])
##
####  从迭代器中随机取出元素有3种方法  choice,   randint,    shuffle
##li = list(range(10))
##print(random.choice(range(10)))
##print(li[random.randint(0,len(li) - 1)])
##random.shuffle(li)
##print(li[0],'li:',li)
##
####  random.randrange([start,] stop [,step])   [start, stop)
##print(random.randrange(1,100,2))

def v_code():
    """ 生成随机验证码"""
    a = list(range(0,9))
    b = list(range(97, 122))
    c = list(range(65, 90))
    res = a + b
    out = ''
    for i in range(4):
        j = random.choice(res)
        if j<=122 and 65<= j:
            out += chr(j)
        else:
            out += str(j)
    print(out)
    return 0
v_code()
def check
##for i in range(123):
##    print(i,chr(i))
