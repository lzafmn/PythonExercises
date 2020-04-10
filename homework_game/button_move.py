import  sys
from tkinter import *
root = Tk()
root.geometry("480x320") #Raspberry Pi touchscreen resolution
root.title("Counter")

counter = 30

def goUp():
    counter += 1
    mButton2.config(text = "", borderwidth = 0, highlightthickness=0, relief='ridge', pady = "100")

def downClick():
    counter -= 1
    mButton1.config(text = counter, borderwidth = 0, highlightthickness=0, relief='ridge', pady = "100")

mButton1 = Button(text = counter, command = downClick, height = 4000, width = 320, font = ("Monospace", 200))
mButton1.pack()

mButton2 = Button(text = "", command = downClick, height = 50, width = 50, font = ("Monospace", 10))
mButton2.pack()

root.mainloop()
