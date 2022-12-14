from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random

win = ThemedTk(theme='azure')
win.geometry("1200x850")

def creatPassword():

    passwords = ''
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*-_=+/?<>()[]'

    amount = int(a.get())
    lenght = int(b.get())
    maxAmount = 25
    maxLenght = 120

    if(amount > maxAmount):
        label.config(text="ERROR = Max passwords: "+ str(maxAmount))
    elif(lenght > maxLenght):
        label.config(text="ERROR = Max lenght per password: "+ str(maxLenght))
    else:
        for pwd in range(amount):
            for c in range(lenght):
                passwords += random.choice(chars)
                label.config(text="Your passwords: \n"+passwords)
            passwords += '\n'
        
    w = Text(win, height=15, font=('sora', 12,'bold'))
    w = Text(win, height=1, borderwidth=0)
    w.pack(fill=BOTH, expand=1)
    w.configure(state="disabled")
    w.configure(inactiveselectbackground=w.cget("selectbackground"))
    w.insert(1.0, passwords)

label = ttk.Label(win, text="Password amount:", font=('sora 12')).pack()
a = ttk.Entry(win, width=30)
a.pack()

label = ttk.Label(win, text="Password lengh:", font=('sora 12')).pack()
b = ttk.Entry(win, width=35)
b.pack()

label = ttk.Label(win, text="Your passwords:", font=('sora 10'))
label.pack(pady=20)

button = ttk.Button(win, text="Generate passwords", command=creatPassword).pack()

win.mainloop()