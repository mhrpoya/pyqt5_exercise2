import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import *
from login_page import Ui_MainWindow
from page2 import Ui_MainWin
from random_password.random_pass import rand_pass




class Panel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui_ = Ui_MainWin()
        self.ui_.setupUi(self)

        "delete title"
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()



class Root(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui_ = Ui_MainWindow()
        self.ui_.setupUi(self)

        "delete title"
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()
        self.ui_.loginbtn.clicked.connect(self.log)
        self.ui_.bucket.clicked.connect(self.reload_)
    
    def reload_(self):
        rand = rand_pass()
        self.ans_rand = self.ui_.randcode.setText(rand)


    def log(self):
        user = self.ui_.userline.text()
        password = self.ui_.passline.text()
        random_p = self.ui_.randline.text()
        if user and password and random_p:
            self.ui_.userline.setText("")
            self.ui_.passline.setText("")
            self.ui_.randline.setText("")
            self.ui_.userline.setFocus()
            self.ui_.passline.setFocus()
            self.ui_.randline.setFocus()
        
        if len(str(user)) == 0 and len(str(password)) == 0 and len(str(random_p)):
            self.ui_.war.setText("")

        elif user == "mehrpoya_kh" and password == "mekh1380" and random_p == self.ans_rand:
            self.ui_.war.setText("")
            self.panel = Panel()
            self.panel.show()

        
        elif not user and password and random_p != self.ans_rand:
            self.ui_.war.setText("Error, Please try Again !!")
    
    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Root()
    app.exec_()