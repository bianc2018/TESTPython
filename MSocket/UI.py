#-*- coding:utf-8 _*-
"""
@author:hql
@file: UI
@time: 2018/08/{DAY}
"""
from ServerUI import Ui_ServerUI
from PyQt5.QtWidgets import QApplication,QMainWindow,QSystemTrayIcon,QMenu,QAction
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
import sys
import datetime
from setting import ServerPro

import Protocol

_app = QApplication(sys.argv)
class MainServer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pro = Protocol.Protocol()
        self.pro.bind('info',self.info)
        self.orders = ServerPro
        self.myorders = {'clear':self.clear,'lock':self.lock,'unlock':self.unlock,'hide':self.Gethide}

        self.tray = QSystemTrayIcon()  # 创建系统托盘对象
        self.icon = QIcon('python.png')  # 创建图标
        self.tray.setIcon(self.icon)  # 设置系统托盘图标
        self.tray.activated.connect(self.TuoPanEvent)  # 设置托盘点击事件处理函数

        self.tray_menu = QMenu(QApplication.desktop())  # 创建菜单
        self.RestoreAction = QAction(u'还原 ', self, triggered=self.show)  # 添加一级菜单动作选项(还原主窗口)
        self.QuitAction = QAction(u'退出 ', self, triggered=self.mquit)  # 添加一级菜单动作选项(退出程序)
        self.StartAction = QAction(u'启动 ', self, triggered=self.start)  # 添加一级菜单动作选项(启动)
        self.CloseAction = QAction(u'关闭 ', self, triggered=self._close)  # 添加一级菜单动作选项(关闭)
        self.tray_menu.addAction(self.RestoreAction)  # 为菜单添加动作
        self.tray_menu.addAction(self.QuitAction)
        self.tray_menu.addAction(self.StartAction)
        self.tray_menu.addAction(self.CloseAction)
        self.tray.setContextMenu(self.tray_menu)  # 设置系统托盘菜单

        self.id = None
    def start(self,e):
        self.Imsg(self.pro.pack({},'ui','server','open'))
        pass
    def _close(self,e):
        self.Imsg.put(self.pro.pack({}, 'ui', 'server', 'close'))
        pass
    def TuoPanEvent(self,e):
        self.show()
        pass
    def Gethide(self,data):
        self.hide()
    def run(self,Imsg,Omsg):
        self.Imsg = Imsg
        self.Omsg = Omsg
        self.timer = QBasicTimer()
        self.timer.start(10, self)

        self.ui = Ui_ServerUI()
        self.ui.setupUi(self)
        self.ui.output.setReadOnly(True)
        self.show()
        sys.exit(_app.exec_())
        pass

    def mquit(self):
        self.Imsg.put(self.pro.pack({}, 'ui', 'server', 'sendstr'))
        pass
    def send(self):
        msg = self.ui.sendmsg.text()
        if len(msg)==0:
            return
        self.output(msg)
        self.sendMsg(msg)
       # self.Imsg.put(msg)
        self.ui.sendmsg.clear()
        pass

    def sendMsg(self,text):
        if self.id:
            if text =='~':
                self.unlock()
                return
            args = {'id':self.id,'str':text}
            self.Imsg.put(self.pro.pack(args, 'ui', 'server', 'sendstr'))
            return
        lists = text.split(' ')
        #self.output(str(list),"test")
        head = lists[0]
        if head in self.orders :
            args = self.getArgs(lists[1:])
            self.Imsg.put(self.pro.pack(args, 'ui', 'server', head))
        elif head  in self.myorders.keys():
            args = self.getArgs(lists[1:])
            self.myorders[head](args)
        else:
            self.output(f"指令：{head}不存在",'error')

    def getArgs(self,arglist):
        data = {}
        for arg in arglist:
            if ':' in arg:
                key, value = arg.split(':')
                data.update({key: value})
        return data

    def closeEvent(self,e):
        self.sendMsg("quit")

    def timerEvent(self, e):
        while self.Omsg.qsize()>0:
            msgpack = self.Omsg.get(True)
            msg = self.pro.unpack(msgpack)
            self.pro.interpret_msg(msg)

    def info(self,msg):
        data = msg['DATA']
        time = msg['TIME']
        _from = msg['FROM']
        self.ui.output.append(f"[{time}][{_from}]:{data}")

    def output(self,info,title = 'send'):
        ti = datetime.datetime.now().strftime("%T")  # 获得时间
        if self.id == None:
            self.ui.output.append(f"[{ti}][{title}]:{info}")
        else:
            self.ui.output.append(f"[{ti}][LOCK:{self.id}]:{info}")

    def clear(self,data=None):
        self.ui.output.clear()

    def lock(self,arg):
        if 'id' in arg.keys():
            self.id = arg['id']
            self.output(f'LOCK{self.id}', 'result')

    def unlock(self,arg=None):
        self.output(f'UNLOCK{self.id}','result')
        self.id = None

def RUN(Imsg,Omsg):
    MainWindow = MainServer()
    MainWindow.run(Imsg,Omsg)
if __name__ == '__main__':
    MainWindow = MainServer()
    MainWindow.run(None,None)