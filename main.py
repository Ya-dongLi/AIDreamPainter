import sys
import time
import webbrowser
from utils import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from windows.login import Ui_Login
from windows.dream import Ui_DreamPainter
from windows.result import Ui_PictureSite
from windows.waiting import Ui_Waiting



#登陆界面
class LoginWindow(QMainWindow, Ui_Login):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.getAPI.clicked.connect(self.getAPIkey)

    def getAPIkey(self):
        webbrowser.open("https://wenxin.baidu.com/moduleApi/key")



#写故事界面
class DreamPaint(QMainWindow, Ui_DreamPainter):
    def __init__(self):
        super(DreamPaint, self).__init__()
        self.setupUi(self)



#绘梦结果界面
class PictureWindow(QMainWindow, Ui_PictureSite):
    def __init__(self):
        super(PictureWindow, self).__init__()
        self.setupUi(self)
        self.CloseButton.clicked.connect(self.close_window)

    def close_window(self):
        self.close()



#等待界面
class Waiting(QMainWindow,Ui_Waiting):
    def __init__(self):
        super(Waiting, self).__init__()
        self.setupUi(self)
        self.background_show = QMovie("./picture/wait.gif")
        self.background.setMovie(self.background_show)
        self.background_show.start()
        self.GotoWeb.clicked.connect(self.gotoweb)

    def gotoweb(self):
        webbrowser.open("https://wenxin.baidu.com/moduleApi/ernieVilg")



#另开线程获取结果，避免窗口线程因等待时间过长卡死
class getIMG(QThread):
    time_required = pyqtSignal(int)
    website = pyqtSignal(str)
    stop_window = pyqtSignal(bool)

    def __init__(self,key,text):
        super().__init__()
        self.key = key
        self.text = text

    def run(self):
        #获取文本摘要
        summary = get_summary(self.key,self.text)
        if summary==-1:
            self.stop_window.emit(True)
        time.sleep(2)
        #获取图片任务ID
        taskID = get_imgID(self.key,summary)
        if taskID==-1:
            self.stop_window.emit(True)
        time.sleep(2)
        #获取等待时间和结果
        while True:
            r = get_img(self.key,taskID)
            if r==-1:
                self.stop_window.emit(True)
            elif type(r)==int:
                self.time_required.emit(r)
            else:
                self.website.emit(r)
            time.sleep(30)



#总控制端
class terminal():
    def __init__(self):
        #login窗口
        self.login_window = LoginWindow()
        self.login_window.submit.clicked.connect(self.submitKey)
        self.login_window.show()
        #dream窗口
        self.dreampaint_window = DreamPaint()
        self.dreampaint_window.start.clicked.connect(self.paint)
        #result窗口
        self.picture_window = PictureWindow()
        #wainting窗口
        self.waiting = Waiting()

    #检查key
    def submitKey(self):
        ak = self.login_window.AKey.text()
        sk = self.login_window.SKey.text()
        licence = get_token(ak, sk)
        if licence == -1:
            QMessageBox.critical(self.login_window, "Error", "服务器连接错误！")
        elif licence == None:
            QMessageBox.critical(self.login_window, "Error", "key输入错误，请重新输入！")
        else:
            self.key = licence
            self.dreampaint_window.show()
            self.login_window.close()

    #绘制
    def paint(self):
        text = self.dreampaint_window.DreamText.toPlainText()
        if len(text)<20:
            QMessageBox.warning(self.dreampaint_window,"Waring","请输入更详细的内容！")
        else:
            if len(text)>987:
                text = text[0:987]
            text = text+"。一句话概括上面的段落："
            self.ImgWebsites = getIMG(self.key,text)    #准备绘制
            self.ImgWebsites.time_required.connect(self.chang_window_time)
            self.ImgWebsites.website.connect(self.website_window)
            self.ImgWebsites.stop_window.connect(self.close_window)
            self.waiting.show()
            self.dreampaint_window.close()
            self.ImgWebsites.start()                    #开始绘制

    #服务异常，关闭窗口
    def close_window(self,stop):
        if stop:
            self.ImgWebsites.quit()
            QMessageBox.critical(self.login_window, "Error", "服务器连接错误！")
            self.waiting.close()

    #更新等待时间
    def chang_window_time(self,minute):
        self.waiting.time_label.setText("预计还需要<=%d分钟"%(minute))

    def website_window(self,websites):
        self.ImgWebsites.quit()
        self.picture_window.result_text.setPlainText(websites)
        img = requests.get(url=websites.split("\n")[0]).content #获取一张图片
        with open("./picture/result.png", "wb") as f:
            f.write(img)
            f.close()
        self.picture_window.img_view.setStyleSheet("border-image: url(\"./picture/result.png\");")
        self.picture_window.show()
        self.waiting.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = terminal()
    sys.exit(app.exec_())
