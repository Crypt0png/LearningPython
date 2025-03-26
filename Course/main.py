from tkinter import *

# Placeholders for future functions
# def login():
# def search():

def reg_window():
    def back_button():
        reg.destroy()

    reg = Toplevel()
    reg.geometry('250x250')
    reg.title('Регистрация')

    log = Frame(reg)
    passw = Frame(reg)
    log.pack()
    passw.pack()
    Label(log, text='Логин:').pack()
    login = Entry(log)
    login.pack()

    Label(passw, text='Пароль:').pack()
    password = Entry(passw)
    password.pack()

    Button(reg, text='Зарегистрироваться').pack()
    Button(reg, text='Вернуться', command=back_button).pack()


root = Tk()
root.title('Главное окно')
root.geometry('400x250')

# Login/Registration block
login = Frame()
login.pack(anchor='ne')

Button(login, text='Регистрация', command=reg_window).pack(side='right')
Button(login, text='Войти').pack(side='right')
Entry(login).pack(side='right')
Entry(login).pack(side='right')

# Search block
search = Frame()
search.pack(anchor='center', pady=60)

Entry(search).pack()
Button(search, text='Ок').pack()

root.mainloop()
