#-*- coding:utf-8 _*-
"""
@author:hql
@file: Client
@time: 2018/08/{DAY}
"""
from Protocol import Protocol
from multiprocessing import Process, Queue
import datetime
import socket

class Client:
    """
        socket 客户端代码
    """
    clients = {}
    def __init__(self):
        self.pro = Protocol()
        self.to = None
        self.packMsg = ['msg','login','unlogin','list']
        self.myorders = {'lock':self.lock,'unlock':self.unlock}

    def initConnect(self,adress='192.168.191.1',port = 8001,size=1024):
        self.host = adress
        self.port = port
        self.socket = socket.socket()
        self.socket.connect((adress, port))
        self.BUFFER_SIZE = size

        self.id = self.socket.recv(self.BUFFER_SIZE)
        self.output(self.id)
        self.startRecv()

    def send(self,string):
        print(string)
        self.socket.sendall(string)

    def startRecv(self):
        self.recvPro = Process(target=self.recv, args=())
        self.recvPro.start()

    def recv(self):
        while True:
            msg = self.socket.recv(self.BUFFER_SIZE)
            self.recv_queue.put(msg)

    def sendMsg(self,text):
        print(text)
        if self.to:
            if text=='~':
                self.unlock()
                return
            self.send(self.pro.pack(text,self.id,self.to,'msg'))
            return
        lists = text.split(' ')
        # self.output(str(list),"test")
        head = lists[0]
        if head in self.packMsg:
            args = self.getArgs(lists[1:])
            self.send(self.pro.pack(args, 'ui', 'server', head))
        elif head in self.myorders.keys():
            args = self.getArgs(lists[1:])
            self.myorders[head](args)
        else:
            self.output(f"指令：{head}不存在", 'error')
        pass
    def getArgs(self,arglist):
        data = {}
        for arg in arglist:
            if ':' in arg:
                key, value = arg.split(':')
                data.update({key: value})
        return data
    def run(self):
        pass

    def quit(self,data=None):
        self.recvPro.terminate()
        self.recvPro.join()
        exit(0)
    def lock(self,arg):
        if 'id' in arg.keys():
            self.to = arg['id']
            self.output(f'LOCK{self.to}', 'result')

    def unlock(self,arg=None):
        self.output(f'UNLOCK{self.to}','result')
        self.to = None

    def output(self,string,title="server"):
        t = datetime.datetime.now().strftime("%T")
        text = "[%s][%s]:%s"%(t,title,string)
        print(text)
        #print text

if __name__ == "__main__":
    c = Client()
    c.initConnect()
    while True:
        text = input("send:")
        c.sendMsg(text)



