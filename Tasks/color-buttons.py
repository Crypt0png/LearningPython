from tkinter import *

def insert_color(button):
    colorid = en.get()
    lab.config(text=colorid)
    button.config(bg=colorid)

root = Tk()

f_top = Frame(root)
f_bot = Frame(root)

en = Entry(f_top, justify="center")
lab = Label(f_top)

but1 = Button(f_bot, width=2, command=lambda: insert_color(but1))
but2 = Button(f_bot, width=2, command=lambda: insert_color(but2))
but3 = Button(f_bot, width=2, command=lambda: insert_color(but3))
but4 = Button(f_bot, width=2, command=lambda: insert_color(but4))
but5 = Button(f_bot, width=2, command=lambda: insert_color(but5))
but6 = Button(f_bot, width=2, command=lambda: insert_color(but6))
but7 = Button(f_bot, width=2, command=lambda: insert_color(but7))
but8 = Button(f_bot, width=2, command=lambda: insert_color(but8))
but9 = Button(f_bot, width=2,command=lambda: insert_color(but9))

f_top.pack(padx=15, pady=15)
f_bot.pack(padx=20, pady=20)

en.pack()
lab.pack()
but1.grid(column=0, row=0, padx=5, pady=5)
but2.grid(column=1, row=0, padx=5, pady=5)
but3.grid(column=2, row=0, padx=5, pady=5)
but4.grid(column=0, row=1, padx=5, pady=5)
but5.grid(column=1, row=1, padx=5, pady=5)
but6.grid(column=2, row=1, padx=5, pady=5)
but7.grid(column=0, row=2, padx=5, pady=5)
but8.grid(column=1, row=2, padx=5, pady=5)
but9.grid(column=2, row=2, padx=5, pady=5)

root.mainloop()
