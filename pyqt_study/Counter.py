#-*- coding:utf-8 _*-
"""
@author:hql
@file: Counter
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import QLabel,QApplication,QPushButton,QGridLayout,QWidget
import sys

class Counter(QWidget):
    def __init__(self):
        self.gridtip = [    ["重置","0","*","/"],
                            ['7','8','9','+'],
                            ['4','5','6','-'],
                            ['1','2','3','='],
                        ]
        self.strs = ""
        super().__init__()
        self.initUI()
        self.iniMain()

    def initUI(self):
        grid = QGridLayout(self)
        grid.setSpacing(10)
        self.outp = QLabel(self.strs,self)
        grid.addWidget(self.outp,1,0,1,4)

        i = 1
        for row in self.gridtip:
            i+=1
            j=0
            for name in row:
                b = QPushButton(name,self)
                b.clicked.connect(self.onClicked)
                grid.addWidget(b,i,j)
                j+=1
        self.setLayout(grid)
        pass
    def iniMain(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('计算器')
        self.show()
    def onClicked(self,text):
        use = self.sender()
        getclieck = use.text()
        if getclieck == "重置":
            self.strs = ""
        elif getclieck == "=":
            self.strs = self.count(self.strs)
        else:
            self.strs += getclieck
        self.outp.setText(self.strs)
        pass
    def count(self,strs):
        num = []
        op = []
        d = 0
        for s in strs:
            if s not in "0123456789*/-+":
                return "错误输入"
           # print(op,num)
            if s in "0123456789":
                d = d*10+int(s)
            elif s in "+-":
                num.append(d)
                d = 0
                if len(op)>=1:
                    result = self.subCount(num[-2],op[-1],num[-1])
                    if type(result) == str:
                        return result
                    op.pop()
                    num.pop()
                    num.pop()
                    num.append(result)
                op.append(s)
            elif s in "*/":
                num.append(d)
                d = 0
                op.append(s)
        num.append(d)
        size = len(op)
        #print(op, num)

        for  i in range(0,size):
           # print(op, num)
            p = op.pop()
            n2 = num.pop()
            n1 = num.pop()
           # print(n1,p,n2)
            result = self.subCount(n1,p,n2)
            if type(result) == str:
                return result
            num.append(result)
        #print(op, num)
        return str(num[0])
    def subCount(self,n1,op,n2):
        if op == "-":
            return n1-n2
        elif op == "+":
            return n1+n2
        elif op == "*":
            return n1*n2
        elif op == '/':
            if n2==0:
                return "除零错误"
            return n1/n2
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Counter()
    sys.exit(app.exec_())