from tkinter import *
root = Tk()
w = Label(root,text="red",bg="red",fg="white")
w.pack(padx=5,pady=10,side=LEFT)
w = Label(root,text="red",bg="blue",fg="white")
w.pack(padx=5,pady=10,side=LEFT)
w = Label(root,text="red",bg="green",fg="white")
w.pack(padx=5,pady=10,side=LEFT)
mainloop()