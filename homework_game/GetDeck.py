import random
class Deck:
    #std_number:初始手牌数  member:玩家数
    def newDeck(self, init_number=17, member=3, ):#得到一副扑克牌
        ranks=['3','4','5','6','7','8','9','A10','J','Q','QK','YA','Z2']
        suits = ['S', 'H', 'D', 'C']
        deck = []
        for s in suits:
            for r in ranks:
                deck.append(s + r)
        deck.append('BigJoker')
        deck.append('SmallJoker')
    ##  得到属性
        self.deck = deck#   一套顺序牌
        self.init_number = init_number#     初始手牌数
        self.member = member#   玩家数
        random.shuffle(self.deck)    ##        洗牌
    ##  排序后替换函数  
    def g(self, x):
        x = x.replace('A10', '10')
        x = x.replace('QK','K')
        x = x.replace('YA','A')
        x = x.replace('Z2','2')
        x = x.replace('Big', 'B')
        x = x.replace('Small', 'S')
        return x
    
    ##    确定对应座位上的玩家的身份
    def confirm_roles(self,member):
        roles = {}
        beginner = random.randint(0, member-1)
    ##   ...此处待完善
        roles['landlord'] = 0  #0对应座位序号
        roles['farmer1'] = 1   #1对应座位序号
        roles['farmer2'] = 2   #2对应座位序号
        return roles
    
    ##  从牌堆取牌返回这些牌    
    def Deal_hand(self):
    ##  hand列表记录当前手牌
        hand = []
    ##  从牌堆发init_number张牌，牌堆减少init_number张牌
        hand = self.deck[:self.init_number]
        del self.deck[:self.init_number]
                
    ##  返回摸的牌
        return hand

    def Deal(self):
        self.newDeck()
        roles = self.confirm_roles(self.member)
        hands = []
        for i in range(self.member):
            hands.append(self.Deal_hand())
        hands[roles['landlord']] += self.deck
    ##  排序
        for hand in hands:
            for i in range(1,len(hand)):
                for j in range(1,len(hand)-i+1):
                    if hand[j][1:] < hand[j-1][1:]:
                        hand[j],hand[j-1] = hand[j-1],hand[j]
    ##  'A10','QK','YA','Z2'替换回来
        for i in range(len(hands)):                
            hands[i] = list(map(self.g, hands[i]))
        return hands

        
