
from tkinter import *

root =Tk()
root.geometry("655x333")

def add():
    print("This is for addition")

def sub():
    print("This is for sub")
    
def mul():
    print("This is for mul")

def div():
    print("This is for div")    
    

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="ADD", command=add)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="SUB", command=sub)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="MUL",command=mul)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="DIV",command=div)
b4.pack(side=LEFT, padx=23,fill=X)
root.mainloop()
