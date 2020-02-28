import tkinter 
from tkinter import ttk

root = tkinter.Tk()
root.title('Tab')

nb = ttk.Notebook(root)
nb.pack(side = 'left')
page1 = tkinter.Frame(nb)
nb.add(page1,text ='one',padding=10)
page2 = tkinter.Frame(nb)

nb.add(page2,text='two')
nb.select(page2)
nb.enable_traversal()


root.mainloop()