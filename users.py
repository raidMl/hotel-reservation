from tkinter import  *
from  tkinter import ttk
from  DbConnect import  DBConnect
dbconnect=DBConnect()
class ListTickect:
    def __init__(self):
       self.root=Tk()
       self.dbconnect=DBConnect()
       tv=ttk.Treeview(self.root)
       tv.pack()
       tv.heading("#0",text='id')
       tv.configure(column=("#user",))
       tv.heading("#user",text="user_name")
      
       L=self.dbconnect.ShowListes()
       for row in L:
           tv.insert("","end","#{}".format(row["id"]),text=row["id"])
           tv.set("#{}".format(row["id"]),"#Name",row["user_name"])





       self.root.mainloop()