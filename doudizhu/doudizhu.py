##import tkinter
##
##
##root = tkinter.Tk()
##root.title('Show Canvas Pic')
##root.geometry('800x600')
##cv = tkinter.Canvas(root, bg = 'white', width=700, height= 600)
##b_joker = tkinter.PhotoImage(file= r"images\BJoker.gif")
##s_joker = tkinter.PhotoImage(file= r"images\SJoker.gif")
##cv.create_image(100, 100, image=b_joker)
##cv.create_image(130, 100, image=s_joker)
##cv.pack()
##root.mainloop()
import tkinter as tk

root = tk.Toplevel()
photo = tk.PhotoImage(file='images\\BJoker.gif') #创建一个图片对象
textLabel = tk.Label(root,
                  text='一张牌',
                  justify = "left"
                     ,   #定义多行文本如何对齐。可取值有：LEFT, RIGHT, 或 CENTER
                  image=photo) #设置标签图片
textLabel.pack()
root.mainloop()
