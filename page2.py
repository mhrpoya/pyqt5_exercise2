# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 190, 531, 201))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.restore2 = QtWidgets.QPushButton(self.centralwidget)
        self.restore2.setGeometry(QtCore.QRect(720, 10, 31, 31))
        self.restore2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restore2.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    background-color:rgb(166, 166, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.restore2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/MSI/Desktop/restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restore2.setIcon(icon)
        self.restore2.setIconSize(QtCore.QSize(24, 24))
        self.restore2.setObjectName("restore2")
        self.exit2 = QtWidgets.QPushButton(self.centralwidget)
        self.exit2.setGeometry(QtCore.QRect(760, 10, 31, 31))
        self.exit2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit2.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    background-color:rgb(166, 166, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.exit2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/MSI/Desktop/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit2.setIcon(icon1)
        self.exit2.setIconSize(QtCore.QSize(25, 26))
        self.exit2.setObjectName("exit2")
        self.minsize = QtWidgets.QPushButton(self.centralwidget)
        self.minsize.setGeometry(QtCore.QRect(680, 10, 31, 31))
        self.minsize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minsize.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius: 5px;\n"
"    background-color:rgb(166, 166, 166);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.minsize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/MSI/Desktop/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minsize.setIcon(icon2)
        self.minsize.setIconSize(QtCore.QSize(28, 28))
        self.minsize.setObjectName("minsize")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit2.clicked.connect(MainWindow.close) # type: ignore
        self.restore2.clicked.connect(MainWindow.showMaximized) # type: ignore
        self.minsize.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome to app"))
