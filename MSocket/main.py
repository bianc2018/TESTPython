#-*- coding:utf-8 _*-
"""
@author:hql
@file: Client
@time: 2018/08/{DAY}
"""
import socket
class Client:
    """
    socket 客户端代码
    """
    clients = {}
    def __init__(self,adress,port = 8000,num=5):
        self.host = adress
        self.port = port
        self.socket = socket.socket()
        self.socket.connect((adress,port))

    def send(self,string):
        self.socket.sendall(bytes(string,encoding="utf-8"))
    def recv(self):
        return str(self.socket.recv(1024), encoding="utf-8")
    def put(self):
        print("Cerver:")
        print(f"\tHost:{self.host}:{self.port}")

if __name__ == "__main__":
    c = Client('192.168.191.1')
    c.put()
    while True:
        print(c.recv())