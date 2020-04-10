# A: ace, J: jack, Q: queen, K: king
# C: clubs, D: diamonds, H: hearts, S: spades
import random
class Deck:
    # 生成一套牌self.deck
    def make_deck(self):
        ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        suits = ['C', 'D', 'H', 'S']
        deck = []
        for s in suits:
            for r in ranks:
                deck.append(s + r)
        deck.append('BJoker')
        deck.append('SJoker')
        random.shuffle(deck)
        return deck
    # 从牌堆deck拿n张牌发到一个人的手中hand   返回手牌列表hand 和 剩下牌堆deck
    def deal_hand(self,n, deck):
        hand = []
        for i in range(n):
            hand.append(deck[i])
        del deck[:n]
        return hand, deck
    
    #发牌，cards_per_hand：每个人发牌数， no_of_players：人数
    def deal(self, cards_per_hand, no_of_players):
        deck = self.make_deck() #生成一堆牌
        hands = [] #所有玩家的手牌列表
        for i in range(no_of_players): #按人数开始发牌
            #返回手牌列表hand 和 剩下牌堆deck
            hand, deck = self.deal_hand(cards_per_hand, deck)
            hands.append(hand)#所有玩家手牌列表增加一名玩家的手牌
        ld_index = random.randint(0,2)
        hands[ld_index].append(self.deck)
        return hands #返回所有玩家手牌列表

    #  返回数量刚好是n_of_a_kind的牌的 牌面数和牌面列表
    def same_rank(self, hand, n_of_a_kind):
        ranks = [card[1:] for card in hand] #取牌面
        counter = 0
        already_counted = [] 
        for rank in ranks:
            if rank not in already_counted and \
               ranks.count(rank) == n_of_a_kind:
                counter += 1
                already_counted.append(rank)
        return counter,already_counted
    #hand:一手牌
    
    def same_suit(self, hand):
        suits = [card[0] for card in hand]
        counter = {} # counter[suit]存放suit花色的数量
        for suit in suits:
            count = suits.count(suit)
            if count > 1:#只记录花色数大于1的
                counter[suit] = count
        return counter

    #实现随机地主
    def deal__ddz(self):
        deck = self.make_deck() #生成一堆牌
        hands = [] #所有玩家的手牌列表
        for i in range(3): #按人数开始发牌
            #返回手牌列表hand 和 剩下牌堆deck
            hand, deck = self.deal_hand(17, deck)
            hands.append(hand)#所有玩家手牌列表增加一名玩家的手牌
        ld_index = random.randint(0,2)
        hands[ld_index] += deck
        rank_dict = {}
        rank_dict['land_lord'] = hands[ld_index]
        rank_dict['farmer'] = hands
        return rank_dict

    
mDeck = Deck()
hands = mDeck.deal__ddz()
print(hands)
##print(mDeck.same_rank(hand,2))
##print(mDeck.same_suit(hand))
