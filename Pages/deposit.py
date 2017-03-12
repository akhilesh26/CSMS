from Pages.UI.depositUi import Ui_Form
from Pages.validators import *
from PyQt5 import QtWidgets,QtCore
from Models.deposit import Deposit

class DepositForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.deposit=Deposit()
        self.show()
        self.depositPushButton.clicked.connect(self.depositMoney)
        self.depositeDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        ## Link all validators
        ## Write in the order it is in GUI
        self.validator = Validator([
            Number(self.memberIdLineEdit),
            # NameWithSpaceValidator(self.nameLineEdit),
            # NameWithSpaceValidator(self.accountTypeComboBox),
            Money(self.amountLineEdit),
            Number(self.voucherNoLineEdit) 
        ])
        



    def depositMoney(self):
        valid = self.validator.is_valid()
        print('IS VALID ? ', valid)

        self.deposit.memberId=self.memberIdLineEdit.text()
        self.deposit.name=self.nameLineEdit.text()
        self.deposit.accountType=self.accountTypeComboBox.currentText()
        self.deposit.amount=self.amountLineEdit.text()
        self.deposit.paymentMode=self.paymentModeComboBox.currentText()
        self.deposit.date=self.depositeDateEdit.text()
        self.deposit.voucherNo=self.voucherNoLineEdit.text()
        self.deposit.comment=self.commentLineEdit.text()

