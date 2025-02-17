from tkinter import *

def draw_rectangle():

root = Tk()

Label(text='x1').grid(row=0, column=0)
x1 = Entry()
x1.grid(row=0, column=1)

Label(text='y1').grid(row=0, column=1)
y1 = Entry()

Label(text='x2').grid(row=1, column=0)
x2 = Entry()

y1.grid(row=0, column=2)
x2.grid()

root.mainloop()
