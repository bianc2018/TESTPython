#-*- coding:utf-8 _*-
"""
@author:hql
@file: ProgressBar
@time: 2018/08/{DAY}
"""

from PyQt5.QtWidgets import  QWidget,QApplication,QLabel,QSlider,QProgressBar,QPushButton
from PyQt5.QtCore import Qt,QBasicTimer
import sys

class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.Pb = QProgressBar(self)
        self.Pb.setGeometry(40,40,200,25)
        self.button = QPushButton('开始',self)
        self.button.move(40,80)
        self.button.clicked.connect(self.doAtion)
        self.timer = QBasicTimer()

        self.value = 0
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QProgressBar控件')
        self.show()
    def timerEvent(self, e):
        if self.value>=100:
            self.timer.stop()
            self.button.setText("完成")
            return
        self.value+=1
        self.Pb.setValue(self.value)
    def doAtion(self,text):
        if self.value>=100:
            self.value = 0
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('开始')
        else:
            self.timer.start(100,self)
            self.button.setText("停止")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = ProgressBar()
    sys.exit(app.exec_())