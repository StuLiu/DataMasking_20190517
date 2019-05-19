'''
--------------------------------------------------------
@File    :   MaskerQMainWindow.py    
@Contact :   1183862787@qq.com
@License :   (C)Copyright 2017-2018, CS, WHU

@Modify Time : 2019/5/19 9:21     
@Author      : Liu Wang    
@Version     : 1.0   
@Desciption  : None
--------------------------------------------------------  
''' 

from Viewer.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot

class MaskController():

	def __init__(self):
		self.mainWindow = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.mainWindow)
		self.ui.pushButton_OK.clicked.connect(lambda :self.print_key())
		self.ui.pushButton_OK.clicked.connect(lambda: self.print_path())
		self.ui.pushButton_OK.clicked.connect(lambda: self.do_masking())

	@pyqtSlot()
	def print_key(self):
		key_str = self.ui.lineEdit_key.text()
		print(key_str)

	@pyqtSlot()
	def print_path(self):
		print('path_str')

	@pyqtSlot()
	def do_masking(self):
		print('do masking')
		key_str = self.ui.lineEdit_key.text()

		pass


