from tkinter import *
from tkinter import filedialog as fd

def insert_text():
    file_name = fd.askopenfilename(
        filetypes=(('TXT files', '*.txt'),
                   ('HTML files', '*.html')
                   ('ALL files', '*.*')))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
root = Tk()

root.mainloop()
