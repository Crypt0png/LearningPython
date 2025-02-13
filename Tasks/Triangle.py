from tkinter import *

root = Tk()

c = Canvas(root, width=200, height=400, bg='white')
c.pack()
c.create_rectangle(10, 10, 190, 90, fill='white')
c.create_rectangle(50, 100, 130, 280, fill='yellow', outline='green')

root.mainloop()