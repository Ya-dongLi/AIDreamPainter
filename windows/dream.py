# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dream.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DreamPainter(object):
    def setupUi(self, DreamPainter):
        DreamPainter.setObjectName("DreamPainter")
        DreamPainter.resize(816, 559)
        DreamPainter.setMinimumSize(QtCore.QSize(816, 559))
        DreamPainter.setMaximumSize(QtCore.QSize(816, 559))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        DreamPainter.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./picture/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DreamPainter.setWindowIcon(icon)
        self.DreamLabel = QtWidgets.QLabel(DreamPainter)
        self.DreamLabel.setGeometry(QtCore.QRect(30, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.DreamLabel.setFont(font)
        self.DreamLabel.setObjectName("DreamLabel")
        self.DreamText = QtWidgets.QTextEdit(DreamPainter)
        self.DreamText.setGeometry(QtCore.QRect(110, 150, 599, 269))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DreamText.setFont(font)
        self.DreamText.setStyleSheet("font: 12pt \"宋体\";\n"
"background-color: rgb(143, 212, 255,60);\n"
"color: rgb(0, 0, 0);\n"
"border:0px;")
        self.DreamText.setObjectName("DreamText")
        self.title = QtWidgets.QLabel(DreamPainter)
        self.title.setGeometry(QtCore.QRect(280, 40, 241, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.start = QtWidgets.QPushButton(DreamPainter)
        self.start.setGeometry(QtCore.QRect(320, 440, 161, 101))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"background-color: rgb(165, 206, 255);\n"
"color: qlineargradient(spread:reflect, x1:0.512, y1:0.472091, x2:1, y2:1, stop:0.124378 rgba(0, 0, 165, 255), stop:1 rgba(255, 255, 255, 255));  \n"
"border-radius: 50px;  border: 2px groove gray;\n"
"border-style: outset;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}")
        self.start.setObjectName("start")
        self.background = QtWidgets.QLabel(DreamPainter)
        self.background.setGeometry(QtCore.QRect(0, 0, 821, 561))
        self.background.setStyleSheet("border-image: url(\"./picture/dream.jpg\");")
        self.background.setText("")
        self.background.setObjectName("background")
        self.background.raise_()
        self.DreamLabel.raise_()
        self.DreamText.raise_()
        self.title.raise_()
        self.start.raise_()

        self.retranslateUi(DreamPainter)
        QtCore.QMetaObject.connectSlotsByName(DreamPainter)

    def retranslateUi(self, DreamPainter):
        _translate = QtCore.QCoreApplication.translate
        DreamPainter.setWindowTitle(_translate("DreamPainter", "AI绘梦师"))
        self.DreamLabel.setText(_translate("DreamPainter", "请写出你的梦境："))
        self.DreamText.setHtml(_translate("DreamPainter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.DreamText.setPlaceholderText(_translate("DreamPainter", "不超过1000字"))
        self.title.setText(_translate("DreamPainter", "AI绘梦师"))
        self.start.setText(_translate("DreamPainter", "开始绘梦"))

