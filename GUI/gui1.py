import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Gui 1')

#root.resizable(False,True)

# create label
ttk.Label(root,text='A label').grid(row=0,column=0)


root.mainloop()