#-*- coding:utf-8 _*-
"""
@author:hql
@file: Slider
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import  QWidget,QApplication,QLineEdit,QLabel,QSlider
from PyQt5.QtCore import Qt
import sys

class Slider(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.label = QLabel("   ",self)
        self.label.setGeometry(160,40,80,30)

        slider = QSlider(Qt.Horizontal,self)
        slider.setMinimum(10)
        slider.setMaximum(500)
        slider.setGeometry(30,40,100,30)
        slider.valueChanged[int].connect(self.onChange)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider控件')
        self.show()
    def onChange(self,text):
        self.label.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = Slider()
    sys.exit(app.exec_())