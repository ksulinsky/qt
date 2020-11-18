import sys

from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, \
    QPushButton, QMessageBox


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Moja aplikacja'
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 300)
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle(self.name)

        buttonMsg = QPushButton('Co chcesz zrobić?', self)
        buttonMsg.resize(150, 25)
        buttonMsg.move(100, 150)
        buttonMsg.clicked.connect(self.showMsg)

        self.show()

    def showMsg(self):

        choice = QMessageBox.question(self, 'Definitywnie', 'Czy chcesz wyjść z aplikacji?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if choice == QMessageBox.Yes:
            sys.exit(0)

        elif choice == QMessageBox.No:
            print('Kontynuuje dzialanie.')

    def showStatus(self, status):
        print('Status przycisku:', status.text())




app = QApplication(sys.argv)
ex = MyWindow()
sys.exit(app.exec_())