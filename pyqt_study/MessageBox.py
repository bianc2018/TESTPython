#-*- coding:utf-8 _*-
"""
@author:hql
@file: MYQT.py
@time: 2018/08/{DAY}
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class MessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('对话框')
        self.show()
    def closeEvent(self,event):
        Message = QMessageBox.question(self,'消息',"您真的要退出吗？",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if Message == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
msg = MessageBox()
sys.exit(app.exec_())