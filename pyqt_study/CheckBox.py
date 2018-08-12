#-*- coding:utf-8 _*-
"""
@author:hql
@file: CheckBox
@time: 2018/08/{DAY}
"""

from PyQt5.QtWidgets import  QWidget,QApplication,QLineEdit,QLabel,QCheckBox
from PyQt5.QtCore import Qt
import sys

class CheckBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        check = QCheckBox("请选择我",self)
        check.move(20,20)
        check.stateChanged.connect(self.onChange)
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('未选择')
        self.show()
    def onChange(self,state):
        if state == Qt.Checked:
            self.setWindowTitle("以选择")
        else:
            self.setWindowTitle("未选择")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = CheckBox()
    sys.exit(app.exec_())