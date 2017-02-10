from PyQt5.QtSql import QSqlTableModel

class Table(QSqlTableModel):
    def __init__(self,tableName='members'):
        super().__init__()
        self.tableName = tableName
        
    def print(self):
        self.setTable(self.tableName)
        print(self.select())
        row = self.rowCount()
        column = self.columnCount()
        print(self.record(1).value(1))
        for i in range(row):
            for j in range(column):
                print(self.record(i).value(j))
        
        



