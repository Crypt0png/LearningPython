from tkinter import *

root = Tk()

f_top = LabelFrame(text='Верх')
f_bot = LabelFrame(text='Низ')

l1 = Label(f_top, width=7, height=4, bg='yellow', text='1')
l2 = Label(f_top, width=7, height=4, bg='orange', text='2')
l3 = Label(f_bot, width=7, height=4, bg='lightgreen', text='3')
l4 = Label(f_bot, width=7, height=4, bg='lightblue', text='4')

f_top.pack(padx=10, pady=10)
f_bot.pack(ipadx=15, ipady=20)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=RIGHT)
l4.pack(side=LEFT)

root.mainloop()
