# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(624, 451)
        Login.setMinimumSize(QtCore.QSize(624, 451))
        Login.setMaximumSize(QtCore.QSize(624, 451))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./picture/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.formLayoutWidget = QtWidgets.QWidget(Login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 150, 451, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.InputKey = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.InputKey.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.InputKey.setFormAlignment(QtCore.Qt.AlignCenter)
        self.InputKey.setContentsMargins(0, 0, 0, 0)
        self.InputKey.setVerticalSpacing(30)
        self.InputKey.setObjectName("InputKey")
        self.AK = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AK.setFont(font)
        self.AK.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AK.setStyleSheet("color: rgb(250, 250, 0);")
        self.AK.setObjectName("AK")
        self.InputKey.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.AK)
        self.SK = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SK.setFont(font)
        self.SK.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SK.setStyleSheet("color: rgb(250, 250, 0);")
        self.SK.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SK.setObjectName("SK")
        self.InputKey.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.SK)
        self.AKey = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.AKey.setMinimumSize(QtCore.QSize(0, 0))
        self.AKey.setSizeIncrement(QtCore.QSize(0, 0))
        self.AKey.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.AKey.setFont(font)
        self.AKey.setStyleSheet("border: 1px solid gray;/*设置边框的粗细，以及颜色*/\n"
"border-radius: 10px;/*设置圆角的大小*/\n"
"padding: 0 8px;/*如果没有内容光标在开始往后移动0.8像素点*/\n"
"selection-background-color: darkgray;")
        self.AKey.setObjectName("AKey")
        self.InputKey.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.AKey)
        self.SKey = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.SKey.setFont(font)
        self.SKey.setStyleSheet("border: 1px solid gray;/*设置边框的粗细，以及颜色*/\n"
"border-radius: 10px;/*设置圆角的大小*/\n"
"padding: 0 8px;/*如果没有内容光标在开始往后移动0.8像素点*/\n"
"selection-background-color: darkgray;")
        self.SKey.setText("")
        self.SKey.setObjectName("SKey")
        self.InputKey.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.SKey)
        self.submit = QtWidgets.QPushButton(Login)
        self.submit.setGeometry(QtCore.QRect(260, 340, 93, 28))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submit.setStyleSheet("/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"    /*字体颜色为白色*/    \n"
"    color:balck;\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(211, 211, 211);\n"
"    /*边框圆角半径为8像素*/ \n"
"    border-radius:10px;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.984886, y2:0.995, stop:0 rgba(249, 255, 116, 138), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(255, 255, 255);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.submit.setObjectName("submit")
        self.getAPI = QtWidgets.QPushButton(Login)
        self.getAPI.setGeometry(QtCore.QRect(400, 340, 151, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.getAPI.setFont(font)
        self.getAPI.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.getAPI.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(250, 250, 0);\n"
"border-radius: 10px;  \n"
"border: rgba(255, 255, 255, 0);\n"
"border-style: outset;")
        self.getAPI.setObjectName("getAPI")
        self.title = QtWidgets.QLabel(Login)
        self.title.setGeometry(QtCore.QRect(150, 50, 351, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(250, 250, 0);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.background = QtWidgets.QLabel(Login)
        self.background.setGeometry(QtCore.QRect(0, -1, 631, 461))
        self.background.setStyleSheet("border-image: url(\"./picture/login.png\");")
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.raise_()
        self.formLayoutWidget.raise_()
        self.submit.raise_()
        self.getAPI.raise_()
        self.title.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "AI绘梦师(登录)"))
        self.AK.setText(_translate("Login", "API key:"))
        self.SK.setText(_translate("Login", "Secret key:"))
        self.AKey.setPlaceholderText(_translate("Login", "请输入你的API Key"))
        self.SKey.setPlaceholderText(_translate("Login", "请输入你的Secret Key"))
        self.submit.setText(_translate("Login", "确定"))
        self.getAPI.setText(_translate("Login", "如何获取key?"))
        self.title.setText(_translate("Login", "AI绘梦师(登录)"))

