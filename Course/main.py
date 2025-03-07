from tkinter import *

root = Tk()
root.geometry('250x200')

Entry().grid(column=0, row=0) # Логин
Entry().grid(column=1, row=0) # Пароль
Button(text='Войти').grid(column=2, row=0) # Кнопка войти
Button(text='Зарегистрироваться').grid(column=3, row=0) # Кнопка зарегистрироваться

# Поле для поиска
Entry().grid(column=0, row=1)
Button(text='Ок').grid(column=1, row=1)

root.mainloop()
