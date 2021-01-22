import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QListWidget, QLineEdit, QLabel
from Definicja import Ui_ShowDefinition
from Logowanie import Ui_Logowanie
from DodawaniePojecia import Ui_Dodawanie
from DefinicjaAdmin import Ui_ShowDefinitionAdmin
from baza2 import Baza2

class Ui_AdminMainWindow(object):

    def setupUi(self, AdminMainWindow):

        AdminMainWindow.setObjectName("UserMainWindow")
        AdminMainWindow.resize(639, 477)
        self.centralwidget = QtWidgets.QWidget(AdminMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        image = QPixmap('python-logo.png')
        imageLabel = QLabel(self.centralwidget)
        imageLabel.setScaledContents(True)
        image.scaled(105, 50)
        imageLabel.setPixmap(image)

        imageLabel.move(390, 320)

        self.showDef = Ui_ShowDefinition()

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(200, 0, 240, 70)
        self.label1.setBaseSize(QtCore.QSize(10, 10))

        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(20)
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
        self.btn_zaloguj.clicked.connect(self.logowanie)
        self.btn_zaloguj.clicked.connect(AdminMainWindow.close)
        self.btn_zaloguj.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : black;"
                                      "border-radius: 10px;"
                                      "color : white;"
                                      "}"
                                      )

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 400, 140))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
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
        self.lineEdit_pojecie.setStyleSheet("background-color: '#CCFFFF';")
        self.horizontalLayout.addWidget(self.lineEdit_pojecie)

        #szukaj------------------------------------------
        self.btn_szukaj = QtWidgets.QPushButton(self.centralwidget)
        self.btn_szukaj.setGeometry(QtCore.QRect(418, 178, 75, 23))

        self.btn_szukaj.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : '#FBA40A';"
                                      "border-radius: 10px;"
                                      "color : white;"
                                      "}"
                                      )
        self.btn_szukaj.clicked.connect(self.passingInformation)
        self.btn_szukaj.clicked.connect(AdminMainWindow.close)
        self.btn_szukaj.setObjectName("QPushButton")
        # self.horizontalLayout.addWidget(self.btn_szukaj)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 241, 170))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # ---LISTA-------------
        self.baza1 = Baza2()
        self.lista = self.baza1.lista_pojec()

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("background-color : '#FFFF99';")
        for i in self.lista:
            self.comboBox.addItem(i)

        self.verticalLayout.addWidget(self.comboBox)

        # -----SZUKAJ Z LISTY-----------
        self.btn_szukajZListy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_szukajZListy.setObjectName("btn_szukajZListy")
        self.btn_szukajZListy.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : '#FFFF66';"
                                     
                                     "color : black;"
                                     "}"
                                     )
        self.verticalLayout.addWidget(self.btn_szukajZListy)
        self.btn_szukajZListy.clicked.connect(self.szukajZListy)
        self.btn_szukajZListy.clicked.connect(AdminMainWindow.close)

        # -----losowanie-----------
        self.btn_losuj = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_losuj.setObjectName("btn_losuj")
        self.btn_losuj.setStyleSheet("QPushButton"
                                      "{"
                                      "background-color : '#FFFF33';"
                                      # "border-radius: 10px;"'#F6D542'
                                      "color : black;"
                                      "}"
                                      )
        self.verticalLayout.addWidget(self.btn_losuj)
        self.btn_losuj.clicked.connect(self.losowanie)
        self.btn_losuj.clicked.connect(AdminMainWindow.close)


        # -----dodaj pojecie do bazy-----------
        self.btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setStyleSheet("QPushButton"
                                     "{"
                                     "background-color : '#FFFF00';"
                                     # "border-radius: 10px;"'#F6D542'
                                     "color : black;"
                                     "}"
                                     )
        self.verticalLayout.addWidget(self.btn_add)
        self.btn_add.clicked.connect(self.add)
        self.btn_add.clicked.connect(AdminMainWindow.close)

        # -----------pojecia do akceptacji--------
        self.btn_accept = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_accept.setObjectName("btn_accept")
        self.btn_accept.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : '#FFCC33';"
                                   # "border-radius: 10px;"'#F6D542'
                                   "color : black;"
                                   "}"
                                   )
        self.verticalLayout.addWidget(self.btn_accept)
        self.btn_accept.clicked.connect(self.showAccept)
        # self.btn_accept.clicked.connect(AdminMainWindow.close)

        self.list_accept = QListWidget()
        self.list_accept.setWindowTitle("Do akceptacji")




        AdminMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        AdminMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminMainWindow)
        self.statusbar.setObjectName("statusbar")
        AdminMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminMainWindow)

    def retranslateUi(self, AdminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminMainWindow.setWindowTitle(_translate("AdminMainWindow", "Panel Administratora"))
        AdminMainWindow.setStyleSheet("background-color: '#99CCFF';")
        self.label1.setText(_translate("AdminMainWindow", "Python - Słownik"))
        self.btn_zaloguj.setText(_translate("AdminMainWindow", "Wyloguj"))
        self.label_2.setText(_translate("AdminMainWindow", "Wyszukaj pojęcie: "))
        self.btn_szukaj.setText(_translate("AdminMainWindow", "Szukaj"))
        self.btn_losuj.setText(_translate("AdminMainWindow", "Losuj pojęcie"))
        self.btn_szukajZListy.setText(_translate("AdminMainWindow", "Szukaj z listy"))
        self.btn_add.setText(_translate("AdminMainWindow", "Dodaj pojęcie"))
        self.btn_accept.setText(_translate("AdminMainWindow", "Pojęcia do akceptacji"))


    def listaTresc(self):

        self.item=self.list_accept.currentItem()
        print(str(self.item.text()))
        self.defi = self.baza1.get_tresc_akceptacja(str(self.item.text()))
        print(self.defi[0])

        from Akceptacja import Ui_Akceptacja
        self.ui = Ui_Akceptacja()
        self.ui.pojecie = str(self.item.text())
        self.ui.tresc = self.defi[0]
        self.ui.click = 2

        self.window1 = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()



    def showAccept(self):
        self.baza3 = Baza2()
        self.list_accept.clear()
        self.fields = self.baza3.wyswietl_akceptacja()

        for i in self.fields:
            self.list_accept.addItem(str(i))

        self.list_accept.show()
        self.list_accept.clicked.connect(self.listaTresc)
        self.list_accept.clicked.connect(self.list_accept.close)

    def szukajZListy(self):
        self.ui = Ui_ShowDefinitionAdmin()
        self.ui.pojecie = self.comboBox.currentText()

        baza = Baza2()
        self.trescTemp = baza.get_tresc(self.ui.pojecie)
        self.ui.tresc = self.trescTemp[0]
        self.ui.click = 2

        self.window1 = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def logowanie(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Logowanie()
        self.ui.setupUi(self.window)
        self.window.show()

    def passingInformation(self):

        self.ui = Ui_ShowDefinitionAdmin()
        self.ui.pojecie = self.lineEdit_pojecie.text()

        baza = Baza2()
        self.trescTemp = baza.get_tresc(self.ui.pojecie)
        self.ui.tresc = self.trescTemp[0]
        self.ui.click = 2

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
        self.ui.click = 2 #zaznaczam ze losowanie w userze kliknieto zeby wrocic do panelu usera

        self.window1 = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()

    def add(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dodawanie()
        self.ui.setupUi(self.window)
        self.ui.click1 = 2
        self.window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    AdminMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminMainWindow()
    ui.setupUi(AdminMainWindow)
    AdminMainWindow.show()
    sys.exit(app.exec_())
