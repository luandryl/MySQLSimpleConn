#!/usr/bin/env python
# -*- coding: utf-8 -*-

#lib to comunicate pyhton/mysql
import MySQLdb
from pprint import pprint
import sys
import os

class MySQLConn:
	#define the parameters to connect
	__data = None
	__session = None
	__conn = None

	#init config the parameters
	def __init__(self, data):
		self.__data = data

	#open the connection
	def open(self):
		try:
			self.__conn  =  MySQLdb.connect(self.__data[0], self.__data[1], self.__data[2], self.__data[3])
		except Exception as e:
			raise

		self.__session = self.__conn.cursor()

	#close the connection
	def __close(self):
		self.__session.close()
		self.__connection.close()

	#method to make a simple select and return the values xD
	def select(self):
		self.open()
		self.__session.execute("SELECT * FROM " + self.__data[4])
		return self.__session.fetchall()
		self.__close()

class Docummentation(object):

	def test_select_error(self):
		return "\t\n\n\nDATA ERROR\n\n\n"+ "Database não configurada!\n \t 1-Crie uma Banco no Mysql com o nome que preferir \n \t2-importe a tabela users.sql"

	def dataError(self):
		os.system('clear')
		return "\t\n\n\nData Error\n\n\n"+ "aparentemente alguns dados estão incorretos. Verifique-os e tente novamente"

	def help(self):
		return "COMANDOS DISPONIVEIS ./Conn.py \n" + "Comando: \n" +"\t$./Conn.py [HOST] [USER] [PASSWORD] [DATABASE] [TABLE] \n" +"Onde: \n"+"\t[HOST] : Server Host do seu database \n"+"\t[USER] : Usuario do SGBD \n"+"\t[PASSWORD] : Senha p/ [USER] \n"+"\t[DATABASE] : Database Name  \n"+"\t[Table] : Table Name  \n"+"Caso a senha for nula, passar NULL em PASSWORD\n " +"Faz: \n"+"\t Realiza um select * na tabela mapeada \n\n\n\n"+"Comando: \n" +"\t$./Conn.py run test \n" +"Faz: \n"+"\t Realiza um select * nos parametros de conexão configurados em config.db \n\n\n"+"Comando: \n" +"\t$./Conn.py map table \n" +"Faz: \n"+"\t Realiza um select * nos parametros de conexão que serão informados"

	def run_test_help(self):
		return "BEM VINDO AOS TESTES\n\n\n\t1- Favor criar um base de dados chamada teste no seu MYSQL\n\t2-Importar a Base de dados user.sql";

	def test_sucess(self):
		return "\n\n\n SUCCESSFUL TEST";

	def test_fail(self):
		return "\n\n\n FAIL TEST";

	def show_data(self, data):
		print 'Data: \n\n\n\n'
		for tupl in data:
			line = ''
			for item in tupl:
				line += `item`
			print line + "\n"


class ModelConnInfo(object):

	def data_bind(self):
		data = []
		ct = 0
		for (line) in open('config.db').read().split(';\n'):
			for info in line.split('|'):
				if(ct == 1):
					data.append(info)
					ct = 0
				else:
					ct = ct + 1

		return data

class ConnDispatcher(object):

	__result_set = None

	def dispatch_run_test(self):
		print Docummentation().run_test_help()

		try:
			MySQLConn(ModelConnInfo().data_bind()).open()
		except Exception as e:
			print Docummentation().establish_conn_error()
			print Docummentation().test_fail()

		try:
			data = MySQLConn(ModelConnInfo().data_bind()).select()
		except Exception as e:
			print Docummentation().test_select_error()
			print Docummentation().test_fail()

		print Docummentation().test_sucess()
		Docummentation().show_data(data)

	def dispatch_map_table(self):

		sv = raw_input("Server Host: \n")
		us = raw_input("User: \n")
		ps = raw_input("Password: \n")
		db = raw_input("Database: \n")
		table = raw_input("Table:\n ")
		data = [ sv, us, ps, db, table ]

		try:
			data = MySQLConn(data).select()
		except Exception as e:
			print Docummentation().dataError()

		Docummentation().show_data(data)


if __name__ == '__main__':

	ModelConnInfo().data_bind()

	if(len(sys.argv) == 1):
		print Docummentation().help()
	if(sys.argv[1] == "--help"):
		print Docummentation().help()
	elif(sys.argv[1] == "map" and sys.argv[2] == "table"):
		ConnDispatcher().dispatch_map_table()
	elif(sys.argv[1] == "run" and sys.argv[2] == "test"):
		ConnDispatcher().dispatch_run_test()
	else:
		print Docummentation().help()
