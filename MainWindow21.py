# Form implementation generated from reading ui file 'D:\UEL\KyThuatLapTrinh\Chuong1_Ham\baitap21\ui\MainWindow21.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 70, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 140, 511, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(224, 255, 174);")
        self.groupBox.setObjectName("groupBox")
        self.label_N = QtWidgets.QLabel(parent=self.groupBox)
        self.label_N.setGeometry(QtCore.QRect(20, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_N.setFont(font)
        self.label_N.setObjectName("label_N")
        self.lineEditN = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditN.setGeometry(QtCore.QRect(120, 40, 261, 20))
        self.lineEditN.setStyleSheet("background-color: rgb(255, 170, 255);\n"
"background-color: rgb(207, 255, 247);")
        self.lineEditN.setObjectName("lineEditN")
        self.lineEditK = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditK.setGeometry(QtCore.QRect(120, 80, 261, 20))
        self.lineEditK.setStyleSheet("background-color: rgb(207, 255, 247);")
        self.lineEditK.setObjectName("lineEditK")
        self.label_K = QtWidgets.QLabel(parent=self.groupBox)
        self.label_K.setGeometry(QtCore.QRect(20, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_K.setFont(font)
        self.label_K.setObjectName("label_K")
        self.pushButtonThucHien = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonThucHien.setGeometry(QtCore.QRect(280, 320, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonThucHien.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\UEL\\KyThuatLapTrinh\\Chuong1_Ham\\baitap21\\ui\\../../../../TuDuyLapTrinh/2530802_cog_gear_general_machine_office_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonThucHien.setIcon(icon)
        self.pushButtonThucHien.setObjectName("pushButtonThucHien")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(90, 370, 511, 151))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(224, 255, 174);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_A = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_A.setGeometry(QtCore.QRect(20, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_A.setFont(font)
        self.label_A.setObjectName("label_A")
        self.lineEditA = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditA.setGeometry(QtCore.QRect(140, 40, 251, 20))
        self.lineEditA.setStyleSheet("background-color: rgb(207, 255, 247);")
        self.lineEditA.setObjectName("lineEditA")
        self.lineEditC = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditC.setGeometry(QtCore.QRect(140, 80, 251, 20))
        self.lineEditC.setStyleSheet("background-color: rgb(207, 255, 247);")
        self.lineEditC.setObjectName("lineEditC")
        self.label_C = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_C.setGeometry(QtCore.QRect(20, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_C.setFont(font)
        self.label_C.setObjectName("label_C")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditN, self.lineEditK)
        MainWindow.setTabOrder(self.lineEditK, self.pushButtonThucHien)
        MainWindow.setTabOrder(self.pushButtonThucHien, self.lineEditA)
        MainWindow.setTabOrder(self.lineEditA, self.lineEditC)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phan Ngoc Bao Chau - Bai 21"))
        self.label.setText(_translate("MainWindow", "Chỉnh Hợp - Tổ Hợp"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập K và N:"))
        self.label_N.setText(_translate("MainWindow", "Nhập N:"))
        self.label_K.setText(_translate("MainWindow", "Nhập K:"))
        self.pushButtonThucHien.setText(_translate("MainWindow", "Thực hiện"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Kết quả:"))
        self.label_A.setText(_translate("MainWindow", "Chỉnh Hợp A:"))
        self.label_C.setText(_translate("MainWindow", "Tổ Hợp C:"))
