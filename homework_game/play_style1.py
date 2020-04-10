import tkinter as tk
import GetDeck as gd

game = tk.Tk()
game.title('欢迎来到斗地主')


OneDeck = gd.Deck()
hands = OneDeck.Deal()
out_list0 = []
out_list1 = []
out_list2 = []
hand_cards0=[]
hand_cards1=[]
hand_cards2=[]
def uplift0(i):
    out_list0.append(i)


def outs0():
    for i in out_list0:
        hand_cards0[i].grid(row=1)
def uplift1(i):
    out_list1.append(i)


def outs1():
    for i in out_list1:
        hand_cards1[i].grid(row=4)
def uplift2(i):
    out_list2.append(i)

def outs2():
    for i in out_list2:
        hand_cards2[i].grid(row=7)
def shuffle():
    hands = OneDeck.Deal()
    start()
def start():
    START.destroy()
    hand0 = hands[0]
    tk.Label(game, text='landlord\'s cards').grid(row=0,column = 0)
    for i in range(len(hand0)):
        code = """
hand_cards0.append(tk.Button(game, text=hand0[i], command=lambda : uplift0(%d),width=5, height=5, activebackground='yellow', relief='groove',anchor='n'))
hand_cards0[i].grid(row=2, column=i+1, sticky='s', padx=2)
"""% i
        exec(code)
        if hand0[i][0] == '♥':
            hand_cards0[i]['fg'] ='red'
        if hand0[i][0] == '♦':
            hand_cards0[i]['fg'] ='red' 
    Out = tk.Button(game, text='Outs', command=outs0, width=5, height=5)
    Out.grid(row=2, column=len(hand0)+1, sticky='s',padx=5)


    hand1 = hands[1]
    tk.Label(game, text='farmer1\'s cards').grid(row=3, column = 0)
    for i in range(len(hand1)):
        code = """
hand_cards1.append(tk.Button(game, text=hand1[i], command=lambda : uplift1(%d),width=5, height=5, activebackground='yellow', relief='groove',anchor='n'))
hand_cards1[i].grid(row=5, column=i+1, sticky='s', padx=2)
"""% i
        exec(code)
        if hand1[i][0] == '♥':
            hand_cards1[i]['fg'] ='red'
        if hand1[i][0] == '♦':
            hand_cards1[i]['fg'] ='red' 
    Out = tk.Button(game, text='Outs', command=outs1, width=5, height=5)
    Out.grid(row=5, column=len(hand1)+1, sticky='s',padx=5)


    hand2 = hands[2]
    tk.Label(game, text='farmer2\'s cards').grid(row=6, column = 0)
    for i in range(len(hand2)):
        code = """
hand_cards2.append(tk.Button(game, text=hand2[i], command=lambda : uplift2(%d),width=5, height=5, activebackground='yellow', relief='groove',anchor='n'))
hand_cards2[i].grid(row=8, column=i+1, sticky='s', padx=2)
"""% i
        exec(code)
        if hand2[i][0] == '♥':
            hand_cards2[i]['fg'] ='red'
        if hand2[i][0] == '♦':
            hand_cards2[i]['fg'] ='red' 
    Out = tk.Button(game, text='Outs', command=outs2, width=5, height=5)
    Out.grid(row=8, column=len(hand2)+1, sticky='s',padx=5)    




START = tk.Button(game, text='开始', command=start,\
                  width=10, anchor='n', bg='RoyalBlue', font = ('微软雅黑'))
START.grid(row=2,column=2,sticky='s', padx=500)

game.mainloop()

