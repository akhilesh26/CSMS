from Pages.UI.createAccountsUi import Ui_Form
from Pages.confirmDialog import ConfirmDialog
from PyQt5 import QtWidgets

class AccountForm(Ui_Form,QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.createAccountPushButton.clicked.connect(self.createAccount)

	def createAccount(self):
		memberId=self.memberIdLineEdit.text()
		name=self.nameLineEdit.text()
		accountType=self.accountTypeComboBox.currentText()
                accountNo = self.accountNoLineEdit.text()
		date=self.openingDateEdit.text()
                print(memberId, name, accountType, accountNo, date)
