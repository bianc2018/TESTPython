#-*- coding:utf-8 _*-
"""
@author:hql
@file: AbsoluteLayout
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import *
import sys

class AbsoluteLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel("姓名",self)
        label1.move(15,10)
        label2 = QLabel("年龄",self)
        label2.move(35,40)
        label3 = QLabel("所在城市",self)
        label3.move(55,70)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("绝对布局")
        self.show()
app = QApplication(sys.argv)
msg = AbsoluteLayout()
sys.exit(app.exec_())