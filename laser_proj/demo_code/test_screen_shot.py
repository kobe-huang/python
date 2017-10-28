import sys
from PyQt5 import QtCore, QtGui, QtWidgets,QtQuickWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtQuick import *
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtSlot, pyqtSignal
#import pixcolor
import base64

import win32api
import win32con
import win32gui
from ctypes import *
import time
class GraspWin(QQuickView,QObject):
    graspWinQuit = pyqtSignal()
    def __init__(self):
        super(GraspWin,self).__init__()
        self.img = QtGui.QGuiApplication.primaryScreen().grabWindow(0)
        self.img.save("123.bmp", "bmp");
        # screen = QApplication.desktop().screenGeometry()
        # self.setGeometry(screen)
        # self.setFlags(Qt.FramelessWindowHint);
        # self.setColor(QtGui.QColor(Qt.transparent));
        # self.setSource(QUrl("grasp.qml"))
        # self.rootContext().setContextProperty("graspwin", self)
    @pyqtSlot(str,result=str)
    def getThisColor(self,pos):
        #return pixcolor.getThisColor(pos, self.img)
        pass
    @pyqtSlot()
    def closeGraspwin(self):
        self.graspWinQuit.emit()
        self.close()
    @pyqtSlot(str,str,str)
    def saveGrasp(self,datas,path,ext):
        pass;
        # b64datas = base64.b64decode(datas.split("base64,")[1])
        # bar = QtCore.QByteArray.fromBase64(base64.b64encode(b64datas))
        # qimg = QtGui.QImage.fromData(base64.b64encode(b64datas))
        # qpic =QtGui.QPixmap()
        # isload = qpic.loadFromData(bar,ext.upper())
        # if(path != "zero"):
        #     bol = qpic.save(path, ext.upper())
        # else:
        #     clipb = QApplication.clipboard()
        #     clipb.clear()
        #     clipb.setPixmap(qpic)
def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)

def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
import sys  
import os.path  
import win32clipboard as w    
import win32con  
import win32api  
def getText():#读取剪切板  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_UNICODETEXT )  
    w.CloseClipboard()  
    return d  

def setText(string_z):#写入剪切板  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    print(string_z);
    w.SetClipboardData(win32con.CF_UNICODETEXT , string_z)  
    w.CloseClipboard()  

def copy_to(): 
    a = "aaaaaz"
    setText(a)#将“你好”写入剪切板  
    print(getText())
    #自动粘贴剪切板中的内容
    # QtGui.QGuiApplication.clipboard.clear()
    # PyQt5.QtGui.QGuiApplication.clipboard.setText("huangyinke")
    # clipboard = QtGui.QApplication.clipboard()
    # clipboard = QtGui.QGuiApplication.clipboard();
    # #clipboard.clear()
    # clipboard.setText("huang2222yinke")
    # clipboard.store()
    # print(clipboard.text())

    win32api.keybd_event(17,0,0,0)  #ctrl的键位码是17  
    win32api.keybd_event(86,0,0,0)#v的键位码是86  
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键  
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)  
    win32api.keybd_event(13,0,0,0)#Enter的键位码是13  
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)  

import cv2
import numpy as np
import matplotlib.pyplot as plt
def find_pic():
    mrW=cv2.imread('2.png',1)
    backIMG=cv2.imread('123.bmp',1)
    plt.figure(0)
    plt.imshow(backIMG)
    plt.figure(1)
    plt.imshow(mrW)
    (WHeight, WWidth, n)=mrW.shape
    result = cv2.matchTemplate(backIMG, mrW, cv2.TM_CCOEFF)
    #print(str(result))
    (_, _, minimumLocation, maximumLocation) = cv2.minMaxLoc(result)
    topLeft = maximumLocation
    bottomRight = ((topLeft[0] + WWidth), (topLeft[1] + WHeight))
    print(str(topLeft) + "--" +str(bottomRight))
    return topLeft;
    # roi = backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]
    # mask = np.zeros(backIMG.shape, dtype="uint8")
    # backIMG = cv2.addWeighted(backIMG, 0.25, mask, 0.75, 0)
    # backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]] = roi
    # plt.figure(2)
    # plt.imshow(backIMG)


if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    mouse_click(572,1768) #(564,1127)#(572,1768) 
    time.sleep(1)
    c = GraspWin()
    time.sleep(1)

    xxxx = find_pic();

    mouse_click(xxxx[0],xxxx[1])
    time.sleep(1)
    copy_to();
    # c.show()
    # myApp.exec_()
    print("sdsddsd");
    sys.exit()