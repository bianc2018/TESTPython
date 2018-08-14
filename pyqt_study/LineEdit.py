#-*- coding:utf-8 _*-
"""
@author:hql
@file: LineEdit
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import  QWidget,QApplication,QLineEdit,QLabel
import sys

class LineEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.label = QLabel(self)
        edit = QLineEdit(self)
        edit.textChanged[str].connect(self.onChange)
        edit.move(80,100)
        self.label.move(80, 40)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QLineEdit控件')
        self.show()
    def onChange(self,text):
        print(text)
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = LineEdit()
    sys.exit(app.exec_())