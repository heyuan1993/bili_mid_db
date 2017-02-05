# -*- coding: utf-8 -*-

'''
Created on Sun Feb  5 02:00:14 2017

@author: heyua_000

generateDB

create the mid-encrypted_mid table
'''

import bili_mid_db.sql as sql

'''
before work: need to create database and table
create table mid_DB
	(
		mid char(8) not null primary key,
		encrypted_mid char(8) not null
	);
'''

import binascii

def get_encrypt_mid(mid):
	mid = bytearray(mid, 'u8')
	encrypted_mid = hex(binascii.crc32(mid))
	# delete the 0x from the begining of the string
	encrypted_mid = encrypted_mid[2:]
	return encrypted_mid



def main():
	max_member = 99999999
	for i in range(1,max_member):
		mid = str(i)
		encrypt_mid = get_encrypt_mid(mid)
		try:
			sql.insert_mid(mid, encrypt_mid)
		except Exception as e:
			# print error message
			print(e)


if __name__ == '__main__':
    main()

