from tkinter import *

def add_item():
    buy.readlines()
    box2.append(box1.pop(0))
def delete_item():
    products.readlines()
    box1.append(box2.pop(0))

root = Tk()

box1 = (Listbox(selectmode=EXTENDED))
box1.pack(side=LEFT)
box2 = (Listbox(selectmode=EXTENDED))
box2.pack(side=RIGHT)
scroll1 = Scrollbar(command=box1.yview)
scroll2 = Scrollbar(command=box2.yview)
scroll1.pack(side=LEFT, fill=Y)
scroll2.pack(side=RIGHT, fill=Y)
box1.config(yscrollcommand=scroll1.set)
box2.config(yscrollcommand=scroll2.set)

f1 = Frame()
f2 = Frame()
f1.pack(side=LEFT)
f2.pack(side=RIGHT)

Button(text='>>>', command=add_item).pack()
Button(text='<<<', command=delete_item).pack()

buy = open('buylst.txt', 'r+')
products = open('productlst.txt', 'r+')
buy.readlines()
products.readlines()

root.mainloop()


