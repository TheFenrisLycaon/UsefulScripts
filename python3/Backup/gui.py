from tkinter import *

root = Tk()
root.title("Simple Gui Tryout")

e = Entry(root)
e.pack()


def Reveal():
    mylabel = Label(root, text="Hello " + e.get(), bg="Black", fg="White", padx=50)
    mylabel.pack()


mybutton = Button(root, text="Click Me!!", command=Reveal)
mybutton.pack()

root.mainloop()
