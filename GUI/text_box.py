import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Text Box')

def click_me():
    action.configure(text='Hi '+name_var.get())


label=ttk.Label(text='Enter the name : ', width=15)
label.grid(column=2,row=1)

#text box
name_var = tk.StringVar()
name = ttk.Entry(root,textvariable=name_var,width=16)
name.grid(column=3,row=1)

#buttn
action = ttk.Button(text='Click me',width=10,command=click_me)
action.grid(column=3,row=5)

root.mainloop()