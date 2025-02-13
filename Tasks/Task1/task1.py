from tkinter import *

root = Tk()

def save_text():
    file = en.get()
    save_txt = text.get('1.0', 'end-1c')
    file2 = open(file, 'w')
    file2.write(save_txt)

def open_file():
    file = en.get()
    file2 = open(file, 'r')
    text.insert(END, file2.read())


f_top = Frame()

en = Entry(f_top)
but1 = Button(f_top, text='Открыть', command=open_file)
but2 = Button(f_top, text='Сохранить', command=save_text)
text = Text(width=50, height=10, wrap='none')
scrollY = Scrollbar(orient='vertical', command=text.yview)
scrollY.grid(column=1, row=1, sticky=NS)
scrollX = Scrollbar(orient='horizontal', command=text.xview)
scrollX.grid(column=0, row=2, sticky=EW)

text['yscrollcommand'] = scrollY.set
text['xscrollcommand'] = scrollX.set
f_top.grid(column=0, row=0)
en.grid(column=1, row=0)
but1.grid(column=2, row=0)
but2.grid(column=3, row=0)
text.grid(column=0, row=1)

root.mainloop()
