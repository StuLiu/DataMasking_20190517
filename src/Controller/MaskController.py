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
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
from src.utils import append_zero, encrypt, decrypt, save_map, load_map, read_data
class MaskController():

	def __init__(self):
		self.mainWindow = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.mainWindow)
		self.ui.pushButton_export.clicked.connect(lambda: self._do_masking())
		self.ui.pushButton_browse.clicked.connect(lambda: self._browse_file())

	@pyqtSlot()
	def _do_masking(self):
		try:
			print('do masking')
			# create mapping dict, keys are the masked private msg, and the values are the public check results
			mapping_dict = dict()
			# get key and dir's abs_path
			key_str = self._get_key()
			file_path = self._get_path()
			print(key_str, file_path)
			# get data
			data_private, data_public = read_data(file_path)
			print('data_private:', data_private)
			print('data_public:', data_public)
			# encrypt data
			data_private_masked = encrypt(key_str=key_str, data_str=data_private)
			# mapping dict add
			mapping_dict[data_private_masked] = data_public
			save_map('output.pkl', mapping_dict)

			overproof_data = load_map('output.pkl')
			print(overproof_data)
			data_private_recovered = decrypt(key_str=key_str, data_bytes=list(overproof_data.keys())[0])
			assert data_private_recovered == data_private
			print('data_private_recovered:', data_private_recovered)
		except Exception as e:
			print(e)

	@pyqtSlot()
	def _browse_dir(self):
		selected_path = QFileDialog.getExistingDirectory(caption="浏览", directory="./data")
		self.ui.lineEdit_dir.setText(selected_path)

	@pyqtSlot()
	def _browse_file(self):
		selected_path = QFileDialog.getOpenFileName(caption="浏览", directory="./data")
		self.ui.lineEdit_dir.setText(selected_path[0])

	def _get_path(self):
		dir_path = self.ui.lineEdit_dir.text()
		if len(dir_path) <= 0:
			raise Exception('Please browse the data file or directory!')
		else:
			return dir_path

	def _get_key(self):
		return append_zero(self.ui.lineEdit_key.text())