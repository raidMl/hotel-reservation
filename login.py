from hashlib import new
from numbers import Number
from time import time
from tkinter import font, ttk
from tkinter import *
from turtle import circle
from webbrowser import BackgroundBrowser
from controle import *
import logindb
from tkinter import messagebox
import sqlite3
from reset import *


root=Tk()
dbconect=DBConnectUser()
all=dbconect.ShowUsers()
for row in all:
 user=row["name"]
 mdpass=row["password"]
print(user,mdpass)
# user="raid"
# mdpass="ess"

# root.grid_rowconfigure(0, weight=1)
# root.grid_columnconfigure(0, weight=1)
# root.configure(background="#0156ce")
# root.configure(background="#1565c0")
root.configure(background="#1f66ad")


varn=StringVar()
varp=StringVar()

style=ttk.Style()
root.title("Ticket reservation")


root.geometry("700x500")

    #  themes #####('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use("default")
style.configure("TButton",background="#80aaff",forground="#f1f1f1",font=("sans-serif",14),)
style.configure("TLabel",background="#0156ce",foreground="#f1f1f1",font=("arial",12))
style.configure("TEntry",background="#F1F1F1", foreground="#323232",font=("arial",10))

img_l=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UiReserve\img\ahot.png")
lbl_back=Label(root,image=img_l)    # height=40,width=40
lbl_back.place(x=300,y=30)

# img_s=PhotoImage(file=r"C:\Users\r_dev\Documents\ui reserve\img\zzz.png")
# lbl_backss=Label(root,image=img_s)    # height=40,width=40
# lbl_backss.place(x=660,y=30)
# lbl_backss.grid(row=0,column=3,padx=0)

img_l1=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UIreserve\img\us.png")
lbl_back1=Label(root,image=img_l1,foreground="#000000")    # height=40,width=40
lbl_back1.place(x=20,y=150)

img_l2=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UIreserve\img\ps.png")

lbl_back2=Label(root,image=img_l2,  borderwidth =2,)    # height=40,width=40
lbl_back2.place(x=20,y=210)

ttk.Label(root,text="R hotels",background="#3A53F7",font=("comic sans ms",14)).grid(row=0,column=2,padx=150,pady=50)


#first row
ttk.Label(root,text="user").grid(row=1,column=1,padx=70,pady=10)
name=ttk.Entry(root,width=30,font=("arial",16),textvariable=varn)
name.grid(row=1,column=2,columnspan=2,pady=20)    #pad is margin ipad is padding


#second row
ttk.Label(root,text="password").grid(row=2,column=1,padx=70,pady=10)
password=ttk.Entry(root,width=30,font=("arial",16),show="*",textvariable=varp)
password.grid(row=2,column=2,columnspan=2,pady=20)

lbl_text = Label(root,bg="#1f66ad",text="")
# lbl_text.grid(row=4,column=2, columnspan=2)
lbl_text.place(x=270,y=320)


b1=ttk.Button(root,text="log in") #fg bg activebackground="blue"
b1.grid(row=3,column=2,pady=10,padx=150)

def try_login():
 if varn.get() == "" or varp.get() == "":
        lbl_text.config(text="Please complete the required field!",background="#2b2b2b", fg="#FF2247",font=("serif",14))
 elif(varn.get()==user and varp.get()==mdpass):
     #root.withdraw() #for hide window
     lbl_text.config(text="Log in success", fg="green",font=("serif",14))
     root.destroy()  #for delete window
     fun1=fun.function()

 else: 
     lbl_text.config(text="error: Invalid username or password",background="#2b2b2b",fg="#FF2247",font=("serif",14))
     varn.set("")
     varp.set("")

     
    #  x = datetime.now()
    #  a=int(x.strftime("%S")) #convert to int 
    #  b=str(a+5)                   #convert to string
    #  y=True
    #  while(y):
    #   if(x.strftime("%S")==b):
    #           lbl_text.config(text="",fg="#FF2247",font=("serif",14))
    #           y=False
    #   x = datetime.now()
    #   a=int(x.strftime("%S")) #convert to int 
    #   b=str(a+5)      
    # 
    # 
    #  
    #  print(a)
    #  print(x.strftime("%S"))
    #  print(b)

    #  print(x.strftime("%"+S+10))




# def enter(e):
#     print("hello word")
#     b1.config(bg="black")
# def leave(e):
#     b1.config(bg="red")
#     print("you leave it")
 
b1.config(command=try_login)    # COMMAND=root.quit   for quit window
# b1.bind('<Enter>',enter)   #<ButtonPress>
# b1.bind('<Leave>',leave)


# from datetime import date #for use date
# from datetime import datetime #date & time


# # today = date.today()
# # print("Today's date:", today)
# # dd/mm/YY

# today = date.today()
# now=datetime.now()
# # d1 = today.strftime("%d/%m/%Y")
# # print("d1 =", d1)

# dt_string = now.strftime("%d/%m/%Y %H:%M")
# print(dt_string)

root.mainloop()
