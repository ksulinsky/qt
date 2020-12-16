import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *


class ProgressBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count =0
        self.setFixedSize(500, 500)
        self.progressBar = QProgressBar(self)
        self.progressBar.move(5, 5)
        self.progressBar.setValue(0)

        self.lista = QListWidget()
        self.lista.addItem("python")
        # self.lista.move(5,200)
        self.lista.show()


        self.btnDodaj = QPushButton("Dodaj",self)
        self.btnDodaj.move(120,40)
        self.btnDodaj.clicked.connect(self.dodawanie)


        self.nazwaObiektu = QLineEdit("",self)
        self.nazwaObiektu.move(5,40)


        self.show()

        self.timer = QTimer()
        # self.timer.timeout.connect(self.TimeCount)
        # self.timer.start(100)



    def dodawanie(self):
        if self.count<10 and self.nazwaObiektu.text()!="":
            self.lista.addItem(self.nazwaObiektu.text())
            # print(self.lista.text())
            self.count = self.count + 1
            print("Dodano")

            self.timer.timeout.connect(self.TimeCount)
            self.timer.start(100)


        elif(self.nazwaObiektu.text() == ""):
            print("Obiekt musi miec nazwe")
        else:
            print("lista jest pelna")

    def TimeCount(self):
        value = self.progressBar.value()
        if value < 100:
            value = value +10
            self.progressBar.setValue(value)

            self.timer.stop()
        else:
            self.timer.stop()
            print("Mamy 100%")

app = QApplication(sys.argv)
window = ProgressBar()
sys.exit(app.exec_())