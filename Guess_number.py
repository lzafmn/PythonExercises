import random
ans = random.randint(1,100)
while True:
    res = int(input('Please input your response 1~100 : '))
    if ans == res:
        print('U win!')
        break
    elif ans < res:
        print('Your response is too big')
    else:
        print('Your response is too small')
