import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('GUI APP')
#pack #grid

#creates labels
#widgets --> labelsn,button radio button - tk, ttk
name_label=ttk.Label(root, text='Enter your name')
name_label.grid(row=0,column=0,sticky=tk.W)

age_label = ttk.Label(root, text='Enter your age')
age_label.grid(row=1,column=0,sticky=tk.W)

email_label = ttk.Label(root, text='Enter your E-mail')
email_label.grid(row=2,column=0,sticky=tk.W)

#create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=16, textvariable = name_var)
name_entrybox.grid(row=0,column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(root, width=16, textvariable = age_var)
age_entrybox.grid(row=1,column=1)

mail_var = tk.StringVar()
mail_entrybox = ttk.Entry(root, width=16, textvariable = mail_var)
mail_entrybox.grid(row=2,column=1)

#create button
def action():
    username=name_var.get()
    userage =age_var.get()
    email   =mail_var.get()
    print(f'{username} is {userage} years old , {email}')
submit_button=ttk.Button(root, text='Submit', command=action)
submit_button.grid(row=3,column=1)

root.mainloop()