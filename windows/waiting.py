# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waiting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Waiting(object):
    def setupUi(self, Waiting):
        Waiting.setObjectName("Waiting")
        Waiting.setWindowModality(QtCore.Qt.NonModal)
        Waiting.resize(431, 206)
        Waiting.setMinimumSize(QtCore.QSize(431, 206))
        Waiting.setMaximumSize(QtCore.QSize(431, 206))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./picture/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Waiting.setWindowIcon(icon)
        Waiting.setStyleSheet("")
        self.time_label = QtWidgets.QLabel(Waiting)
        self.time_label.setGeometry(QtCore.QRect(20, 20, 391, 111))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.GotoWeb = QtWidgets.QPushButton(Waiting)
        self.GotoWeb.setGeometry(QtCore.QRect(10, 140, 411, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GotoWeb.setFont(font)
        self.GotoWeb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GotoWeb.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(1, 166, 255);")
        self.GotoWeb.setObjectName("GotoWeb")
        self.background = QtWidgets.QLabel(Waiting)
        self.background.setGeometry(QtCore.QRect(0, 0, 431, 211))
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.raise_()
        self.time_label.raise_()
        self.GotoWeb.raise_()

        self.retranslateUi(Waiting)
        QtCore.QMetaObject.connectSlotsByName(Waiting)

    def retranslateUi(self, Waiting):
        _translate = QtCore.QCoreApplication.translate
        Waiting.setWindowTitle(_translate("Waiting", "Waiting"))
        self.time_label.setText(_translate("Waiting", "请稍候"))
        self.GotoWeb.setText(_translate("Waiting", "等待时间太长，可以点击这里前往官网等待"))

