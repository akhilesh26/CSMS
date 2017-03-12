from Pages.UI.createAccountUi import Ui_Form
from Models.recurring import Recurring
from Models.fixedDeposit import FixedDeposit
from Models.saving import Saving
from Models.database import db

from PyQt5 import QtWidgets

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
        # Combo box stuffs
        self.accountTypeComboBox.clear()
        for item in accountTypes:
            self.accountTypeComboBox.addItem(accountTypes[item])

        self.accountType = self.accountTypeComboBox.currentText()
        # Trigger action for account Type
        self.accountTypeComboBox.activated.connect(self.createFieldGui)

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
        # Sav account type
        if accountTypeIndex == 1:
            print(accountTypes[accountTypeIndex])
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
        accountNo = self.accountNoLineEdit.text()
        date=self.openningDateEdit.text()
        rate = self.rateLineEdit.text()
        self.accountType.get(accountType)(accountNo, date, rate)
        print(accountType, accountNo, date, rate)

    def createFixedAccount(self, accountNo, date, rate):
        from Models.fixedDeposit import FixedDeposit
        fd = FixedDeposit(accountNo, date)
        db.session.add(fd)
        db.session.commit()

    def createSavingAccount(self, accountNo, date, rate):
        from Models.saving import Saving 
        sa = Saving(accountNo, date)
        db.session.add(sa)
        db.session.commit()

    def createRecurringAccount(self, accountNo, date, rate):
        from Models.recurring import Recurring 
        ra = Recurring(accountNo, date)
        db.session.add(ra)
        db.session.commit() 
