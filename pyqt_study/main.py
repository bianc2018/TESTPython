#-*- coding:utf-8 _*-
"""
@author:hql
@file: main.py
@time: 2018/08/{DAY}
"""
'''
PyQt5模块
1.QtCore:包含了核心的非GUI功能
2.QtGui:包含了窗口系统、事件处理、2D图像邓
3.QtWidgets:包含了一系列创建桌面应用的UI元素
'''
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import ui
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())