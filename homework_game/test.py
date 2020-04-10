import tkinter
import tkinter.messagebox
root = tkinter.Tk()
root.title("ceshi")
root.geometry('800x600')
def warning():
    tkinter.messagebox.showinfo('提示','人生苦短，我用pyhon')
    print('人生苦短，我用pyhon')
tkinter.Button(root, text = '提示', command = warning).pack()
##root.mainloop()
