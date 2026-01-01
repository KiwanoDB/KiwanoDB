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
        #SETTINGS
        filemenu.add_command(label="Change Database", command=None) #Change DataBase
        filemenu.add_command(label="Other", command=Settings) #other
        filemenu.add_separator()
        filemenu.add_command("V0.1 Alpha", command=None) #V0.1 Alpha
         #TABLE
        tablemenu.add_command(label="Create New, command=None)
        tablemenu.add_separator()
        tablemenu.add_command(label="Insert Row", command=None)
        tablemenu.add_command(label="Edit Row", command=None)
        tablemenu.add_command(label="Delete Row", command=None)
        tablemenu.add_separator()
        tablemenu.add_command(label="Edit Table", command=None)
        tablemenu.add_separator()
        tablemenu.add_command("Delete Table", command=None)
        
        menu.add_cascade(label="Settings", menu=filemenu)
        menu.add_cascade(label="Table", menu=tablemenu)
        helpmenu = tk.Menu(menu, tearoff=0, bg=Colour1, fg=Colour3)
        helpmenu.add_command(label="Help", command=None)
        menu.add_cascade(label="Docummentation", menu=helpmenu)
    menu = tk.Menu(homepage)

    CreateMenu()
    homepage.config(menu=menu)
    def test(self):
        print("beans")

root = tk.Tk()
root.withdraw()

#lang = []
colour = ""
e = open("DATA.txt", "a")
e.close()
with open("DATA.txt") as f:
    Settings2 = False
    while Settings2 == False:
        with open("DATA.txt", "r") as f:
            settingsload = f.read()
        print("test")
        if settingsload == "":
            import NewUser
        else:

            Settings2 = True
            sett = settingsload.split("/")
            print(sett)
            try:
                if sett[1] == "TEAL":
                    Colour1="#353535"
                    Colour2="#354f52"
                    Colour3="#ffffff"
                    Colour4="#22333b"
                elif sett[1] == "WHITE":
                    Colour1="#ffffff"
                    Colour2="#ffffff"
                    Colour3="#000000"
                    Colour4="#ffffff"
                elif sett[1] == "PINK":
                    
                    Colour1="#ff0a54"
                    Colour2="#ff477e"
                    Colour3="#ffffff"
                    Colour4="#ff477e"
                else:
                    print("X")

            except Exception as err:
                if err == "list index out of range":
                    tkinter.messagebox.showerror(title="ERROR", message="Error 100 \n Data Files corrupted")
                    os.remove("DATA.txt")
                    root.destroy()
                    sys.exit()
                else:
                    print(err)

            pro()
root.mainloop()
#Threader = Threader()

