#!/usr/bin/env python
# -*- coding: utf-8 -*-

#lib to comunicate pyhton/mysql
import MySQLdb

class MySQLConn:
	#define the parameters to connect 
	__host = None
	__user = None
	__passw1 = None
	__db = None
	__session = None
	__conn = None

	#init config the parameters
	def __init__(self, host, user, passw, db):
		self.__host = host
		self.__user = user
		self._passw1 = passw
		self.__db = db
		
	#open the connection
	def __open(self):
		self.__conn  =  MySQLdb.connect(self.__host, self.__user, '101520',self.__db)		
		self.__session = self.__conn.cursor()
	
	#close the connection
	def __close(self):
		self.__session.close()
		self.__connection.close()
	
	#method to make a simple select and return the values xD
	def select(self):
		self.__open()
		self.__session.execute("SELECT * FROM Aluno")
		return self.__session.fetchall()
		self.__close()

if __name__ == '__main__':
    
	#creates the conn and show resuts
	conn = MySQLConn('localhost','root','101520','TESTE')
	print conn.select()
		
		
		
		
		