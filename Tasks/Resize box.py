from tkinter import *

def resize(self):
    text.config(width=ent.get(), height=ent1.get())
def change_color_focus(self):
    text.configure(bg='white')
def change_color_no_focus(self):
    text.configure(bg='lightgray')

root = Tk()

ent = Entry(width=5)
ent1 = Entry(width=5)
ent.focus_set()
but = Button(text='Изменить', command=resize)
text = Text(width=10, height=10, bg='lightgray')

ent.grid(column=0, row=0)
ent1.grid(column=0, row=1)
but.grid(column=1, row=0)
but.bind('<Return>', resize)
text.grid(column=0, row=3)
text.bind('<FocusIn>', change_color_focus)
text.bind('<FocusOut>', change_color_no_focus)

root.mainloop()
