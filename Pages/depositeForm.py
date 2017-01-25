from Pages.UI.depositeFormUi import Ui_Form
from PyQt5 import QtWidgets

class DepositeForm(Ui_Form,QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.depositePushButton.clicked.connect(self.dopositeMoney)
        
	def dopositeMoney(self):
		memberId=self.memberIdLineEdit.text()
		name=self.nameLineEdit.text()
		accountType=self.accountTypeComboBox.currentText()
		amount=self.amountLineEdit.text()
		paymentMode=self.paymentModeComboBox.currentText()
		date=self.depositeDateEdit.text()
		voucherNo=self.voucherNoLineEdit.text()
		comment=self.commentLineEdit.text()
		print(memberId,name,accountType,amount,paymentMode,date,voucherNo,comment)