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

gender_label = ttk.Label(root,text='Select Sex')
gender_label.grid(row=3,column=0,sticky=tk.W)

#create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=16, textvariable = name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var = tk.StringVar()
age_entrybox = ttk.Entry(root, width=16, textvariable = age_var)
age_entrybox.grid(row=1,column=1)

mail_var = tk.StringVar()
mail_entrybox = ttk.Entry(root, width=16, textvariable = mail_var)
mail_entrybox.grid(row=2,column=1)

#create comobox
gender_var =tk.StringVar()
gender_combobox = ttk.Combobox(root,width=16,textvariable = gender_var,state='readonly')
gender_combobox['values'] =('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

#radio button
usertype = tk.StringVar()
radio_btn1=ttk.Radiobutton(root,text='Student',value='Student',variable=usertype)
radio_btn1.grid(row=4,column=0)

radio_btn2=ttk.Radiobutton(root,text='Teacher',value='Teacher',variable=usertype)
radio_btn2.grid(row=4,column=1)

#check button
check_btn1_var = tk.IntVar()
check_btn1=ttk.Checkbutton(root, text='Check if you want',variable=check_btn1_var)
check_btn1.grid(row=5,columnspan=3)
#create button
def action():
    username=name_var.get()
    userage =age_var.get()
    email   =mail_var.get()
    sex    = gender_var.get()
    radio = usertype.get()
    if check_btn1_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    print(f'{username} is {userage} years old , {email},{sex},{radio},{subscribed}')
submit_button=ttk.Button(root, text='Submit', command=action)
submit_button.grid(row=6,column=1)

root.mainloop()