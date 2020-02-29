import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext

root = tk.Tk()
root.title('Scroll Text Widget')

scrol_w = 30
scrol_h = 3
one = tk.StringVar()
scr = scrolledtext.ScrolledText(root,width=scrol_w,height=scrol_h,wrap=tk.WORD)
scr.grid(column=1,row=1)

root.mainloop()

