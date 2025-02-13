from tkinter import *

root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_triangle(10,10, 100,100, 10)