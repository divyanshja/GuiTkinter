import tkinter
from tkinter import *

#Tkinter not allowwed jpeg image for that we install pillow package.
from PIL import Image, ImageTk

a_root = Tk()

a_root.geometry("1200x800")

#To show the label in the gui we have to pack it.

photo = ImageTk.PhotoImage(file="1.jpeg")

b = Label(image = photo)

b.pack()

a_root.mainloop()



