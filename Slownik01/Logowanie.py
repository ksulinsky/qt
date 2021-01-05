from PyQt5 import QtCore, QtGui, QtWidgets
from Rejestracja import Ui_Registration



class Ui_Logowanie(object):
    def setupUi(self, Logowanie):
        Logowanie.setObjectName("Logowanie")
        Logowanie.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(Logowanie)
        self.centralwidget.setObjectName("centralwidget")

        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(270, 20, 81, 41))
        self.label_log.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 240, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 80, 211, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        # powrót--------------------------------------------------------
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(560, 410, 75, 23))
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
        Logowanie.setWindowTitle(_translate("Logowanie", "MainWindow"))
        self.label_log.setText(_translate("Logowanie", "LOGOWANIE"))
        self.clbtn_registration.setText(_translate("Logowanie", "Nie masz konta? Zarejestruj się"))
        self.pushButton.setText(_translate("Logowanie", "Zaloguj"))
        self.label.setText(_translate("Logowanie", "E-mail"))
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Logowanie = QtWidgets.QMainWindow()
    ui = Ui_Logowanie()
    ui.setupUi(Logowanie)
    Logowanie.show()
    sys.exit(app.exec_())
