from PyQt5 import QtWidgets
from Pages.UI.rdAccountReportUi import Ui_Form
from Models.member import Member
from Models.database import db

class RdAccountReport(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        data = [[1,2,3,4,5,6]]*10
        self.queryDb()
        self.showTable(data)
        self.show()

    def queryDb(self):
        data = db.session.query(Member).all()
        print('Data:\n', data)
        pass


    def showTable(self,data):
        # set row_i = 1 when s.no. is removed
        row_i = 1
        rows_count = len(data)
        col_count = len(data[0])
        for i, row in enumerate(data):
            self.tableWidget.insertRow(i)
            for j, data in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tableWidget.setItem(i,j,item)

