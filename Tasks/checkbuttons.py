from tkinter import *

root = Tk()

check_var = BooleanVar()

c0 = Checkbutton(text='0', variable=check_var)
c1 = Checkbutton(text='1', variable=check_var)
c2 = Checkbutton(text='2', variable=check_var)
c3 = Checkbutton(text='3', variable=check_var)
c4 = Checkbutton(text='4', variable=check_var)
c5 = Checkbutton(text='5', variable=check_var)
c6 = Checkbutton(text='6', variable=check_var)
c7 = Checkbutton(text='7', variable=check_var)
c8 = Checkbutton(text='8', variable=check_var)
c9 = Checkbutton(text='9', variable=check_var)
c0.grid(column=0, row=0)
c1.grid(column=1, row=0)
c2.grid(column=2, row=0)
c3.grid(column=3, row=0)
c4.grid(column=4, row=0)
c5.grid(column=5, row=0)
c6.grid(column=6,row=0)
c7.grid(column=7, row=0)
c8.grid(column=8, row=0)
c9.grid(column=9, row=0)

Button(text='all on', command=lambda: check_var.set(True)).grid(column=10, row=1)
Button(text='all off', command=lambda: check_var.set(False)).grid(column=11, row=1)

root.mainloop()