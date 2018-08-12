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
app = QApplication(sys.argv)
w = QWidget()
w.setGeometry(300,300,300,220)
w.setWindowTitle('窗口')
app.setWindowIcon(QIcon('python.png'))
QToolTip.setFont(QFont('SanSerif',20))
button = QPushButton('关闭',w)
button.setToolTip("这是一个按钮\n设计者：HQL")
w.setToolTip("这是一个窗口\n设计者:HQL")
button.resize(button.sizeHint())
button.move(50,50)
button.clicked.connect(QCoreApplication.instance().quit)
w.show()
sys.exit(app.exec_())