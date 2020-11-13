import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Knowlegde Center"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(QSize(1920, 1080))
        
        label = QLabel(self)
        pixmap = QPixmap('Web 1920 – 1.png')
        label.setPixmap(pixmap)
        
       
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit( app.exec_() )
