#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("RixTix")

def time():
	string = strftime('%I:%M:%S %p')
	label.config(text=string)
	label.after(1000, time)

label = Label(root, font=("DS-Digital", 30), background = "black", foreground = "cyan")
label.pack(anchor='center')

time()

mainloop()
