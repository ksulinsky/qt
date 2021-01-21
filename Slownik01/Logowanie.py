import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Rejestracja import Ui_Registration
from baza2 import Baza2



class Ui_Logowanie(object):
    def setupUi(self, Logowanie):
        Logowanie.setObjectName("Logowanie")
        Logowanie.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(Logowanie)
        self.centralwidget.setObjectName("centralwidget")

        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(229, 20, 201, 41))
        self.label_log.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        # font.setUnderline(True)
        font.setWeight(75)


        self.label_log.setFont(font)
        self.label_log.setOpenExternalLinks(False)
        self.label_log.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_log.setObjectName("label1")

        self.clbtn_registration = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.clbtn_registration.setGeometry(QtCore.QRect(170, 310, 261, 41))
        self.clbtn_registration.setObjectName("commandLinkButton")
        self.clbtn_registration.clicked.connect(self.goToRegistration)
        self.clbtn_registration.clicked.connect(Logowanie.close)

        self.btn_logIn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logIn.setGeometry(QtCore.QRect(260, 240, 91, 31))
        self.btn_logIn.setObjectName("pushButton")
        self.btn_logIn.setStyleSheet("QPushButton"
                             "{"
                             "background-color : green;"
                             "color : white;"
                              "border-radius: 10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightgreen;"
                             "}")
        self.btn_logIn.clicked.connect(self.logIn)
        self.btn_logIn.clicked.connect(Logowanie.close)


        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 80, 211, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.lineEdit_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_email.setStyleSheet("background-color: white;")
        self.verticalLayout.addWidget(self.lineEdit_email)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setStyleSheet("background-color: white;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_password)

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
        self.btn_back.clicked.connect(Logowanie.close)

        self.btn_back.setObjectName("pushButton")

        Logowanie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Logowanie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Logowanie.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(Logowanie)
        self.statusbar.setObjectName("statusbar")
        Logowanie.setStatusBar(self.statusbar)

        self.retranslateUi(Logowanie)
        QtCore.QMetaObject.connectSlotsByName(Logowanie)

    def retranslateUi(self, Logowanie):
        _translate = QtCore.QCoreApplication.translate
        Logowanie.setWindowTitle(_translate("Logowanie", "Logowanie"))
        Logowanie.setStyleSheet("background-color: '#CCCCFF';")
        self.label_log.setText(_translate("Logowanie", "LOGOWANIE"))
        self.clbtn_registration.setText(_translate("Logowanie", "Nie masz konta? Zarejestruj się"))
        self.btn_logIn.setText(_translate("Logowanie", "Zaloguj"))
        self.label.setText(_translate("Logowanie", "Login"))
        self.label_2.setText(_translate("Logowanie", "Hasło"))
        self.btn_back.setText(_translate("Logowanie", "Pwrót"))

    def goToRegistration(self):
        self.ui = Ui_Registration()


        self.window1 = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def goBack(self):

        from MainWindow import Ui_MainWindow
        self.ui1 = Ui_MainWindow()

        self.window2 = QtWidgets.QMainWindow()
        self.ui1.setupUi(self.window2)

        self.window2.show()
    def mesBox(self):
        self.mess = QtWidgets.QMessageBox()
        self.mess.setWindowTitle("Błąd")
        self.mess.setText("Nie zalogowano")
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


    def logIn(self):
        baza = Baza2()
        logged, uprawnienia = baza.zaloguj(self.lineEdit_email.text(),self.lineEdit_password.text())

        if (self.lineEdit_email.text()!="" or self.lineEdit_password.text() !=""):
            if(logged ==1 and uprawnienia==1):
                from UserMainWindow import Ui_UserMainWindow
                self.ui1 = Ui_UserMainWindow()
                self.window2 = QtWidgets.QMainWindow()
                self.ui1.setupUi(self.window2)
                self.window2.show()

            elif(logged==1 and uprawnienia==2):
                from AdminMainWindow import Ui_AdminMainWindow
                self.ui1 = Ui_AdminMainWindow()
                self.window2 = QtWidgets.QMainWindow()
                self.ui1.setupUi(self.window2)
                self.window2.show()
            else:
                print("niezalogowano")

                self.mesBox()


        else:
            print("niezalogowano")

            self.mesBox()




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Logowanie = QtWidgets.QMainWindow()
    ui = Ui_Logowanie()
    ui.setupUi(Logowanie)
    Logowanie.show()
    sys.exit(app.exec_())
