from PyQt5 import QtWidgets
from Pages.UI.newExpenseUi import Ui_Form
from Models.expense import Expense
from Models.database import db
class NewExpenseForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.submitButton.clicked.connect(self.submit)
        self.expense = Expense()

    def submit(self):
    	print("Starting submit")
    	self.expense.id = int(self.expenseIdLineEdit.text())
    	self.expense.type = self.expenditureTypeComboBox.currentText()
    	self.expense.payment_method = self.paymentMethodComboBox.currentText()
    	self.expense.cost = self.expenditureCostLineEdit.text()
    	self.expense.date = self.dateDateEdit.text()

    	# inserting the data in database
    	print(self.expense)
    	db.session.add(self.expense)
    	db.session.commit()
    	self.close()


