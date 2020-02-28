import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Tab')

nb = ttk.Notebook(root)

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)

nb.add(page1,text ='one')
nb.add(page2,text='two')

# nb.pack(expend=True, fill = 'both')

label1 = ttk.Label(page1,text='This is page one')
label1.grid(row=0,column=0)

entry_box = ttk.Entry(page1, width = 27)
entry_box.grid(row=0,column=1)

root.mainloop()