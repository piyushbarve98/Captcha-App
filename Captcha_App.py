import random 
from tkinter import *
from tkinter import messagebox

text= 'ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstvxyz0123456789'
window =Tk()
window.title('Captcha App')
window.geometry('400x400')

Captcha= StringVar()
user_input= StringVar()

def set_captcha():
    s= random.choices(text,k=6)
    Captcha.set(''.join(s))

def check():
    
    if Captcha.get() == user_input.get():
        messagebox.showinfo('Success','Succesfull Captcha Submit!')
    else:
        messagebox.showerror('Incorrect','Incorrect Captcha Submit')
    set_captcha()

Label(window,textvariable=Captcha,font='Helvetica 16 bold').pack()
Label(window,text='Enter Captcha',font='Helvetica 16 bold').pack()
Entry(window,textvariable=user_input,font='Helvetica 12').pack(ipady=5)
Button(window,command=check,text='Check',font='Helvetica 14 ').pack()
set_captcha()
window.mainloop()