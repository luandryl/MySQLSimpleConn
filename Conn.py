#!/usr/bin/env python
# -*- coding: utf-8 -*-

#lib to comunicate pyhton/mysql
import MySQLdb
from pprint import pprint
import sys

class MySQLConn:
	#define the parameters to connect
	__host = None
	__user = None
	__key = None
	__db = None
	__table = None
	__session = None
	__conn = None

	#init config the parameters
	def __init__(self, host, user, key, db, table):
		self.__host = host
		self.__user = user
		self.__key = key
		self.__table = table
		self.__db = db

	#open the connection
	def __open(self):
		self.__conn  =  MySQLdb.connect(self.__host, self.__user, self.__key, self.__db)
		self.__session = self.__conn.cursor()

	#close the connection
	def __close(self):
		self.__session.close()
		self.__connection.close()

	#method to make a simple select and return the values xD
	def select(self):
		self.__open()
		self.__session.execute("SELECT * FROM " + self.__table)
		return self.__session.fetchall()
		self.__close()

if __name__ == '__main__':

	#creates the conn and show resuts
	#conn = MySQLConn('localhost','root','101520','nina', 'users')

	conn = MySQLConn(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	
	for itens in conn.select():
		for (item) in itens:
			print item
