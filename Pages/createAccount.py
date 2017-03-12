from Pages.UI.createAccountUi import Ui_Form

from PyQt5 import QtWidgets, QtCore

from Models.recurring import Recurring
from Models.fixedDeposit import FixedDeposit
from Models.saving import Saving
from Models.database import db

from PyQt5 import QtWidgets
from Pages.validators import Validator, Number, String, Money


accountTypes = {
    0: 'Fixed Account',
    1: 'Saving',
    2: 'Recurring Account'
}

class CreateAccountForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self, member):
        super().__init__()
        # Account type here
        self.setupUi(self)
        self.member = member
        self.show()
        self.memberIdLineEdit.setText(str(self.member.id))
        self.nameLineEdit.setText(self.member.name)
        self.createAccountPushButton.clicked.connect(self.createAccount)

        self.openningDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # Combo box stuffs
        self.accountTypeComboBox.clear()
        for item in accountTypes:
            self.accountTypeComboBox.addItem(accountTypes[item])

        self.accountType = self.accountTypeComboBox.currentText()
        # Trigger action for account Type
        self.accountTypeComboBox.activated.connect(self.createFieldGui)

        # Validations
        self.validator = Validator([
            Number(self.memberIdLineEdit),
            String(self.nameLineEdit),
            Number(self.termLineEdit),
            Money(self.amountLineEdit),
            Number(self.durationLineEdit),
            Number(self.rateLineEdit),
        ])
        


    def createFieldGui(self, accountTypeIndex):
        # Fix account type
        if accountTypeIndex == 0:
            print(accountTypes[accountTypeIndex])
            self.termLineEdit.hide()
            self.termLabel.hide()
            self.durationLineEdit.hide()
            # Duration label
            self.label_8.hide()
            self.amountLineEdit.show()
            self.amountLabel.show()
            self.maturityAmount.show()

        # Sav account type
        if accountTypeIndex == 1:
            print(accountTypes[accountTypeIndex])
        print('IS VALID ? ', self.validator.is_valid())
            self.termLineEdit.hide()
            self.termLabel.hide()
            self.durationLineEdit.hide()
            # Duration label
            self.label_8.hide()
            self.amountLineEdit.hide()
            self.amountLabel.hide()
        # Rec account type
        if accountTypeIndex == 2:
            self.termLineEdit.show()
            self.termLabel.show()
            self.durationLineEdit.show()
            # Duration label
            self.label_8.show()
            self.amountLineEdit.show()
            self.amountLabel.show()
            print(accountTypes[accountTypeIndex])
    
    def createAccount(self):
        # memberId=self.memberIdLineEdit.text()
        # name=self.nameLineEdit.text()
        accountType=self.accountTypeComboBox.currentText()
            
        if accountType == accountTypes[0]:
            self.fd = FixedDeposit()
            self.fd.member = self.member
            self.term = int(self.termLineEdit.text())

