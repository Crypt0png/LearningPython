from tkinter import *

def paint(color):
    label['bg'] = color

class RBColor:
    def __init__(self, color, val):
        Radiobutton(text=color.capitalize(),
                    command=lambda i=color: paint(i), variable=var,
                    value=val).pack()


root = Tk()

var = IntVar()
var.set(0)
RBColor('red', 0)
RBColor('green', 1)
RBColor('blue', 2)
label = Label(width=20, height=10, bg='darkgreen')
label.pack()

root.mainloop()
