from tkinter import *

root = Tk()
cv = Canvas(root, background = 'white')
cv.pack(fill = BOTH, expand = YES)
##前四个参数是主对角线上两点坐标
cv.create_rectangle(30, 30, 200, 200, outline = 'red',# 边框颜色
                    stipple = 'question',# 填充的位图
                    fill = 'yellow',# 填充颜色
                    width = 5)# 边框宽度
cv.create_rectangle(380, 30, 550, 200, outline = 'red',
                    stipple = 'question',
                    fill = 'yellow', width = 5)
cv.create_oval(240, 430, 340, 200, outline = 'yellow', fill = 'pink',\
               width = 4)
root.mainloop()
