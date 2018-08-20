#-*- coding:utf-8 _*-
"""
@author:hql
@file: Server
@time: 2018/08/{DAY}
"""
import socket
from PyQt5 import sip
from multiprocessing import Process, Queue
from time import sleep
import multiprocessing
import datetime
from sys import exit
import UI
import Protocol
from setting import defultSocket

class Server:
    """
    socket 服务器端代码
    """
    clients = {} #id : addr:post,con
    state = "未初始化"
    def __init__(self):
        #server to ui
        self.Pro = Protocol.Protocol()
        self.Pro.bind('quit',self.quit)
        self.Pro.bind('info',self.put)
        self.Pro.bind('help',self.help)
        self.Pro.bind('list', self.list)
        self.Pro.bind('sendstr', self.sendstr)
        self.Pro.bind('open', self.open)
        self.Pro.bind('close', self.close)

        #server and client
        self.cs = Protocol.Protocol()
        self.cs.bind('msg',self.msg)
        self.cs.bind('quit', self.subCloseClient)

        self.host = "127.0.0.1"
        self.port = 80
        self.Imsg = Queue()
        self.Omsg = Queue()
        self.accept_queue = Queue()
        self.recv_queue = Queue()
        self.show()
    def open(self,data={"DATA":{}}):
        if self.state == '启动':
            self.info("服务器已启动")
            return
        try:
            msg = data['DATA']
            df = defultSocket
            df.update(msg)
            self.accept_queue = Queue()
            self.recv_queue = Queue()
            self.createSocket(df['ip'],df['port'],df['num'],df['size'])
        except Exception as e:
            self.info(f"出现错误："+str(e))

    def createSocket(self,adress,port = 8001,num=5,size=1024):
        self.host = adress
        self.port = port
        self.socket = socket.socket()
        self.socket.bind((adress, port))
        self.socket.listen(num)
        self.BUFFER_SIZE = size
        self.startAccept()
        self.state = "启动"
        self.info("New Server Info:")
        self.put()

    def info(self,string):
       # print(string)
        msg = self.Pro.pack(string, "server", 'ui', 'info')
        self.Omsg.put(msg)

    def accept(self):
        self.info("监听程序启动")
        self.id = 0
        while True:
            try:
                con, adr = self.socket.accept()
                self.info(f"接收新连接:{adr}")
                con.sendall(bytes(str(self.id), encoding="utf-8"))
                self.accept_queue.put({str(self.id):[adr,con,datetime.datetime.now().strftime("%T"),None]})
                self.id+=1
            except Exception as e:
                self.info("出现一个错误：" + str(e))

    def recv(self,con,key):
        self.info(f"recver create:{key}")

        while True:
            try:
                msg = con.recv(self.BUFFER_SIZE)
                self.recv_queue.put(msg)
            except Exception as e:
                self.info("出现一个错误："+str(e))
                self.recv_queue.put(self.cs.pack({'key':key,'why':str(e)},key,'server','quit'))
                return -1

    def send(self,string,key):
        if key not in self.clients.keys():
            self.info(f"用户:{key},未连接。。。。")
            return None
        con = self.clients[key][1]
        con.sendall(bytes(string,encoding="utf-8"))

    def show(self):
        self.UIProcess = Process(target=UI.RUN, args=(self.Imsg, self.Omsg))
        self.UIProcess.start()

    def startAccept(self):
        self.AcceptProcess = Process(target=self.accept, args=())
        self.AcceptProcess.start()

    def loop(self):
        try:
            #self.RecvProcess = []
            self.info("开始主循环")
            self.open()
            while True:
                #accept
                while self.accept_queue.qsize()>0:
                    q = self.accept_queue.get(True)
                    key = list(q.keys())[0]
                    recv = Process(target=self.recv, args=(q[key][1],key))
                    recv.start()
                    q[key][3] = recv
                    self.clients.update(q)
                #recv
                while self.recv_queue.qsize()>0:
                    msg = self.recv_queue.get(True)
                    msg = self.cs.unpack(msg)
                    self.cs.interpret_msg(msg)
                #ui
                while self.Imsg.qsize()>0:
                    msg = self.Imsg.get(True)
                    self.Pro.interpret_msg(self.Pro.unpack(msg))

        except Exception as e:
            self.info("发生错误："+str(e))
            self.quit()
        finally:
            self.quit()

    def close(self,data=None):
        self.Quit_Pro(self.AcceptProcess)

        for key in self.clients:
            self.send("close",key)
            self.closeClient(key)

        self.clients={}
        self.recv_queue.close()
        self.accept_queue.close()
        self.socket.close()
        self.info("Socket Close")
        self.state = "关闭"

    def Quit_Pro(self,Pro):
        Pro.terminate()
        Pro.join()
    def subCloseClient(self,data):
        key = data['DATA']['key']
        self.closeClient(key)
    def closeClient(self,key):
        if key in self.clients.keys():
            self.clients[key][1].close()
            self.Quit_Pro(self.clients[key][3])
            del self.clients[key]
        else:
            self.info(f"id:{key}不存在")

    def put(self,data = None):
        self.info(f"Server:{self.state}")
        self.info(f"\tHost:{self.host}:{self.port}")
        self.list()

    def list(self,data=None):
        size = len(self.clients)
        self.info(f"Connect Client:{size}:")
        self.info("Begin:")
        for c in self.clients:
            self.info(f"id:{c},ip:{self.clients[c][0][0]+':'+str(self.clients[c][0][1])},time:{self.clients[c][2]}")
        self.info("End")

    def msg(self,packmsg):
        to = packmsg['TO']
        if to == "server":
            self.info(packmsg)
            return
        if to in self.clients.keys():
            self.send(self.cs.pack(packmsg['DATA'],packmsg['FROM'],to,'msg'),to)
        else:
            self.send(self.cs.pack(f"发生错误：{to}不存在或不在线","server", packmsg['FROM'], 'info'),packmsg['FROM'])

    def sendstr(self,msg):
        data = msg['DATA']
        ids = str(data['id'])
        string = data['str']
        self.send(string,ids)

    def quit(self,data=None):
        df = {'t':0}
        if data:
            msg = data['DATA']
            df.update(msg)
        self.info("SERVER QUITING.....")
        self.put()
        self.info(f"exit after {df['t']} sec.....")
        if self.state == "启动":
            self.close()
        sleep(int(df['t']))
        self.Quit_Pro(self.UIProcess)
        exit(0)

    def help(self,data=None):
        text =  '''
                    局域网通信软件：
                    服务器端
                    版本：1.0
                    作者：BAINC
                    指令：
                    quit：退出程序
                    info：打印信息
                    help：打印帮助文档
                    list：列出连接的客户端
                    sendstr ip:.... post:8888 str:文字 ：向客户机（ip,host）发送信息str
                '''
        self.info(text)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    try:
        s = Server()
        s.loop()
    except Exception as e:
        print("发生未知错误：",str(e))

