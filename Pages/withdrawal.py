from Pages.UI.withdrawalUi import Ui_Form
from PyQt5 import QtWidgets, QtCore
from Pages.validators import *

class WithdrawalForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.withdrawalPushButton.clicked.connect(self.withdraw)
        self.withdrawalDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # LINK ALL VALIDATORS
        self.validator = Validator([
            NumberValidator(self.memberIdLineEdit),
            NameWithSpaceValidator(self.nameLineEdit),
            MoneyValidator(self.amountLineEdit),
            NumberValidator(self.voucherNoLineEdit)
        ])

    def withdraw(self):
        memberId=self.memberIdLineEdit.text()
        name=self.nameLineEdit.text()
        accountType=self.accountTypeComboBox.currentText()
        currentBalance=self.currentBalanceLineEdit.text()
        amount=self.amountLineEdit.text()
        paymentMode=self.paymentModeComboBox.currentText()
        date=self.withdrawalDateEdit.text()
        voucherNo=self.voucherNoLineEdit.text()
        comment=self.commentLineEdit.text()
        print('IS VALID ? ', self.validator.is_valid())
        print(memberId,name,accountType,amount,paymentMode,currentBalance,date,voucherNo,comment)
