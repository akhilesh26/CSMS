from Pages.UI.depositUi import Ui_Form
from PyQt5 import QtWidgets,QtCore
from Models.deposit import Deposit
class DepositForm(Ui_Form,QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.deposit=Deposit
		self.show()
		self.depositPushButton.clicked.connect(self.depositMoney)
		self.depositeDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        
	def depositMoney(self):
		self.deposit.memberId=self.memberIdLineEdit.text()
		self.deposit.name=self.nameLineEdit.text()
		self.deposit.accountType=self.accountTypeComboBox.currentText()
		self.deposit.amount=self.amountLineEdit.text()
		self.deposit.paymentMode=self.paymentModeComboBox.currentText()
		self.deposit.date=self.depositeDateEdit.text()
		self.deposit.voucherNo=self.voucherNoLineEdit.text()
		self.deposit.comment=self.commentLineEdit.text()

		print(memberId,name,accountType,amount,paymentMode,date,voucherNo,comment)
