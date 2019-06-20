'''
--------------------------------------------------------
@File    :   masker.py    
@Contact :   1183862787@qq.com
@License :   (C)Copyright 2017-2018, CS, WHU

@Modify Time : 2019/5/18 23:51     
@Author      : Liu Wang    
@Version     : 1.0   
@Desciption  : None
--------------------------------------------------------  
'''

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
from openpyxl import load_workbook, Workbook
import pickle

def encrypt(key_str, data_str): # ->bytes
	if data_str == None:
		return None
	assert len(key_str) == 16
	key_bytes = bytes(key_str, encoding='utf-8')
	data_bytes = bytes(data_str, encoding='utf-8')
	crypt_sm4 = CryptSM4()
	crypt_sm4.set_key(key_bytes, SM4_ENCRYPT)
	return crypt_sm4.crypt_ecb(data_bytes)  # bytes类型

def decrypt(key_str, data_bytes):   # ->str
	if data_bytes == None:
		return None
	assert len(key_str) == 16
	key_bytes = bytes(key_str, encoding='utf-8')
	crypt_sm4 = CryptSM4()
	crypt_sm4.set_key(key_bytes, SM4_DECRYPT)
	decrypted_data = crypt_sm4.crypt_ecb(data_bytes)  # bytes类型
	return str(decrypted_data, encoding='utf-8')

def append_zero(key_str)->str:
	"""对不够16位的密码做补零处理"""
	if len(key_str) < 16:
		key_str += '0' * (16 - len(key_str))
	return key_str

def read_xlsx(file_path, have_head=True)->dict:
	result = {}
	wb = load_workbook(file_path)
	print('wb.sheetnames:',wb.sheetnames)
	for sheetname in wb.sheetnames:
		sheet = wb[sheetname]
		rows_list = []
		for row in sheet.values:
			rows_list.append(list(row))
		result[sheetname] = rows_list
	return result

def save_xlsx(file_path, data_dict)->None:
	wb = Workbook()
	for key, values in data_dict.items():
		print(key)
		for row in values:
			print(row)
		ws = wb.create_sheet(title=key)
		for row in values:
			ws.append(row)
	wb.save(file_path)

def save_pickle(file_name, dict_obj):
	assert type(dict_obj) == type(dict())
	with open(file_name, "wb") as file:
		pickle.dump(dict_obj, file)
	pass

def load_pickle(file_name)->dict:
	with open(file_name, "rb") as file:
		data = pickle.load(file)
		assert type(data) == type(dict())
		return data


def do_encrypt(key_str, data_rows, year)->(str, list):
	hash_bytes = {}     # the dict with key:hashcode and value:bytes
	if len(data_rows) <= 1:
		return year, [[]], hash_bytes
	if year == '17' or year == '18':
		indexs = [7, 20, 22, 24, 26, 33, 34, 39, 48, 53]    # 必须加密字段的下标
		# 处理条件加密字段
		for row in data_rows[1:]:
			if row[36] == '生产':
				encrypt_bytes = encrypt(key_str, str(row[0]))
				encrypt_hash = str(hash(encrypt_bytes))
				hash_bytes[encrypt_hash] = encrypt_bytes
				row[0] = encrypt_hash
				encrypt_bytes = encrypt(key_str, str(row[6]))
				encrypt_hash = str(hash(encrypt_bytes))
				hash_bytes[encrypt_hash] = encrypt_bytes
				row[6] = encrypt_hash
	else:
		indexs = []
	# 处理必须加密字段
	for row in data_rows[1:]:
		for index in indexs:
			encrypt_bytes = encrypt(key_str, str(row[index]))
			encrypt_hash = str(hash(encrypt_bytes))
			row[index] = encrypt_hash
			hash_bytes[encrypt_hash] = encrypt_bytes
	return year, data_rows, hash_bytes

def do_decrypt(key_str, data_rows, year, hash_bytes):
	"""data_rows:list()"""
	print(data_rows)
	if year == '17' or year == '18':
		indexs = [7, 20, 22, 24, 26, 33, 34, 39, 48, 53]    # 必须解密字段的下标
		# 处理条件加密字段
		for row in data_rows[1:]:
			if row[36] == '生产':
				row[0] = decrypt(key_str, hash_bytes[str(row[0])])
				row[6] = decrypt(key_str, hash_bytes[str(row[6])])
	else:
		indexs = []
	# 处理必须加密字段
	for row in data_rows[1:]:
		for index in indexs:
			print(hash_bytes[row[index]])
			row[index] = decrypt(key_str, hash_bytes[str(row[index])])
	return year, data_rows

if __name__ == '__main__':

	a = 'asdasd'
	d = {}
	d[hash(a)] = a
	print(d)



	hash_bytes = {}
	data_dict = read_xlsx('../17、18年统计数据格式模板.xlsx')
	data_dict_enc = {}
	for year, data_rows in data_dict.items():
		year_, data_rows_, hash_bytes_ = do_encrypt(append_zero('123'), data_rows, year)
		hash_bytes.update(hash_bytes_)
		print(year, hash_bytes)
		data_dict_enc[year_] = data_rows_
		for data_row in data_rows_:
			print(data_row)
	save_xlsx('../加密数据.xlsx', data_dict_enc)
	save_pickle('mapping.pkl', hash_bytes)

	data_dict_enc = read_xlsx('../加密数据.xlsx')
	hash_bytes = load_pickle('mapping.pkl')
	for year, data_rows in data_dict_enc.items():
		print(do_decrypt(append_zero('123'), data_rows, year, hash_bytes))

	a = {}
	a['1'] = 10
	b = {}
	b['1'] = 100
	a.update(b)
	print(a)
