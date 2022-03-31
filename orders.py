from tkinter import  *
from  tkinter import ttk
from  DbConnect import  DBConnect
dbconnect=DBConnect()
class ListTickect:
    def __init__(self):
       self.root=Tk()
       self.root.configure(bg="yellow")

       self.root.title("reserved liste")        

       self.dbconnect=DBConnect()
       tv=ttk.Treeview(self.root)
       tv.pack()
       tv.heading("#0",text='id')
       tv.configure(column=("#FName","#LName","#date","#phone","#nat","#Gender","#Comments"))
       tv.heading("#FName",text="First-Name")
       tv.heading("#LName",text="Last-Name")
       tv.heading("#date",text="reserve date")
       tv.heading("#phone",text="phone")

       tv.heading("#nat",text="nationality")
       
       tv.heading("#Gender",text="Gender")
       tv.heading("#Comments",text="Comments")
       L=self.dbconnect.ShowListes()
       for row in L:
           tv.insert("","end","#{}".format(row["id"]),text=row["id"])



           tv.set("#{}".format(row["id"]),"#FName",row["FName"])
           tv.set("#{}".format(row["id"]),"#LName",row["LName"])
           tv.set("#{}".format(row["id"]),"#phone",row["phone"])

           tv.set("#{}".format(row["id"]),"#nat",row["nat"])

           tv.set("#{}".format(row["id"]),"#Gender",row["Gender"])
           tv.set("#{}".format(row["id"]),"#date",row["date"])

           tv.set("#{}".format(row["id"]),"#Comments",row["Comments"])




       self.root.mainloop()