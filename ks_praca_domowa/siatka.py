import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Moja aplikacja'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)
        gridLayout = QGridLayout(self)
        licznik=1;
        for x in range(3):
                for y in range(3):
                    buttonConcat = QPushButton('%d' %licznik, self)
                    gridLayout.addWidget(buttonConcat, x, y)
                    licznik+=1
        licznik+=1
        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2





        self.setWindowTitle(self.name)
        self.show()




app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())
