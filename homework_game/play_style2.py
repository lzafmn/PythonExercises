import tkinter 
import GetDeck as gd

game = tkinter.Tk()
game.title('欢迎来到斗地主')
game.geometry('1500x900')
cv = tkinter.Canvas(game, bg = 'white', width = 1500, height = 900)
photo_list_list = []
photo_list = []
OneDeck = gd.Deck()
hands = OneDeck.Deal()
x0 = 400
y0 = 800
x1 = 180
y1 = 70
x2 = 1300
y2 = 70

background = tkinter.PhotoImage(file = 'images\\bg.gif')
cv.create_image(750,450,image = background)
for card in hands[0]:
    x0 += 30
    photo_list.append(tkinter.PhotoImage(file = 'images\\' + card + '.gif'))
    cv.create_image(x0, y0, image = photo_list[-1])
photo_list_list.append(photo_list)
for card in hands[1]:
    y1 += 30
    photo_list.append(tkinter.PhotoImage(file = 'images\\' + card + '.gif'))
    cv.create_image(x1, y1, image = photo_list[-1])
photo_list_list.append(photo_list)
for card in hands[2]:
    y2 += 30
    photo_list.append(tkinter.PhotoImage(file = 'images\\' + card + '.gif'))
    cv.create_image(x2, y2, image = photo_list[-1])
photo_list_list.append(photo_list)

cv.pack()
game.mainloop()

