# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\study\python\TESTPython\MSocket\ServerUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServerUI(object):
    def setupUi(self, ServerUI):
        ServerUI.setObjectName("ServerUI")
        ServerUI.resize(684, 596)
        ServerUI.setMinimumSize(QtCore.QSize(684, 596))
        self.centralwidget = QtWidgets.QWidget(ServerUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 671, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.send = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.send.setObjectName("send")
        self.gridLayout.addWidget(self.send, 4, 1, 1, 1)
        self.sendmsg = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sendmsg.setObjectName("sendmsg")
        self.gridLayout.addWidget(self.sendmsg, 3, 1, 1, 1)
        self.quit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.quit.setObjectName("quit")
        self.gridLayout.addWidget(self.quit, 4, 0, 1, 1)
        self.set = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.set.setObjectName("set")
        self.gridLayout.addWidget(self.set, 3, 0, 1, 1)
        self.output = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 2, 1, 1, 1)
        ServerUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(ServerUI)
        self.quit.clicked.connect(ServerUI.mquit)
        self.send.clicked.connect(ServerUI.send)
        self.sendmsg.editingFinished.connect(ServerUI.send)
        QtCore.QMetaObject.connectSlotsByName(ServerUI)
        ServerUI.setTabOrder(self.send, self.sendmsg)
        ServerUI.setTabOrder(self.sendmsg, self.quit)
        ServerUI.setTabOrder(self.quit, self.set)

    def retranslateUi(self, ServerUI):
        _translate = QtCore.QCoreApplication.translate
        ServerUI.setWindowTitle(_translate("ServerUI", "Server"))
        self.label_2.setText(_translate("ServerUI", "输出:"))
        self.send.setText(_translate("ServerUI", "发送"))
        self.quit.setText(_translate("ServerUI", "退出"))
        self.set.setText(_translate("ServerUI", "设置"))

