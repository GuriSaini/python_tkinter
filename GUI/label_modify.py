import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Modify label Text')

# add label
a_label = ttk.Label(root,text='Hello World')
a_label.grid(column=0,row=0)

#button click Event

def click_me():
    action.configure(text='I have been Clicked')
    a_label.configure(foreground= "red")
    a_label.configure(text='A Red LAbel')
action = ttk.Button(root,text='Click Me!', command=click_me)
action.grid(column=1,row=0)

root.mainloop()