from tkinter import *

root = Tk()

Label(text='x1').grid(row=0, column=0)
x1 = Entry(width=5)
x1.grid(row=0, column=1)

Label(text='y1').grid(row=0, column=2)
y1 = Entry(width=5)
y1.grid(row=0, column=3)

Label(text='x2').grid(row=1, column=0)
x2 = Entry(width=5)
x2.grid(row=1, column=1)

Label(text='y2').grid(row=1, column=2)
y2 = Entry(width=5)
y2.grid(row=1, column=3)

Checkbutton(text='Прямоугольник').grid(row=2, column=0)
Checkbutton(text='Овал').grid(row=3, column=0)
Button(text='Нарисовать').grid(row=4, column=0)

root.mainloop()
