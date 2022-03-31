import sqlite3
class DBConnect:
    def __init__(self):# function intialize db
        self.db=sqlite3.connect("Reservatio.db")#  connect db
        self.db.row_factory=sqlite3.Row  #for modify db
        self.db.execute("create table if not exists Ticket(ID integer primary key autoincrement,FName text,LName text,date text,phone text,nat text,Gender text,Comments text)") #create Tables on db
        self.db.commit()

    def Add(self,FName,LName,date,phone,nat,Gender,Comments):
        self.db.execute("insert into Ticket(FName,LName,date,phone,nat,Gender,Comments)values(?,?,?,?,?,?,?)",(FName,LName,date,phone,nat,Gender,Comments))
        self.db.commit()
        return("request is submited")


    def ShowListes(self):
        L=self.db.execute("select * from Ticket")
        return L
