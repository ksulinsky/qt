from PyQt5 import QtCore, QtGui, QtWidgets
from baza2 import Baza2
click1=1
class Ui_Dodawanie(object):
    def setupUi(self, Dodawanie):
        global click1
        Dodawanie.setObjectName("MainWindow")
        Dodawanie.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Dodawanie)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(70, 120, 141, 21))
        self.lineEdit_name.setObjectName("lineEdit")

        self.lineEdit_def = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_def.setGeometry(QtCore.QRect(70, 190, 321, 131))
        self.lineEdit_def.setObjectName("lineEdit_2")

        # ----zatwierdz------------
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(70, 350, 111, 31))
        self.btn_add.setObjectName("pushButton")
        self.btn_add.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : green;"
                                     "color : white;"
                                     "border-radius: 10px;"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color : lightgreen;"
                                     "}")
        self.btn_add.clicked.connect(self.add)
        self.btn_add.clicked.connect(Dodawanie.close)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # ----POWRÓT--------------
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(540, 400, 75, 23))
        self.btn_back.setObjectName("pushButton_2")
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
        self.btn_back.clicked.connect(self.goBack)
        self.btn_back.clicked.connect(Dodawanie.close)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 160, 61, 21))
        self.label_3.setObjectName("label_3")
        Dodawanie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dodawanie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Dodawanie.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dodawanie)
        self.statusbar.setObjectName("statusbar")
        Dodawanie.setStatusBar(self.statusbar)

        self.retranslateUi(Dodawanie)
        QtCore.QMetaObject.connectSlotsByName(Dodawanie)

    def retranslateUi(self, Dodawanie):
        _translate = QtCore.QCoreApplication.translate
        Dodawanie.setWindowTitle(_translate("Dodawanie", "Dodawanie Pojęcia"))
        self.btn_add.setText(_translate("Dodawanie", "Zatwierdź"))
        self.label.setText(_translate("Dodawanie", "Dodaj pojęcie do bazy"))
        self.btn_back.setText(_translate("Dodawanie", "Pwrót"))
        self.label_2.setText(_translate("Dodawanie", "Nazwa:"))
        self.label_3.setText(_translate("Dodawanie", "Definicja:"))

    def goBack(self):
        if (self.click1 == 2):
            from AdminMainWindow import Ui_AdminMainWindow
            self.ui1 = Ui_AdminMainWindow()
            self.window2 = QtWidgets.QMainWindow()
            self.ui1.setupUi(self.window2)
            self.window2.show()
        else:
            from UserMainWindow import Ui_UserMainWindow
            self.ui1 = Ui_UserMainWindow()
            self.window2 = QtWidgets.QMainWindow()
            self.ui1.setupUi(self.window2)
            self.window2.show()

    def mesBox(self):
        self.mess = QtWidgets.QMessageBox()
        self.mess.setWindowTitle("Dodano")
        self.mess.setText("Dodano do bazy")
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
        self.goBack()

    def add(self):
        baza= Baza2()
        if (self.click1 == 1):
            baza.wstaw_pojecie_user(self.lineEdit_name.text(),
                                    self.lineEdit_def.text())

        else:
            baza.wstaw_pojecie_admin(self.lineEdit_name.text(),
                                    self.lineEdit_def.text())
        self.mesBox()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dodawanie = QtWidgets.QMainWindow()
    ui = Ui_Dodawanie()
    ui.setupUi(Dodawanie)
    Dodawanie.show()
    sys.exit(app.exec_())
