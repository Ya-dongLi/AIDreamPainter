# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PictureSite(object):
    def setupUi(self, PictureSite):
        PictureSite.setObjectName("PictureSite")
        PictureSite.resize(1137, 624)
        PictureSite.setMinimumSize(QtCore.QSize(1137, 624))
        PictureSite.setMaximumSize(QtCore.QSize(1137, 624))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./picture/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PictureSite.setWindowIcon(icon)
        PictureSite.setStyleSheet("")
        self.result_label_web = QtWidgets.QLabel(PictureSite)
        self.result_label_web.setGeometry(QtCore.QRect(150, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.result_label_web.setFont(font)
        self.result_label_web.setStyleSheet("color: rgb(255, 255, 255);")
        self.result_label_web.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_web.setObjectName("result_label_web")
        self.result_text = QtWidgets.QTextEdit(PictureSite)
        self.result_text.setGeometry(QtCore.QRect(50, 90, 481, 384))
        self.result_text.setMinimumSize(QtCore.QSize(481, 384))
        self.result_text.setMaximumSize(QtCore.QSize(481, 384))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.result_text.setFont(font)
        self.result_text.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(0, 255, 255);\n"
"border:0px;")
        self.result_text.setObjectName("result_text")
        self.CloseButton = QtWidgets.QPushButton(PictureSite)
        self.CloseButton.setGeometry(QtCore.QRect(490, 520, 141, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.CloseButton.setFont(font)
        self.CloseButton.setStyleSheet("/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"background-color: rgb(192, 192, 192);\n"
"border-radius: 20px; \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"}\n"
"\n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(156, 156, 156);\n"
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
"}\n"
"")
        self.CloseButton.setObjectName("CloseButton")
        self.result_label_img = QtWidgets.QLabel(PictureSite)
        self.result_label_img.setGeometry(QtCore.QRect(710, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.result_label_img.setFont(font)
        self.result_label_img.setStyleSheet("color: rgb(255, 255, 255);")
        self.result_label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_img.setObjectName("result_label_img")
        self.img_view = QtWidgets.QLabel(PictureSite)
        self.img_view.setGeometry(QtCore.QRect(590, 90, 512, 384))
        self.img_view.setMinimumSize(QtCore.QSize(512, 384))
        self.img_view.setMaximumSize(QtCore.QSize(512, 384))
        self.img_view.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.img_view.setText("")
        self.img_view.setObjectName("img_view")
        self.label = QtWidgets.QLabel(PictureSite)
        self.label.setGeometry(QtCore.QRect(0, 0, 1161, 641))
        self.label.setStyleSheet("background-image: url(\"./picture/background.jpg\");")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.result_label_web.raise_()
        self.result_text.raise_()
        self.CloseButton.raise_()
        self.result_label_img.raise_()
        self.img_view.raise_()

        self.retranslateUi(PictureSite)
        QtCore.QMetaObject.connectSlotsByName(PictureSite)

    def retranslateUi(self, PictureSite):
        _translate = QtCore.QCoreApplication.translate
        PictureSite.setWindowTitle(_translate("PictureSite", "梦境图片"))
        self.result_label_web.setText(_translate("PictureSite", "其他梦境图片网址"))
        self.result_text.setHtml(_translate("PictureSite", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CloseButton.setText(_translate("PictureSite", "关闭"))
        self.result_label_img.setText(_translate("PictureSite", "一张梦境图片展示"))

