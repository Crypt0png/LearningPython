from tkinter import *
from datetime import datetime as dt

def insert_time():
    t = dt.now().time()
    el.insert(0, t.strftime('%H:%M:%S'))

root = Tk()

el = Entry(width=50)
but = Button(text='time', command=insert_time)

el.pack()
but.pack()

root.mainloop()