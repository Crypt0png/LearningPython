from tkinter import *

# def login():

# def search():

root = Tk()

login = Frame()
search = Frame()
login.pack(anchor="ne")
search.pack(anchor='center')

Button(login, text='Регистрация').pack(side='right') # Кнопка регистрации
Button(login, text='Войти').pack(side='right') # Кнопка войти
Entry(login).pack(side='right') # Логин
Entry(login).pack(side='right') # Пароль

# Поле для поиска
Entry(search).pack()
Button(search, text='Ок').pack()

root.mainloop()
