#-*- coding:utf-8 _*-
"""
@author:hql
@file: button
@time: 2018/08/{DAY}
"""
"""
    按钮支持两种状态：Normal和Checked。
"""
from PyQt5.QtWidgets import  QWidget,QApplication,QPushButton,QFrame
from PyQt5.QtGui import QColor
import sys

class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.color = QColor(0,0,0)

        greenButton = QPushButton('绿色',self)
        greenButton.setCheckable(True)
        greenButton.move(10,10)
        greenButton.clicked[bool].connect(self.setColor)

        redButton = QPushButton('红色',self)
        redButton.setCheckable(True)
        redButton.move(10,60)
        redButton.clicked[bool].connect(self.setColor)

        blueButton = QPushButton("蓝色",self)
        blueButton.setCheckable(True)
        blueButton.move(10, 110)
        blueButton.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget{background-color:%s}'%self.color.name())

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('居中')
        self.show()
    def setColor(self,p):
        use = self.sender()
        if p:
            val =255
        else:
            val = 0

        print(p,val,use.text())
        if use.text() == "红色":
            self.color.setRed(val)
        elif use.text() == "绿色":
            self.color.setGreen(val)
        elif use.text() == "蓝色":
            self.color.setBlue(val)

        self.square.setStyleSheet('QWidget{background-color:%s}' % self.color.name())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = Button()
    sys.exit(app.exec_())