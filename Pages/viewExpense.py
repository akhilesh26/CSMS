from PyQt5 import QtWidgets
from Pages.UI.viewExpenseUi import Ui_Form
from Models.database import db
from Models.expense import Expense

class ViewExpenseForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        for expense in db.session.query(Expense).order_by(Expense.cost.desc()):
            item = QtWidgets.QListWidgetItem("Id: {} , Type: {} , Cost: {} , Payment Method: {} , Date: {}".format(expense.id, expense.type,expense.cost, expense.payment_method,expense.date),\
                    self.expenseList)

        # connections
        self.costRadioButton.clicked.connect(self.expenseList.clear)
        self.expenseIdRadioButton.clicked.connect(self.expenseList.clear)
        self.typeRadioButton.clicked.connect(self.expenseList.clear)

        self.searchLineEdit.textChanged.connect(self.getSearchResult)

        self.show()

    def getSearchResult(self,str):
        # choose from buttons
        if(self.costRadioButton.isChecked()):
            #search by cost and print list
            self.updateByCost()
        elif(self.typeRadioButton.isChecked()):
            #search by type of payment and print list
            self.updateByType()
        elif(self.expenseIdRadioButton.isChecked()):
            #search by expense id and print list
            self.updateByExpenseId()
        else:
            pass

    def updateByType(self):
        self.expenseList.clear()
        type = self.searchLineEdit.text()
        print(type) 
        for expense in db.session.query(Expense).filter(Expense.type.like(type+"%")):
            item = QtWidgets.QListWidgetItem("Id: {} , Type: {} , Cost: {} , Payment Method: {} , Date: {}".format(expense.id, expense.type,expense.cost, expense.payment_method,expense.date),\
                    self.expenseList)
    def updateByCost(self):
        self.expenseList.clear()
        cost = self.searchLineEdit.text()
        print(cost) 
        for expense in db.session.query(Expense).filter(Expense.cost.like(cost+"%")):
            item = QtWidgets.QListWidgetItem("Id: {} , Type: {} , Cost: {} , Payment Method: {} , Date: {}".format(expense.id, expense.type,expense.cost, expense.payment_method,expense.date),\
                    self.expenseList)
    def updateByExpenseId(self):
        self.expenseList.clear()
        id = self.searchLineEdit.text()
        print(id)
        for expense in db.session.query(Expense).filter(Expense.id.like(id+"%")):
            item = QtWidgets.QListWidgetItem("Id: {} , Type: {} , Cost: {} , Payment Method: {} , Date: {}".format(expense.id, expense.type,expense.cost, expense.payment_method,expense.date),\
                    self.expenseList)

