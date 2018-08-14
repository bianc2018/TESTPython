#-*- coding:utf-8 _*-
"""
@author:hql
@file: ComboBox
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import  QWidget,QApplication,QLabel,QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class ComboBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.label = QLabel('中国',self)
        self.label.move(50,150)

        combo = QComboBox(self)
        combo.addItem('中国')
        combo.addItem('美国')
        combo.addItem('法国')
        combo.addItem('英国')
        combo.addItem('意大利')
        combo.move(50,50)
        combo.activated[str].connect(self.onActivated)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QComboBox控件')
        self.show()
    def onActivated(self,text):
        self.label.setText(text)
        self.label.adjustSize()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = ComboBox()
    sys.exit(app.exec_())