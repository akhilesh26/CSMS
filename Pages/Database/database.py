from PyQt5 import QtSql
from sys import exit
# from create_tables import member_create

class Database():
    def __init__(self,userName='root',password='karma'):
        databaseName='csms'
        #super().__init__()
        self.userName = userName
        self.password = password
        self.databaseName = databaseName
        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setUserName(userName)
        self.db.setPassword(password)

        if not self.db.open():
            print(self.db.lastError().text())

        else:
            print('Database connected')

        self.query = QtSql.QSqlQuery()
        self.query.exec_('create database {}'.format(databaseName))
        self.query.exec_('use database {}'.format(databaseName))
        self.db.setDatabaseName(databaseName)

        
    def createTable(self):
        print(member_create)
        self.query.exec_(member_create)
        self.query.exec_('select * from fark')

    def getTable(self, name):
        pass
    
    def run_query(self, query):
        self.query.exec_(query)

    def printTable(self, name):
        pass

    def addColumn(self, name, columnName):
        pass

    def removeColumn(self, name, columnName):
        pass


if __name__=='__main__':
    db = Database()
    table = Table()
    table.print()
		



