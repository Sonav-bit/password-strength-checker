from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Password strength')
root.geometry('400x400')

l1=Label(root,text='Enter your password')
e1=Entry(root)
def pw():
    pw=e1.get()
    if pw.__len__()>10:
        l4=Label(root,text='You have a Strong password')
        l4.grid(row=3,column=2)
    elif pw.__len__()<10:
        l5=Label(root,text='You have a Weak password')
        l5.grid(row=3,column=2)

b1=Button(root,text='Click me',command=pw)

l1.grid(row=0,column=1)
e1.grid(row=1,column=1)
b1.grid(row=2,column=1)
root.mainloop()
