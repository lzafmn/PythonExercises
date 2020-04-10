import random
import time
def compare():
    user = int(input("\n提示：请出拳头0（石头） 1（剪刀） 2（布）: "))
    if (user >= 0 and user < 3 ):
        pass
    else:
        print("输入不合法,请再次输入")
        user = int(input("\n提示：请出拳头0（石头） 1（剪刀） 2（布）: "))
    atr = ['石头', '剪刀', '布']
    print("用户出拳%d %s" % (user, atr[user]))
    pc = random.randint(0, 2)
    print("电脑出拳%d %s" % (pc, atr[pc]))
    time.sleep(1)
    if (user == 0 and pc == 1) or (user == 1 and pc == 2) or (user == 2 and pc ==0):
        print("你赢了")
        return 1
    elif(pc == 0 and user == 1) or (pc == 1 and user == 2) or (pc == 2 and user ==0):
        print("你输了")
        return 2
    else:
        print("平")
        return 0
count = 0
countu = 0
countp = 0
while countu < 2 and countp < 2:
    count += 1
    print('\n第%d局' % count)
    res = compare()
    if res == 1:
        countu += 1
    elif res == 2:
        countp += 1
    else:
        pass

