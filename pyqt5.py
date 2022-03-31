import sys
from  PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow #  qmainwindow for main of app
from PyQt5.QtGui import QIcon
def Window():
    app=QtWidgets.QApplication(sys.argv)
    win=QtWidgets.QMainWindow() #for create window
    win.setWindowTitle("reservation hotels")
    win.setGeometry(800,100,500,500) # 1200 margin left 300 margin top 500heigt 500w in order
    win.setWindowIcon(QIcon("img/rami.png"))
    win.setToolTip("reservation hotels")  #like alt in html
    win.show() 
    sys.exit(app.exec_()) #for exit
Window()    
