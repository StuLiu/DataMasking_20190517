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
from gmssl.sm3 import sm3_hash
import pickle

def encrypt(key_str, data_str)->bytes:
	assert len(key_str) == 16
	key_bytes = bytes(key_str, encoding='utf-8')
	data_bytes = bytes(data_str, encoding='utf-8')
	crypt_sm4 = CryptSM4()
	crypt_sm4.set_key(key_bytes, SM4_ENCRYPT)
	return crypt_sm4.crypt_ecb(data_bytes)  # bytes类型

def decrypt(key_str, data_bytes)->str:
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

def save_map(file_name, dict_obj):
	assert type(dict_obj) == type(dict())
	with open(file_name, "wb") as file:
		pickle.dump(dict_obj, file)

def load_map(file_name):
	with open(file_name, "rb") as file:
		data = pickle.load(file)
		assert type(data) == type(dict())
		return data

def read_data(file_path)->(str,list):
	with open(file_path, 'r', encoding='utf-8') as file:
		lines = file.readlines()
		return lines[0], lines[1:]

def save_data(file_path, data):
	"""data:{}"""
	with open(file_path, 'w', encoding='utf-8') as file:
		for k,v in data.items():
			lines = k
			for line in v:
				lines += line
			file.write(lines)
# d = {'a\n':['asd\n','sddddd\n'],'c\n':['asd\n','sddddd\n']}
# save_data('./oo.txt', d)
if __name__ == '__main__':
	key_s = append_zero('123456')
	key = bytes(key_s, encoding='utf-8')
	value_s = str('姓名 刘旺 性别 男') #  bytes类型
	print(key_s, value_s)
	value_b = encrypt(key_s, value_s)

	inter_v_s = hash(value_b)

	value_s_2 = decrypt(key_s, value_b)
	print(value_s_2)
	assert value_s == value_s_2

	save_map('test.file', {'1123213':'姓名 刘旺 性别 男'})
	print(load_map('test.file'))