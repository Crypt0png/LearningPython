from tkinter import *

root = Tk()

def event_leave(event):
    if event.type == '7':
        event.widget['text'] = 'In'
    elif event.type == '8':
        event.widget['text'] = 'Out'


lab1 = Label(width=20, height=3, bg='white')
lab1.pack()
lab1.bind('<Enter>', event_leave)
lab1.bind('<Leave>', event_leave)

lab2 = Label(width=20, height=3, bg='black', fg='white')
lab2.pack()
lab2.bind('<Enter>', event_leave)
lab2.bind('<Leave>', event_leave)