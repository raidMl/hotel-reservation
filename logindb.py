import sqlite3
class DBConnectUser:
    def __init__(self):# function intialize db
        self.db=sqlite3.connect("user.db")#  connect db
        self.db.row_factory=sqlite3.Row  #for modify db
        self.db.execute("create table if not exists users(ID integer primary key autoincrement,name ,password)") #create Tables on db
        self.db.commit()

    def update(self,name,password):
        self.db.execute("UPDATE  users SET  name=?,password=? WHERE id=1" ,(name,password)) 
        self.db.commit()
        return("request is submited")
    
    
    def GetUser(self):
        u=self.db.execute("SELECT name FROM users WHERE id=1")
        self.db.commit()
        return u
    def GetPass(self):
        p=self.db.execute("SELECT password FROM users WHERE id=1")
        self.db.commit()
        return p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    def ShowUsers(self):
        L=self.db.execute("select * from users")
        return L
