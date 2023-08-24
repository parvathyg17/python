import tkinter
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
image1=Image.open("images\ka.jpg")
image1=image1.resize((25,50),Image.ANTIALIAS)
test=ImageTk.PhotoImage(image1)


label = tkinter.Label(image=test)
label.image=test

label.place(x=15,y=8)
root.mainloop()
