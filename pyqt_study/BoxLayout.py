#-*- coding:utf-8 _*-
"""
@author:hql
@file: BoxLayout
@time: 2018/08/{DAY}
"""

from PyQt5.QtWidgets import *
import sys

class BoxLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okbutton = QPushButton("确定")
        cancelbutton = QPushButton("取消")
        # 创建水平布局
        hbox = QHBoxLayout()
        # 让两个按钮始终在窗口右侧
        hbox.addStretch()
        hbox.addWidget(okbutton)
        hbox.addWidget(cancelbutton)
        # 创建垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("盒布局")

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    msg = BoxLayout()
    sys.exit(app.exec_())