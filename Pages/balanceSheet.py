# Created a database with name qtsqlteset
# Created a table members with attributes 
# create table members (memberId int, name varchar(20), amount int, shares int, mobile varchar(20));
# insert into members values (1, 'ut', 1000, 1, 09992); 3 records 

from Pages.UI.balanceSheetUi import Ui_Form 
from PyQt5 import QtWidgets,QtSql

class BalanceSheetForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        userName = 'root'
        password = 'karma'
        databaseName = 'csms'
        db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        db.setUserName(userName)
        db.setPassword(password)
        db.setDatabaseName(databaseName)

        if db.open():
            print('Yea! Database connected')
        else:
            print('Oh! NO')
        self.viewMemberInfo()

    def viewMemberInfo(self):
        query = QtSql.QSqlQuery()
        print(query.exec_('select * from members;'))
        print('Funtion called')
        pos = 0
        while query.next():
            self.tableWidget.insertRow(pos)
            for i in range(1,6):
                cellItem = QtWidgets.QTableWidgetItem(str(query.value(i-1)))
                self.tableWidget.setItem(pos, i, cellItem)
                print(cellItem.text())
            pos += 1


    
