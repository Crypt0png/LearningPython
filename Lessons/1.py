import tkinter as tk

root = tk.Tk()

root.title('Калькулятор')

root.geometry("250x250")

frame=tk.Frame(root)
frame.pack(expand=True)

label1=tk.Label(frame, text="Name")
label1.grid(row=0,column=0)

entry1=tk.Entry(frame)
entry1.grid(row=0,column=1)

label2=tk.Label(frame, text='Email')
label2.grid(row=1,column=0)

entry2=tk.Entry(frame)
entry2.grid(row=1, column=1)

button1=tk.Button(frame, text='Send')
button1.grid(row=2,column=1)

root.update_idletasks()

width=root.winfo_width()
height=root.winfo_height()

x = (root.winfo_screenheight() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root.mainloop()