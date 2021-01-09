import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Definicja import Ui_ShowDefinition
from Logowanie import Ui_Logowanie
from baza2 import Baza2

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.showDef = Ui_ShowDefinition()

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(200, 0, 240, 70)
        self.label1.setBaseSize(QtCore.QSize(10, 10))

        font = QtGui.QFont("Cascada Code PL", 20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setOpenExternalLinks(False)
        self.label1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label1.setObjectName("label1")

        #zaloguj----------------------
        self.btn_zaloguj = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zaloguj.setGeometry(QtCore.QRect(560, 0, 75, 23))
        self.btn_zaloguj.setObjectName("btn_zaloguj")
        self.btn_zaloguj.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : green;"
                                     "color : white;"
                                     "border-radius: 10px;"
                                     "}"
                                     "QPushButton::pressed"
                                     "{"
                                     "background-color : lightgreen;"
                                     "}")
        self.btn_zaloguj.clicked.connect(self.logowanie)
        self.btn_zaloguj.clicked.connect(MainWindow.close)


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 400, 140))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # pojęcie----------------------------------------------------------------------------
        self.lineEdit_pojecie = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_pojecie.setObjectName("lineEdit_pojecie")
        self.horizontalLayout.addWidget(self.lineEdit_pojecie)

        #szukaj------------------------------------------
        self.btn_szukaj = QtWidgets.QPushButton(self.centralwidget)
        self.btn_szukaj.setGeometry(QtCore.QRect(418, 199, 75, 23))
        self.btn_szukaj.setObjectName("btn_szukaj")
        self.btn_szukaj.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : '#FBA40A';"
                                      "border-radius: 10px;"
                                      "color : white;"
                                      "}"
                                      )
        self.btn_szukaj.clicked.connect(self.passingInformation)
        self.btn_szukaj.clicked.connect(MainWindow.close)

        # self.horizontalLayout.addWidget(self.btn_szukaj)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 280, 241, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # -----losowanie-----------
        self.btn_losuj = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_losuj.setObjectName("btn_losuj")
        self.btn_losuj.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : '#66CC66';"
                                     # "border-radius: 10px;"'#F6D542'
                                     "color : black;"
                                     "}"
                                     )
        self.verticalLayout.addWidget(self.btn_losuj)
        self.btn_losuj.clicked.connect(self.losowanie)
        self.btn_losuj.clicked.connect(MainWindow.close)

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Python - Słownik"))
        self.btn_zaloguj.setText(_translate("MainWindow", "Zaloguj"))
        self.label_2.setText(_translate("MainWindow", "Wyszukaj pojęcie: "))
        self.btn_szukaj.setText(_translate("MainWindow", "Szukaj"))
        self.btn_losuj.setText(_translate("MainWindow", "Losuj pojęcie"))


    def logowanie(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Logowanie()
        self.ui.setupUi(self.window)
        self.window.show()

    def passingInformation(self):
        self.ui = Ui_ShowDefinition()
        self.ui.pojecie = self.lineEdit_pojecie.text()

        baza = Baza2()
        self.trescTemp = baza.get_tresc(self.ui.pojecie)
        self.ui.tresc = self.trescTemp[0]
        self.ui.click = 0

        self.window1 = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()
    def losowanie(self):
        self.ui = Ui_ShowDefinition()

        baza = Baza2()
        self.string1, self.string2 = baza.losowe_pojecie()
        self.trescTemp = baza.get_tresc(self.string1)

        self.ui.pojecie = self.string1
        self.ui.tresc = self.trescTemp[0]
        self.ui.click =0


        self.window1 = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()



    def zamknij(self):
        self.choice = QMessageBox.Question(self,'Czy chcesz wyjść z aplikacji?',
                                      QMessageBox.Yes | QMessageBox.No)


        if self.choice == QMessageBox.Yes:
            MainWindow.close()

        elif self.choice == QMessageBox.No:
            print('Kontynuuje dzialanie.')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
