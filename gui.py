from tkinter import *
w=Tk()
w.title("gui")
w.resizable(False,False)
w.geometry("600x400")
w.configure(bg="blue")
l=Label(text="hello")
l.pack()
e = Entry()
e.pack()
b = Button(text="submit")
b.pack()
def msg():
    lab=Label(text=e.get())
    lab.pack()
b=Button(text="submit",command=msg)
b.pack()

w.mainloop()
