import tkinter
root = tkinter.Tk()
photo = tkinter.PhotoImage(file = "images\\Bjoker.gif")
photo2 = tkinter.PhotoImage(file = "images\\Sjoker.gif")
textLabel = tkinter.Label(root, text = 'a card', justify = tkinter.LEFT)
textLabel.pack()
def show_image(textLabel, photo):
    textLabel.config(image = photo)
    Button1.config(command = new_image)
def new_image():
    textLabel.config(image = photo2)
Button1 = tkinter.Button(root, text = '显示图片', command = lambda : show_image(textLabel, photo))
Button1.pack()
