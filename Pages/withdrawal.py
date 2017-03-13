from Pages.UI.withdrawalUi import Ui_Form
<<<<<<< HEAD
from PyQt5 import QtWidgets, QtCore
=======
from PyQt5 import QtWidgets
from Pages.validators import *
>>>>>>> 0e3c30eb6a9da14d7158c4514b03004b57dec3eb

class WithdrawalForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.withdrawalPushButton.clicked.connect(self.withdraw)
        self.withdrawalDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # LINK ALL VALIDATORS
        NumberValidator(self.memberIdLineEdit)
        NameWithSpaceValidator(self.nameLineEdit)
        MoneyValidator(self.amountLineEdit)
        NumberValidator(self.voucherNoLineEdit)

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
        print(memberId,name,accountType,amount,paymentMode,currentBalance,date,voucherNo,comment)
