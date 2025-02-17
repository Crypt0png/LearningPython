# Напишите программу по следующему описанию:
# Нажатие Enter в однострочном текстовом поле(Entry) приводит к перемещению текста
# из него в список. При двойном клике по элементу - строке списка она должна
# копироваться в текстовое поле.
# <Double-Button-1> - двойной клик левой кнопкой мыши
# Listbox - виджет, хранящий список
# <Return> - нажатие Enter

from tkinter import *

def insert_txt(self):
    box.insert(END, en.get())
    en.delete(0, END)

def insert_en(self):
    en.delete(0, END)
    select = box.get(ACTIVE)
    en.insert(0, select)

root = Tk()

text = StringVar()

en = Entry(textvariable=text)
en.pack()
en.bind('<Return>', insert_txt)

box = Listbox()
box.pack()
box.bind('<Double-Button-1>', insert_en)

root.mainloop()
