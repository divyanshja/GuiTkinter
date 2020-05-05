import tkinter 
from tkinter import *

a_root = Tk()

#geometry

a_root.geometry("455x200")

#we can set min and max size of layout gui

a_root.minsize(200,100)

a_root.maxsize(1200,990)

b = Label(text="Hello guys my name is divyansh jain")
b.pack()


a_root.mainloop()


