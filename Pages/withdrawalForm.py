from Pages.UI.withdrawalFormUi import Ui_Form
from PyQt5 import QtWidgets

class WithdrawalForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.withdrawalPushButton.clicked.connect(self.withdraw)

    def withdraw(self):
        memberId=self.memberIdLineEdit.text()
        name=self.nameLineEdit.text()
        self.accountTypeComboBox.disable()
        accountType=self.accountTypeComboBox.currentText()
        currentBalance=self.currentBalanceLineEdit.text()
        amount=self.amountLineEdit.text()
        paymentMode=self.paymentModeComboBox.currentText()
        date=self.withdrawalDateEdit.text()
        voucherNo=self.voucherNoLineEdit.text()
        comment=self.commentLineEdit.text()
        print(memberId,name,accountType,amount,paymentMode,currentBalance,date,voucherNo,comment)