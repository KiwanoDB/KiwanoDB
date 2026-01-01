from tkinter import *
from tkinter import ttk
import os

import tkinter.messagebox
import tkinter as tk
import sys
var = 0
Colour1="#"
Colour2="#"
Colour3="#"
Colour4="#"
#txt = open("lang\english.txt", "r")
#fish = txt.read()
#lang = fish.split("/")
#print(fish)
#print(txt)
def Settings():
    def warning():
        tkinter.messagebox.WARNING = 'warning'
        tkinter.messagebox.YES = 'yes'
        tkinter.messagebox.NO = 'no'
        tkinter.messagebox.askyesno(title="ATTENTION", message="You will lose all of your data", icon='warning')
        if tkinter.messagebox.YES:
            os.remove("DATA.txt")
            root.destroy()
            sys.exit()
    settings = tk.Toplevel(root)
    settings.geometry("400x300")
    Title = Label(settings, text="Settings", font=("century gothic", 10, "bold")).place(x=10,y=10)

    Reset_DataButton = Button(settings, text="Reset Data", font=("century gothic", 10, "bold"), fg="red", command=warning).place(x=10,y=260)
def pro():
    global lang
    homepage=tk.Toplevel(root)
    homepage.geometry("1000x650")
    homepage.configure(bg=Colour4)
    def CreateMenu():
        filemenu = tk.Menu(menu, tearoff=0, bg=Colour1, fg=Colour3)
        tablemenu = tk.Menu(menu, tearoff=0, bg=Colour1, fg=Colour3)

        filemenu.add_command(label=lang[0], command=None)
        filemenu.add_command(label=lang[1], command=Settings)
        filemenu.add_separator()
        filemenu.add_command(label=lang[2], command=None)
         
        tablemenu.add_command(label=lang[3], command=None)
        tablemenu.add_separator()
        tablemenu.add_command(label=lang[4], command=None)
        tablemenu.add_command(label=lang[5], command=None)
        tablemenu.add_command(label=lang[6], command=None)
        tablemenu.add_separator()
        tablemenu.add_command(label=lang[7], command=None)
        tablemenu.add_separator()
        tablemenu.add_command(label=lang[8], command=None)
        
        menu.add_cascade(label=lang[9], menu=filemenu)
        menu.add_cascade(label=lang[10], menu=tablemenu)
        helpmenu = tk.Menu(menu, tearoff=0, bg=Colour1, fg=Colour3)
        helpmenu.add_command(label=lang[11], command=None)
        menu.add_cascade(label=lang[12], menu=helpmenu)
    menu = tk.Menu(homepage)

    CreateMenu()
    homepage.config(menu=menu)
    def test(self):
        print("beans")
def login():
    login = tk.Toplevel(root)
    login.geometry("360x100")
    welcome= tk.Label(login, text="Welcome to visonaryDB, please choose your background colour")
    welcome.place(x=15, y=10)

    Choice1=tk.Button(login, text="teal", command=tealhome, bg="#03045e", fg="#ffffff").place(x=100,y=50)
    Choice1=tk.Button(login, text="pink", command=pinkhome, bg="#ff0a54", fg="#ffffff").place(x=200,y=50)

    Choice1=tk.Button(login, text="White", command=whitehome).place(x=150,y=50)
def tealhome():
    global Colour1, Colour2, Colour3, Colour4
    Colour1="#353535"
    Colour2="#354f52"
    Colour3="#ffffff"
    Colour4="#22333b"
    with open("DATA.txt", "a") as f:
        f.write(f"/TEAL")
    pro()
def whitehome():
    global Colour1, Colour2, Colour3, Colour4
    Colour1="#ffffff"
    Colour2="#ffffff"
    Colour3="#000000"
    Colour4="#ffffff"
    with open("DATA.txt", "a") as f:
        f.write(f"/WHITE")
    pro()
def pinkhome():
    global Colour1, Colour2, Colour3, Colour4
    Colour1="#ff0a54"
    Colour2="#ff477e"
    Colour3="#ffffff"
    Colour4="#ff477e"
    with open("DATA.txt", "a") as f:
        f.write(f"/PINK")
    pro()


def NewAccount():
    P = 0
    CreateNew = tk.Toplevel(root)
    CreateNew.geometry("300x150")
    Label = tk.Label(CreateNew, text="Welcome")
    Label.place(x=50,y=20)
    Label.config(text="Welcome", font=("Century Gothic", 18, "bold"))
    a = ["English", "French", "Norwegian", "irish", "spanish", "german", "swedish", "finnish"]
    cb = ttk.Combobox(CreateNew, values=a, font=(None, 12))
    cb.set("Select a language")
    def Redirect():
        global lang
        opt = f"{cb.get()}".lower()
        with open("DATA.txt", "a") as f:
          f.write(f"{opt}")
        print(opt)
        try:
            txt = open(f"lang\{opt}.txt", "r")
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
#lang = []
colour = ""
e = open("DATA.txt", "a")
e.close()
with open("DATA.txt") as f:
    settingsload = f.read()
    if settingsload == "":
        NewAccount()
    else:
        set = settingsload.split("/")
        print(set)
        try:
            if set[1] == "TEAL":
                Colour1="#353535"
                Colour2="#354f52"
                Colour3="#ffffff"
                Colour4="#22333b"
            elif set[1] == "PINK":
                Colour1="#ffffff"
                Colour2="#ffffff"
                Colour3="#000000"
                Colour4="#ffffff"
            elif set[1] == "WHITE":
                
                Colour1="#ff0a54"
                Colour2="#ff477e"
                Colour3="#ffffff"
                Colour4="#ff477e"
            else:
                print("X")
        except Exception as err:
            tkinter.messagebox.showerror(title="ERROR", message=err)
        if set[0] == "english":
            txt = open(f"lang\english.txt", "r")
            fish = txt.read()
            lang = fish.split("/")
        if set[0] == "german":
            txt = open(f"lang\german.txt", "r")
            fish = txt.read()
            lang = fish.split("/")
        if set[0] == "irish":
            txt = open(f"lang\irish.txt", "r")
            fish = txt.read()
            lang = fish.split("/")
        if set[0] == "spanish":
            txt = open(f"lang\spanish.txt", "r")
            fish = txt.read()
            lang = fish.split("/")
        if set[0] == "swedish":
            txt = open(f"lang\swedish.txt", "r")
            fish = txt.read()
            lang = fish.split("/")

        pro()
#Threader = Threader()

