#-*- coding:utf-8 _*-
"""
@author:hql
@file: PixMap
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import  QWidget,QApplication,QLabel,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class PixMap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout(self)

        pixmap = QPixmap('python.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QPixMap控件')
        self.show()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = PixMap()
    sys.exit(app.exec_())