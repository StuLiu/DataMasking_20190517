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
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QWidget
from PyQt5.QtCore import pyqtSlot
from src.utils import append_zero, do_encrypt, do_decrypt, read_xlsx, save_xlsx, save_pickle, load_pickle

class MaskController():

	def __init__(self):
		self.mainWindow = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.mainWindow)
		self.ui.pushButton_export.clicked.connect(lambda: self._do_masking())
		self.ui.pushButton_browse.clicked.connect(lambda: self._browse_file())
		self.ui.pushButton_import.clicked.connect(lambda: self._do_demasking())

	@pyqtSlot()
	def _do_masking(self):
		try:
			print('do masking')
			# create mapping dict, keys are the hash of the values, and the values are the encrypt bytes
			mapping_dict = dict()
			encrypt_data_dict = {}
			# get key and dir's abs_path
			key_str = self._get_key()
			file_path = self._get_path()
			print(key_str, file_path)
			# get data
			data_dict = read_xlsx(file_path)
			for year, sheet_data in data_dict.items():
				# encrypt data
				year_, data_rows, hash_bytes = do_encrypt(key_str, list(sheet_data.copy()), year)
				encrypt_data_dict[year_] = data_rows
				mapping_dict.update(hash_bytes)
			pass
			QMessageBox.information(QWidget(), "Information", "数据脱敏完成")
			write_path = QFileDialog.getSaveFileName(caption="保存为.xlsx文档", directory="./")[0]
			# write_path = './加密数据.xlsx'
			print(write_path)

			save_pickle('mapping.pkl', mapping_dict)
			save_xlsx(write_path, encrypt_data_dict)


			# # mapping dict add
			# mapping_dict[data_private_masked] = data_public
			# save_pickle('../data/data_masked.pkl', mapping_dict)
			#
			# QMessageBox.information(QWidget(), "Information", "脱敏成功")
			#
			# overproof_data = load_pickle('../data/data_masked.pkl')
			# print(overproof_data)
			# data_private_recovered = decrypt(key_str=key_str, data_bytes=list(overproof_data.keys())[0])
			# assert data_private_recovered == data_private
			# print('data_private_recovered:', data_private_recovered)
		except Exception as e:
			QMessageBox.warning(QWidget(), "warning", str(e))
			print(e)

	@pyqtSlot()
	def _do_demasking(self):
		try:
			print('do import')
			# get key and dir's abs_path
			key_str = self._get_key()
			file_path = self._get_path()
			print(key_str, file_path)

			data_dict_enc = read_xlsx(file_path)
			hash_bytes = load_pickle('mapping.pkl')
			data_dict_origin = {}
			for year, data_rows in data_dict_enc.items():
				_, data_rows_origin =  do_decrypt(key_str, data_rows, year, hash_bytes)
				data_dict_origin[year] = data_rows_origin
			write_path = QFileDialog.getSaveFileName(caption="保存为.xlsx文档", directory="./")[0]
			save_xlsx(write_path, data_dict_origin)
			QMessageBox.information(QWidget(), "Information", "解密成功")
		except Exception as e:
			QMessageBox.warning(QWidget(), "warning", str(e))
			print(e)


	@pyqtSlot()
	def _browse_dir(self):
		selected_path = QFileDialog.getExistingDirectory(caption="浏览", directory="./")
		self.ui.lineEdit_dir.setText(selected_path)

	@pyqtSlot()
	def _browse_file(self):
		selected_path = QFileDialog.getOpenFileName(caption="浏览", directory="./")
		self.ui.lineEdit_dir.setText(selected_path[0])

	def _get_path(self):
		dir_path = self.ui.lineEdit_dir.text()
		if len(dir_path) <= 0:
			raise Exception('请选择要加密导出的文件!')
		else:
			return dir_path

	def _get_key(self):
		return append_zero(self.ui.lineEdit_key.text())