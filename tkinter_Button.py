import tkinter 
import tkinter.messagebox
root = tkinter.Tk()
root.geometry('400x400+0+0')
root.title('Test')
photo = tkinter.PhotoImage(file=r'C:\Users\lza\Documents\Python Scripts\doudizhu\images\images\Bjoker.gif')
label = tkinter.Label(root, text='a card')
imgage=r'C:\Users\lza\Documents\Python Scripts\doudizhu\images\images\BJoker.gif'
def showImage(label,image):
    label.config(image=image)
def warning():
    tkinter.messagebox.showinfo('提示','人生苦短')
    print('提示：人生苦短')
tkinter.Button(root, text = '提示', command=warning).pack()
root.mainloop()

##class App:
##    def __init__(self, root):
##        self.root = root
##        self.root.title('提示测试')
##        self.root.geometry('200x200')
##        self.photo = tkinter.PhotoImage(file=r'C:\Users\lza\Pictures\timg.gif')
##        tkinter.Button(self.root, text='tip', command=self.warning).pack()
##        
##        
##    def warning(self):
##        tkinter.messagebox.showinfo('tishi',"Warning!")
##        print('warning')
##
##root = tkinter.Tk()
##app = App(root)
##    
        
