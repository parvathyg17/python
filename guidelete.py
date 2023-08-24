import tkinter as tk
def destroywindow():
    root.destroy()
root=tk.Tk()
root.title("Destroy window example")
label=tk.Label(root,text="kukkumon",font=('Times New Roman','80'),fg="black",bg="white")
label.pack(padx=20,pady=20)
destroy_button=tk.Button(root,text="Close",command=destroywindow)
destroy_button.pack()
root.mainloop()