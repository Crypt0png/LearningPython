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
    Entry().pack()
    Entry().pack()
    Button().pack()
    exit_but = Button(reg, text='Вернуться', command=back_button)
    exit_but.pack()


root = Tk()
root.title('Главное окно')
root.geometry('250x250')

# Login/Registration block
login = Frame()
search = Frame()
login.pack(anchor='ne')
search.pack(anchor='center')

Button(login, text='Регистрация', command=reg_window).pack(side='right')
Button(login, text='Войти').pack(side='right')
Entry(login).pack(side='right')
Entry(login).pack(side='right')

# Search block
Entry(search).pack(pady=20)
Button(search, text='Ок').pack()

root.mainloop()
