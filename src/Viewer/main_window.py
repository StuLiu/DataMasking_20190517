# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 278)
        MainWindow.setMinimumSize(QtCore.QSize(463, 278))
        MainWindow.setMaximumSize(QtCore.QSize(463, 278))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export.setGeometry(QtCore.QRect(40, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setObjectName("pushButton_export")
        self.lineEdit_key = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_key.setGeometry(QtCore.QRect(100, 50, 321, 31))
        self.lineEdit_key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_key.setDragEnabled(False)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(340, 100, 81, 31))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.lineEdit_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_dir.setGeometry(QtCore.QRect(100, 100, 231, 31))
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import.setGeometry(QtCore.QRect(240, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton_import.setFont(font)
        self.pushButton_import.setObjectName("pushButton_import")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 200, 411, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据脱敏程序"))
        self.pushButton_export.setText(_translate("MainWindow", "加密"))
        self.label.setText(_translate("MainWindow", "密码："))
        self.pushButton_browse.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "文件："))
        self.pushButton_import.setText(_translate("MainWindow", "解密"))

