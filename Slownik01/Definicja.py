
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
import sys

pojecie = None
tresc =None
click=1

class Ui_ShowDefinition(object):
    global pojecie, tresc,click

    def setupUi(self, ShowDefinition):
        ShowDefinition.setObjectName("ShowDefinition")
        ShowDefinition.resize(640, 480)

        #layout = QVBoxLayout()
        self.centralwidget = QtWidgets.QWidget(ShowDefinition)
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
        self.btn_back.clicked.connect(ShowDefinition.close)

        self.btn_back.setObjectName("pushButton")

        self.definicja = QtWidgets.QLabel(ShowDefinition)
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

        # pojecie--------------------
        self.poj = QtWidgets.QLabel(ShowDefinition)
        self.poj.setText(self.pojecie)
        self.poj.setGeometry(QtCore.QRect(155, 10, 211, 51))
        self.poj.setStyleSheet("background-color: white")
        self.poj.setFixedSize(340, 60)

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

        ShowDefinition.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShowDefinition)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        ShowDefinition.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShowDefinition)
        self.statusbar.setObjectName("statusbar")
        ShowDefinition.setStatusBar(self.statusbar)

        self.retranslateUi(ShowDefinition)
        QtCore.QMetaObject.connectSlotsByName(ShowDefinition)

    def retranslateUi(self, ShowDefinition):
        _translate = QtCore.QCoreApplication.translate
        ShowDefinition.setWindowTitle(_translate("ShowDefinition", "Definicja"))
        ShowDefinition.setStyleSheet("background-color: '#FAF2B6';")
        self.btn_back.setText(_translate("ShowDefinition", "Powrót"))

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
    ShowDefinition = QtWidgets.QMainWindow()
    ui = Ui_ShowDefinition()
    ui.setupUi(ShowDefinition)
    ShowDefinition.show()
    sys.exit(app.exec_())
