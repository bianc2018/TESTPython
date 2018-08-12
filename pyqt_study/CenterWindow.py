#-*- coding:utf-8 _*-
"""
@author:hql
@file: CenterWindow
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import *
import sys

class CenterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(250,150)
        self.setWindowTitle('居中')
        self.center()
        self.show()
    def center(self):
        desktop = app.desktop()
        self.move((desktop.width()-self.width())/2,(desktop.height()-self.height())/2)
app = QApplication(sys.argv)
msg = CenterWindow()
sys.exit(app.exec_())