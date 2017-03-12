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
        self.createFieldGui(self.accountType)

    def createFieldGui(self, accountType):
        # Fix account type
        if accountType == accountTypes[0]:
            print(accountType)
            self.termLineEdit.hide()
        # Sav account type
        if accountType == accountTypes[1]:
            print(accountType)
            self.termLineEdit.hide()
            self.durationLineEdit.hide()
            self.amountLineEdit.hide()
        # Rec account type
        if accountType == accountTypes[2]:
            print(accountType)
    
    def createAccount(self):
        # memberId=self.memberIdLineEdit.text()
        # name=self.nameLineEdit.text()
        accountType=self.accountTypeComboBox.currentText()
        accountNo = self.accountNoLineEdit.text()
        date=self.openningDateEdit.text()
        self.accountType.get(accountType)(accountNo, date)
        print(accountType, accountNo, date)

    def createFixedAccount(self, accountNo, date):
        from Models.fixedDeposit import FixedDeposit
        fd = FixedDeposit(accountNo, date)
        db.session.add(fd)
        db.session.commit()

    def createSavingAccount(self, accountNo, date):
        from Models.saving import Saving 
        sa = Saving(accountNo, date)
        db.session.add(sa)
        db.session.commit()

    def createRecurringAccount(self, accountNo, date):
        from Models.recurring import Recurring 
        ra = Recurring(accountNo, date)
        db.session.add(ra)
        db.session.commit() 
