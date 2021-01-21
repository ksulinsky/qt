
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
from baza2 import Baza2

pojecie = None
tresc =None
click=1

class Ui_Akceptacja(object):
    global click
    tresc =""
    pojecie=""

    def setupUi(self, Akceptacja):
        Akceptacja.setObjectName("Akceptacja")
        Akceptacja.resize(640, 480)

        self.baza = Baza2()

        #layout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget(Akceptacja)
        self.centralwidget.setObjectName("centralwidget")

        #powrót--------------------------------------------------------
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(560, 410, 75, 23))
        self.btn_back.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color : blue;"
                                    "color : white;"
                                    "border-radius: 10px;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : lightblue;"
                                    "}")
        # self.btn_back.clicked.connect(self.goBack)
        self.btn_back.clicked.connect(Akceptacja.close)

        # -----  AKCEPTUJ  -----------------------------------
        self.btn_accept = QtWidgets.QPushButton(self.centralwidget)
        self.btn_accept.setGeometry(QtCore.QRect(470, 410, 75, 23))
        self.btn_accept.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color : green;"
                                    "color : white;"
                                    "border-radius: 10px;"
                                    "}"
                                    "QPushButton::pressed"
                                    "{"
                                    "background-color : lightblue;"
                                    "}")
        self.btn_accept.clicked.connect(self.accept)
        self.btn_accept.clicked.connect(Akceptacja.close)

        self.btn_accept.setObjectName("accept")

        # -----  DELETE  -----------------------------------
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(380, 410, 75, 23))
        self.btn_delete.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : red;"
                                      "color : white;"
                                      "border-radius: 10px;"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color : lightblue;"
                                      "}")
        self.btn_delete.clicked.connect(self.delete)
        self.btn_delete.clicked.connect(Akceptacja.close)

        self.btn_delete.setObjectName("delete")


        self.definicja = QtWidgets.QLineEdit(Akceptacja)
        self.definicja.setText(self.tresc)
        self.definicja.setGeometry(QtCore.QRect(110, 110, 421, 291))
        self.definicja.setStyleSheet("background-color: white")
        # self.textBrowser.setObjectName("textBrowser")
        #layout.addWidget(self.textBrowser)

        # pojecie--------------------
        self.poj = QtWidgets.QLineEdit(Akceptacja)
        self.poj.setText(self.pojecie)
        self.poj.setGeometry(QtCore.QRect(210, 10, 211, 51))
        self.poj.setStyleSheet("background-color: white")


        #self.textBrowser_2.setObjectName("textBrowser_2")
        # layout.addWidget(self.textBrowser_2)

        Akceptacja.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Akceptacja)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Akceptacja.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Akceptacja)
        self.statusbar.setObjectName("statusbar")
        Akceptacja.setStatusBar(self.statusbar)

        self.retranslateUi(Akceptacja)
        QtCore.QMetaObject.connectSlotsByName(Akceptacja)



    def retranslateUi(self, Akceptacja):
        _translate = QtCore.QCoreApplication.translate
        Akceptacja.setWindowTitle(_translate("Akceptacja", "Akceptacja pojęcia"))
        Akceptacja.setStyleSheet("background-color: '#FFF9C4';")
        self.btn_back.setText(_translate("Akceptacja", "Pwrót"))
        self.btn_accept.setText(_translate("Akceptacja", "Akceptuj"))
        self.btn_delete.setText(_translate("Akceptacja", "Usuń"))

    def mesBoxDelete(self):
        self.mess = QtWidgets.QMessageBox()
        self.mess.setWindowTitle("Usunięto")
        self.mess.setText("Usunięto z bazy")
        self.mess.setStyleSheet(
                                "QPushButton"
                                "{"
                                "background-color : red;"
                                "color : white;"
                                "}"
                                "QMessageBox"
                                "{"
                                "color : red;"
                                "}"
                                )
        self.mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.mess.exec_()
        # Akceptacja.close()

    def mesBoxAccept(self):
        self.mess = QtWidgets.QMessageBox()
        self.mess.setWindowTitle("Dodano")
        self.mess.setText("Zaakceptowano")
        self.mess.setStyleSheet(
                                "QPushButton"
                                "{"
                                "background-color : green;"
                                "color : white;"
                                "}"
                                "QMessageBox"
                                "{"
                                "color : red;"
                                "}"
                                )
        self.mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.mess.exec_()




    def delete(self):
        self.baza.usun_pojecie_admin(self.pojecie)
        self.mesBoxDelete()

    def accept(self):
        print("akceptacja")
        self.mesBoxAccept()
        # Akceptacja.close()


    def goBack(self):
        if(self.click==1):
            from UserMainWindow import Ui_UserMainWindow
            self.ui1 = Ui_UserMainWindow()
            self.window2 = QtWidgets.QMainWindow()
            self.ui1.setupUi(self.window2)
            self.window2.show()
        elif(self.click==2):
            from AdminMainWindow import Ui_AdminMainWindow
            self.ui1 = Ui_AdminMainWindow()
            self.window2 = QtWidgets.QMainWindow()
            self.ui1.setupUi(self.window2)
            self.window2.show()
        else:
            from MainWindow import Ui_MainWindow
            self.ui1 = Ui_MainWindow()
            self.window2 = QtWidgets.QMainWindow()
            self.ui1.setupUi(self.window2)
            self.window2.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Akceptacja = QtWidgets.QMainWindow()
    ui = Ui_Akceptacja()
    ui.setupUi(Akceptacja)
    Akceptacja.show()
    sys.exit(app.exec_())
