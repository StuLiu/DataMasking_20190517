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
from utils import append_zero, encrypt, decrypt, save_map, load_map

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
		key_str = self._get_key()
		print(key_str)

	def _get_key(self)->str:
		return append_zero(self.ui.lineEdit_key.text())

	@pyqtSlot()
	def print_path(self):
		print('path_str')

	@pyqtSlot()
	def do_masking(self):
		print('do masking')
		# create mapping dict
		mapping_dict = dict()
		# get key
		key_str = self._get_key()
		# get data
		data_private = str('姓名 刘旺 性别 男')
		print('data_private:', data_private)
		# encrypt data
		data_private_masked = encrypt(key_str=key_str, data_str=data_private)
		# mapping dict add
		mapping_dict[str(hash(data_private_masked))] = data_private
		save_map('mapping.file', mapping_dict)
		print(load_map('mapping.file'))
		data_private_recovered = decrypt(key_str=key_str, data_bytes=data_private_masked)
		assert data_private_recovered == data_private
		print('data_private_recovered:', data_private_recovered)
		pass


