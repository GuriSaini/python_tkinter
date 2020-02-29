import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

root.title('Text Box')

def click_me():
    action.configure(text='Hi '+name_var.get() + select.get())


label=ttk.Label(text='Enter the name : ', width=15)
label.grid(column=1,row=1)
label1=ttk.Label(text='Select number ', width=15)
label1.grid(column=2,row=1)

#text box
name_var = tk.StringVar()
name = ttk.Entry(root,textvariable=name_var,width=14)
name.grid(column=1,row=2)
name.focus() #place cursor into text box

 #Combo Box
select = tk.StringVar()
number_chosen = ttk.Combobox(root,width=12,textvariable=select,state='readonly')
number_chosen['values'] = (1,2,54,66,33)
number_chosen.grid(column=2,row=2)
number_chosen.current(0)

#buttn
action = ttk.Button(text='Click me',width=10,command=click_me)
action.grid(column=3,row=5)
# action.configure(state='disable')  #disable button

root.mainloop()