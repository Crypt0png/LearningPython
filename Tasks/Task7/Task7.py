from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno, showerror


def clear_text():
    ans = askyesno(title='Подтверждение действия', message='Вы уверены что хотите очистить текстовое поле?')
    if ans is True:
        text.delete('1.0', END)

def open_file():
    filepath = askopenfilename()
    if filepath != "":
        file = open(filepath, 'r')
        saved_text = file.read()
        text.delete('1.0', END)
        text.insert('1.0', saved_text)
    else:
        showerror(title='Ошибка открытия файла!', message='Введите правильное имя или путь к файлу.')

def save_file():
    filepath = asksaveasfilename()
    if filepath != "":
        saved_text = text.get('1.0', END)
        file = open(filepath, 'w')
        file.write(saved_text)
    else:
        showerror(title='Ошибка записи!', message='Укажите место куда нужно сохранить файл, а также его название.')

def left_click(event):
    context_menu.tk_popup(event.x_root, event.y_root)


root = Tk()

main_menu = Menu(tearoff=0)
main_menu.add_command(label='Открыть', command=open_file)
main_menu.add_command(label='Сохранить', command=save_file)

context_menu = Menu(tearoff=0)
context_menu.add_command(label='Очистить', command=clear_text)

text = Text()
text.pack()
text.bind("<Button-3>", left_click)

root.config(menu=main_menu)
root.mainloop()
