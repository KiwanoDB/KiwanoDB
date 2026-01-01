from tkinter import *
from tkinter import ttk
import os

import tkinter.messagebox
import tkinter as tk
import sys
def tealhome():
    with open("DATA.txt", "a") as f:
        f.write(f"/TEAL")
    root.destroy()
    tkinter.messagebox.showinfo(title="Notice", message="Please Rerun the program to start operating")
    sys.exit()
def whitehome():
    with open("DATA.txt", "a") as f:
        f.write(f"/WHITE")
    root.destroy()
    tkinter.messagebox.showinfo(title="Notice", message="Please Rerun the program to start operating")
    sys.exit()
def pinkhome():
    with open("DATA.txt", "a") as f:
        f.write(f"/PINK")
    root.destroy()
    tkinter.messagebox.showinfo(title="Notice", message="Please Rerun the program to start operating")
    sys.exit()
def login():
    login = tk.Toplevel(root)
    login.geometry("360x100")
    welcome= tk.Label(login, text="Welcome to visonaryDB, please choose your background colour")
    welcome.place(x=15, y=10)

    Choice1=tk.Button(login, text="teal", command=tealhome, bg="#03045e", fg="#ffffff").place(x=100,y=50)
    Choice1=tk.Button(login, text="pink", command=pinkhome, bg="#ff0a54", fg="#ffffff").place(x=200,y=50)

    Choice1=tk.Button(login, text="White", command=whitehome).place(x=150,y=50)

def NewAccount():
    P = 0
    CreateNew = tk.Toplevel(root)
    CreateNew.geometry("300x150")
    Label = tk.Label(CreateNew, text="Welcome")
    Label.place(x=50,y=20)
    Label.config(text="Welcome", font=("Century Gothic", 18, "bold"))
    a = ["English"]
    cb = ttk.Combobox(CreateNew, values=a, font=(None, 12))
    cb.set("Select a language")
    def Redirect():
        global lang
        opt = f"{cb.get()}".lower()
        with open("DATA.txt", "a") as f:
          f.write(f"{opt}")
        print(opt)
        try:
            txt = open(f"lang/{opt}.txt", "r")
        except Exception:
            tkinter.messagebox.showerror(title="ERROR", message=Exception)
        fish = txt.read()
        lang = fish.split("/")
        print(lang)
        CreateNew.destroy()
        login()
    selection = tk.Button(CreateNew, text="Done", command=Redirect, ).place(x=240,y=104)
    cb.place(x=20,y=105)
root = tk.Tk()
root.withdraw()
NewAccount()
root.mainloop()
