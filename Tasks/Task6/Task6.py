from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()

def extract_text():
    file_name = fd.asksaveasfilename(
        filetypes=(('TXT files', '*.txt'),
                   ('HTML files', '*.html'),
                   ('ALL files', '*.*')))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

def delete_text():
    answer = mb.askyesno(
        title='Внимание!',
        message='Вы точно хотите очистить текстовое поле?'
    )
    if answer:
        text.delete(1.0, END)


root = Tk()

text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text='Open', command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text='Save', command=extract_text)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text='Delete', command=delete_text)
b3.grid(row=1, sticky=S)

root.mainloop()
