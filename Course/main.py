from tkinter import *
# Placeholders for future functions
# def login():
# def search():

class Login(Tk):
    def __init__(self):
        super().__init__()

        self.title('Регистрация')

        self.entry()
        self.exit_but = Button(self, text='Вернуться')
        self.exit_but['command'] = self.back_button
        self.button.pack()

        Login.grab_set()
    def back_button(self):
        self.destroy()


root = Tk()
root.title('Главное окно')

login = Frame()
search = Frame()
login.pack(anchor="ne")
search.pack(anchor='center')

# Login/Registration block
Button(login, text='Регистрация').pack(side='right')
Button(login, text='Войти').pack(side='right')
Entry(login).pack(side='right')
Entry(login).pack(side='right')

# Placeholder for search
Entry(search).pack()
Button(search, text='Ок').pack()

root.mainloop()
