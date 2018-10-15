from tkinter import *

root = Tk()

def leftClic(event):
    print("left")

def middleClick(event):
    print("Middle")

def rightClick(event):
    print("Right")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClic)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root.mainloop()