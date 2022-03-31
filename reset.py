from os import unlink
from tkinter import font, ttk
from tkinter import *
import tkinter
from controle import *
from tkinter import messagebox
from logindb import *
import sqlite3
class resetPass:
  def resetPassword(): 
      dbconect=DBConnectUser()
      # root=Tk()
      root=tkinter.Toplevel()

      # root.grid_rowconfigure(0, weight=1)
      # root.grid_columnconfigure(0, weight=1)
      root.configure(background="#0156ce")
     

      varn=StringVar()
      varnn=StringVar()
      varp=StringVar() 
      varnp=StringVar()
      style=ttk.Style()
      root.title("Ticket reservation")

      root.geometry("700x500")

      # style.theme_use("vista")
      # style.configure("TButton",background="#01014e",forground="black",font=("sans-serif",14))
      # style.configure("TLabel",background="#0156ce",foreground="white",font=("arial",12))

      style.theme_use("default")
      style.configure("TButton",background="#80aaff",forground="#f1f1f1",font=("sans-serif",14),)
      # style.configure("TLabel",background="#0156ce",foreground="#f1f1f1",font=("arial",12))
      style.configure("TLabel",background="#0156ce",foreground="#f1f1f1",font=("arial",12))

      style.configure("TEntry",background="#F1F1F1", foreground="#323232",font=("arial",10))


      img_l=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UiReserve\img\hh.png")
      lbl_img=Label(root,image=img_l)    # height=40,width=40
      lbl_img.place(x=300,y=50)

      # img_s=PhotoImage(file=r"C:\Users\r_dev\Desktop\ui reserve\img\zzz.png")
      # lbl_backss=Label(root,image=img_s)    # height=40,width=40
      # lbl_backss.place(x=660,y=30)
      # lbl_backss.grid(row=0,column=3,padx=0)

      img_l1=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UIreserve\img\us.png")
      lbl_back1=Label(root,image=img_l1)    # height=40,width=40
      lbl_back1.place(x=20,y=150)

      img_l2=PhotoImage(file=r"C:\Users\r_dev\Documents\py\UIreserve\img\ps.png")

      lbl_back2=Label(root,image=img_l2,  borderwidth =2,)    # height=40,width=40
      lbl_back2.place(x=20,y=210)

      ttk.Label(root,text="change password",background="#3A53F7",font=("comic sans ms",14)).grid(row=0,column=2,padx=150,pady=50)




      #first row 
      ttk.Label(root,text="user").grid(row=1,column=1,padx=70,pady=10)
      name=ttk.Entry(root,width=30,font=("arial",16),textvariable=varn)
      name.grid(row=1,column=2,columnspan=2,pady=20)    #pad is margin ipad is padding

      ttk.Label(root,text="password").grid(row=2,column=1,padx=70,pady=10)
      password=ttk.Entry(root,width=30,font=("arial",16),show="*",textvariable=varp)
      password.grid(row=2,column=2,columnspan=2,pady=20)

      ttk.Label(root,text="new username").grid(row=3,column=1,padx=70,pady=10)
      namen=ttk.Entry(root,width=30,font=("arial",16),textvariable=varnn)
      namen.grid(row=3,column=2,columnspan=2,pady=20)

      #second row
      ttk.Label(root,text="new password").grid(row=4,column=1,padx=70,pady=10)
      passwordn=ttk.Entry(root,width=30,font=("arial",16),show="*",textvariable=varnp)
      passwordn.grid(row=4,column=2,columnspan=2,pady=20)


      lbl_text = Label(root,background="#0156ce",text="")
      # lbl_text.grid(row=4,column=2, columnspan=2)
      lbl_text.place(x=320,y=390)


      b1=ttk.Button(root,text="save") #fg bg activebackground="blue"
      b1.grid(row=5,column=2,pady=10,padx=150)

      def try_change():
         
         # us=dbconect.GetUser()
         # pas=dbconect.GetPass()
         all=dbconect.ShowUsers()
         # us="raid"
         # pas="ess"
         for row in all:
          us=row["name"]
          pas=row["password"]

         print(us,pas,all)
      

         if varn.get() == "" or varp.get() == "" or varnp.get()=="" or varnn.get()=="" :
               lbl_text.config(text="Please complete the required field!", fg="#FF2247",font=("serif",14))
         elif(varn.get()==us and varp.get()==pas and varnn.get()!="" and varnp.get()!=""):
            msg=dbconect.update(varnn.get(),varnp.get())

            #root.withdraw() 

            lbl_text.config(text=" success", fg="green",font=("serif",14))
            # us=varnn.get()
            # pas=varnp.get()
            print(us,pas)
            root.destroy()  #for delete window
            
         else: 
            lbl_text.config(text="error: Invalid username or password",fg="#FF2247",font=("serif",14))
            varn.set("")
            varp.set("")
            varnn.set("")
            varnp.set("")




      b1.config(command=try_change)    
      #

      root.mainloop()
