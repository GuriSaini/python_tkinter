import tkinter as tk 
from tkinter import ttk

root =tk.Tk()
root.title('Using loop crate Gui')

labels = ['Enter your Name','Enter your number']

for i in range(len(labels)):
    cur_label = 'label' +str(i)
    cur_label = ttk.Label(root, text=labels[i])
    cur_label.grid(row=i,column=0,sticky=tk.W)

#Entry Box
entry_box = {
    'name' : tk.StringVar(),
    'number' : tk.StringVar()
}
counter = 0
for i in entry_box:
    cur_entrybox = 'entry' + i
    cur_entrybox = ttk.Entry(root,width=16,textvariable=entry_box[i])
    cur_entrybox.grid(row=counter,column=1)
    counter = counter+1

def submit():
    print(entry_box['name'].get())
    print(entry_box['number'].get())

submit_btn = ttk.Button(root,text='submit',command=submit)
submit_btn.grid(row=6, column=2)
root.mainloop()