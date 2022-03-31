from asyncio.windows_events import NULL
from tabnanny import check
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import bgcolor, circle
from webbrowser import BackgroundBrowser
from DbConnect import DBConnect
from  orders import  ListTickect
from datetime import datetime #date & time
# import reset
from reset import *

class fun:
   def function():     
    dbconnect=DBConnect()




    root=Tk()
    #  root.grid_rowconfigure(0, weight=1)
    #  root.grid_columnconfigure(0, weight=1)
    root.configure(background="#012b65")
    root.geometry("1050x700")

    root.title("Ticket reservation")
    style=ttk.Style()

    #  themes #####('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

    img_l=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UIreserve\img\hotll.png")
    lbl_back=Label(root,image=img_l)    # height=40,width=40
    lbl_back.place(x=560,y=190)
    # style.theme_use("default")

    style.theme_use("clam")
    # style.configure("TButton",background="#0156ce")
    style.configure("TLabel",background="#0156ce",foreground="#f1f1f1",font=("serif",12))
    style.configure("TRadiobutton",background="#012b65", foreground="#F1F1F1",font=("arial",10))

    style.configure("TButton",background="#80aaff",forground="#f1f1f1",font=("sans-serif",14),)
    style.configure("TEntry",background="#F1F1F1", foreground="#323232",font=("arial",10))

    #first row
    ttk.Label(root,text="first name").grid(row=0,column=0,padx=10,pady=10,)
    e1=ttk.Entry(root,width=30,font=("arial",16))
    e1.grid(row=0,column=1,columnspan=2,pady=20)    #pad is margin ipad is padding

    #first row
    ttk.Label(root,text="last name").grid(row=0,column=3,padx=10,pady=10)
    ee=ttk.Entry(root,width=30,font=("arial",16))
    ee.grid(row=0,column=4,columnspan=2,pady=20,)    #pad is margin ipad is padding

    #second row
    ttk.Label(root,text="phone number").grid(row=1,column=0,padx=10,pady=10)
    eph=ttk.Entry(root,width=30,font=("arial",16))
    eph.grid(row=1,column=1,columnspan=2,pady=20)    #pad is margin ipad is padding
    #second row
    ttk.Label(root,text="nationality").grid(row=1,column=3,padx=10,pady=10)
    en=ttk.Entry(root,width=30,background="#f2f2f2", foreground="#323232",font=("arial",16))
    en.grid(row=1,column=4,columnspan=2,pady=20)    #pad is margin ipad is padding

    #3rd row
    ttk.Label(root,text=" gender").grid(row=2,column=0,padx=10,pady=10)
    val=StringVar()
    male=ttk.Radiobutton(root,text="male",value="male",variable=val).grid(column=1,row=2 )
    female=ttk.Radiobutton(root,text="female",value="female",variable=val).grid(column=2,row=2)

    #third row
    ttk.Label(root,text=" comments").grid(row=3,column=0,padx=10,pady=10)
    c=Text(root,width=30,height=12,background="#f2f2f2", foreground="#323232",font=("arial",16))
    c.grid(column=1,row=3,columnspan=2)

    #fourth column

    b1=ttk.Button(root,text="submit")
    b1.grid(row=4,column=3,pady=10)
    b2=ttk.Button(root,text="Liste reserved" )

    # b2.config(style(background="#80aaff",forground="#f1f1f1"))
    b2.grid(row=4,column=2, pady=10,)


    def busaveliste():
        print("first name:{}".format(e1.get()))
        print("last name:{}".format(ee.get()))
        print("date of birth:{}".format(eph.get()))
        print("nationality:{}".format(en.get()))



        
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M")

        print(dt_string)
        print("gender:{}".format(val.get()))
        print("comments:{}".format(c.get(1.0,"end")))
        if(e1.get() and ee.get() and eph.get() and en.get()  )!="":
            msg=dbconnect.Add(e1.get(),ee.get(),dt_string,eph.get(),en.get(),val.get(),c.get(1.0,"end"))
            messagebox.showinfo(title="add info",message=msg)
            e1.delete(0,"end")
            c.delete(1.0,"end")
            ee.delete(0,"end")
            eph.delete(0,"end")
            en.delete(0,"end")

    def Listes():
        print("not implemented yet ")
        listerequeste=ListTickect()
    b1.config(command=busaveliste)
    b2.config(command=Listes)
    ################################  reset pass
    img_s=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UIreserve\img\zzz.png")
    lbl_backss=Label(root,image=img_s)    # height=40,width=40
    lbl_backss.place(x=1000,y=20)
    def resetup(e):
        print ("he click on image")
        root.withdraw()
        resetPass.resetPassword()
    ###                                       #######################""
    lbl_backss.bind('<Button>',resetup)


    ###  remove bg form radio button 

    # def removeBg(e):
    #     print ("he hovered on radio")

    # male.bind('<Button>',removeBg)
    # female.bind('<Button>',removeBg)


    root.mainloop()

