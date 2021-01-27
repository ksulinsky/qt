from PyQt5 import QtCore, QtGui, QtWidgets
from baza2 import Baza2



class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(229, 20, 201, 41))

        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 70, 201, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_email.setStyleSheet("background-color: white;")
        self.verticalLayout.addWidget(self.lineEdit_email)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setStyleSheet("background-color: white;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_login = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_login.setObjectName("lineEdit_confirmPassword")
        self.lineEdit_login.setStyleSheet("background-color: white;")
        self.verticalLayout.addWidget(self.lineEdit_login)

        # ----stworz-------------------
        self.btn_regist = QtWidgets.QPushButton(self.centralwidget)
        self.btn_regist.setGeometry(QtCore.QRect(260, 260, 101, 31))
        self.btn_regist.setObjectName("btn_regist")
        self.btn_regist.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : green;"
                                     "color : white;"
                                     "border-radius: 10px;"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color : lightgreen;"
                                     "}")
        self.btn_regist.clicked.connect(self.signUp)
        self.btn_regist.clicked.connect(Registration.close)

        # powrót--------------------------------------------------------
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
        self.btn_back.clicked.connect(self.goBack)
        self.btn_back.clicked.connect(Registration.close)

        self.btn_back.setObjectName("pushButton")

        Registration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Registration)
        self.statusbar.setObjectName("statusbar")
        Registration.setStatusBar(self.statusbar)

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Rejestracja"))
        Registration.setStyleSheet("background-color: '#CCCCFF';")
        self.label.setText(_translate("Registration", "STWÓRZ KONTO"))
        self.label_2.setText(_translate("Registration", "E-mail"))
        self.label_3.setText(_translate("Registration", "Hasło"))
        self.label_4.setText(_translate("Registration", "Wybierz login"))
        self.btn_regist.setText(_translate("Registration", "Stwórz"))
        self.btn_back.setText(_translate("Registration", "Powrót"))

    def goBack(self):
        from Logowanie import Ui_Logowanie
        self.ui1 = Ui_Logowanie()
        self.window2 = QtWidgets.QMainWindow()
        self.ui1.setupUi(self.window2)
        self.window2.show()

    def mesBox(self):
        self.mess = QtWidgets.QMessageBox()
        self.mess.setWindowTitle("Błąd")
        self.mess.setText("Nie utworzono!")
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


    def signUp(self):
        baza = Baza2()
        if (self.lineEdit_login.text() != "" and self.lineEdit_email.text() != ""
                and self.lineEdit_password.text() != ""):
            baza.zarejestruj(self.lineEdit_login.text(),
                             self.lineEdit_password.text(), self.lineEdit_email.text())
            self.goBack()
        else:
            self.mesBox()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QMainWindow()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
