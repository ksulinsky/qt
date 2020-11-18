import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__ (self):
        super().__init__()
        self.name = "Moja aplikacja"
        self.initUI()

    def initUI(self):
        self.setFixedSize(300,300)
        self.setGeometry(0,0,300,300)

        gridLayout = QGridLayout(self)
        i=1
        while i<10:
            btn = QPushButton(str(i), self)

            gridLayout.addWidget(btn,0,i)

            if i>3 and i<=6:
                gridLayout.addWidget(btn, 1, i-3)
            elif i>6:
                gridLayout.addWidget(btn, 2, i-6)
            i += 1

        self.setWindowTitle(self.name)
        self.show()

app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())