from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 111, 31))

        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
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
        self.verticalLayout.addWidget(self.lineEdit_email)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_confirmPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_confirmPassword.setObjectName("lineEdit_confirmPassword")
        self.verticalLayout.addWidget(self.lineEdit_confirmPassword)

        self.btn_regist = QtWidgets.QPushButton(self.centralwidget)
        self.btn_regist.setGeometry(QtCore.QRect(260, 260, 101, 21))
        self.btn_regist.setObjectName("btn_regist")

        # powrót--------------------------------------------------------
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(560, 410, 75, 23))
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
        self.label.setText(_translate("Registration", "STWÓRZ KONTO"))
        self.label_2.setText(_translate("Registration", "E-mail"))
        self.label_3.setText(_translate("Registration", "Hasło"))
        self.label_4.setText(_translate("Registration", "Powtórz hasło"))
        self.btn_regist.setText(_translate("Registration", "Stwórz"))
        self.btn_back.setText(_translate("Registration", "Pwrót"))

    def goBack(self):
        from Logowanie import Ui_Logowanie
        self.ui1 = Ui_Logowanie()
        self.window2 = QtWidgets.QMainWindow()
        self.ui1.setupUi(self.window2)
        self.window2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QMainWindow()
    ui = Ui_Registration()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())
