import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QMovie

pic1 = 'NW - 1.png'
pic2 = 'NW - 2.png'
pic3 = 'NW - 3.png'


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Nashville Warbler"
        self.clicks = 0
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(QSize(1920, 1080))
        
        self.label = QLabel(self)
        self.pixmap = QPixmap(pic1)
        self.label.setPixmap(self.pixmap)
        
        self.button = QPushButton('--->', self)
        self.button.setGeometry(100,100,200,100)
        self.button.setStyleSheet("font-size:50px;")
        self.button.move(1700, 900)
        self.button.clicked.connect(self.right_button_click)
        
        
        self.show()
        
        
    def right_button_click(self):
        if self.clicks < 1:
            self.clicks = self.clicks + 1
            self.pixmap = QPixmap(pic2)
            self.label.setPixmap(self.pixmap)
        elif self.clicks < 2:
            self.clicks = self.clicks + 1
            self.pixmap = QPixmap(pic3)
            self.label.setPixmap(self.pixmap)
        else:
            self.clicks = 0
            self.pixmap = QPixmap(pic1)
            self.label.setPixmap(self.pixmap)
        self.show()
      
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
