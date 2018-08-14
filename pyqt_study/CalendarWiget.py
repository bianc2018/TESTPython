#-*- coding:utf-8 _*-
"""
@author:hql
@file: CalendarWiget
@time: 2018/08/{DAY}
"""

from PyQt5.QtWidgets import  QWidget,QApplication,QLabel,QCalendarWidget,QVBoxLayout
from PyQt5.QtCore import Qt,QDate
from PyQt5.QtGui import QPixmap
import sys

class CalendarWiget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout(self)

        cw = QCalendarWidget(self)
        cw.setGridVisible(True)
        cw.clicked[QDate].connect(self.onDate)

        vbox.addWidget(cw)
        self.label = QLabel(cw.selectedDate().toString(), self)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QComboBox控件')
        self.show()
    def onDate(self,date):
        self.label.setText(date.toString())
        self.label.adjustSize()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg = CalendarWiget()
    sys.exit(app.exec_())