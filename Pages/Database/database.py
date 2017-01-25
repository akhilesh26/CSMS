from PyQt5 import QtSql

class Database():
	def __init__(self):
		#super().__init__(self)
		db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
		db.setUserName('root')

		db.setPassword('toor')
		db.setDatabaseName('hello')
		if not db.open():
			print(db.lastError().text)


