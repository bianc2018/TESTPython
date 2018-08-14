#-*- coding:utf-8 _*-
"""
@author:hql
@file: Menu
@time: 2018/08/{DAY}
"""
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenu,QAction
import sys

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu('文件')
        imports = QMenu("导入",self)
        news = QAction("新建",self)
        import1 = QAction("从pdf导入",self)
        import2 = QAction("从word导入",self)
        imports.addAction(import1)
        imports.addAction(import2)
        fileMenu.addMenu(imports)
        fileMenu.addAction(news)

        import1.triggered.connect(self.pdf)
        import2.triggered.connect(self.word)
        self.setGeometry(600, 600, 500, 300)
        self.setWindowTitle('menu')
        self.show()
    def pdf(self,text):
        print(text)
        print("pdf")
    def word(self,text):
        print(text)
        print("word")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())