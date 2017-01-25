from PyQt5 import QtSql

class Database():
	def __init__(self,userName,password,databaseName):
		#super().__init__()
		
		self.userName = userName
		self.password = password
		self.databaseName = databaseName

		db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
		db.setUserName(userName)
		db.setPassword(password)
		db.setDatabaseName(databaseName)

		if not db.open():
			print(db.lastError().text())
		else:
			print('Database connected')

		#query can be made after opening database
		self.query = QtSql.QSqlQuery()
		



