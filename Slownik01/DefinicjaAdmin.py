
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import sys
from baza2 import Baza2

pojecie = None
tresc =None
click=1

class Ui_ShowDefinitionAdmin(object):
    global pojecie, tresc,click

    def setupUi(self, ShowDefinitionAdmin):
        ShowDefinitionAdmin.setObjectName("ShowDefinition")
        ShowDefinitionAdmin.resize(640, 480)

        self.baza = Baza2()
        #layout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget(ShowDefinitionAdmin)
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
        self.btn_back.clicked.connect(self.goBack)
        self.btn_back.clicked.connect(ShowDefinitionAdmin.close)

        self.btn_back.setObjectName("pushButton")

        # ----  USUŃ  --------------------------------------------
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(480, 410, 75, 23))
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
        self.btn_delete.clicked.connect(ShowDefinitionAdmin.close)


        self.btn_delete.setObjectName("delete")


        # self.definicja = QtWidgets.QLineEdit(ShowDefinitionAdmin)
        # self.definicja.setText(self.tresc)
        # self.definicja.setGeometry(QtCore.QRect(110, 110, 421, 291))
        # self.definicja.setStyleSheet("background-color: white")

        self.definicja = QtWidgets.QLabel(ShowDefinitionAdmin)
        self.definicja.setText(self.tresc)
        self.definicja.setGeometry(QtCore.QRect(110, 110, 421, 291))
        self.definicja.setStyleSheet("background-color: white")

        font1 = QtGui.QFont()
        font1.setFamily("Lucida Fax")
        font1.setPointSize(10)
        font1.setItalic(False)
        font1.setWeight(75)
        self.definicja.setFont(font1)
        self.definicja.setAlignment(Qt.AlignCenter)
        self.definicja.setWordWrap(True)




        # self.textBrowser.setObjectName("textBrowser")
        #layout.addWidget(self.textBrowser)

        # pojecie--------------------
        self.poj = QtWidgets.QLabel(ShowDefinitionAdmin)
        self.poj.setText(self.pojecie)
        self.poj.setGeometry(QtCore.QRect(210, 10, 211, 51))
        self.poj.setStyleSheet("background-color: white")

        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.poj.setFont(font)
        self.poj.setAlignment(Qt.AlignCenter)

        #self.textBrowser_2.setObjectName("textBrowser_2")
        # layout.addWidget(self.textBrowser_2)

        ShowDefinitionAdmin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShowDefinitionAdmin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        ShowDefinitionAdmin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShowDefinitionAdmin)
        self.statusbar.setObjectName("statusbar")
        ShowDefinitionAdmin.setStatusBar(self.statusbar)

        self.retranslateUi(ShowDefinitionAdmin)
        QtCore.QMetaObject.connectSlotsByName(ShowDefinitionAdmin)

    def retranslateUi(self, ShowDefinition):
        _translate = QtCore.QCoreApplication.translate
        ShowDefinition.setWindowTitle(_translate("ShowDefinitionAdmin", "Definicja"))
        ShowDefinition.setStyleSheet("background-color: '#FAF2B6';")
        self.btn_back.setText(_translate("ShowDefinitionAdmin", "Pwrót"))
        self.btn_delete.setText(_translate("ShowDefinitionAdmin", "Usuń"))


    def delete(self):
        self.baza.usun_pojecie_admin(self.pojecie)

        self.mesBoxDelete()
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
        self.goBack()



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
    ShowDefinitionAdmin = QtWidgets.QMainWindow()
    ui = Ui_ShowDefinitionAdmin()
    ui.setupUi(ShowDefinitionAdmin)
    ShowDefinitionAdmin.show()
    sys.exit(app.exec_())
