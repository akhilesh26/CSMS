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
        self.memberIdLineEdit.setText(str(self.member.id))
        self.nameLineEdit.setText(self.member.name)
        self.maturityAmountLineEdit.setText('0')

        self.openningDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        # Combo box stuffs
        self.accountTypeComboBox.clear()
        for item in accountTypes:
            self.accountTypeComboBox.addItem(accountTypes[item])

        # Trigger action for account Type
        self.createFieldGui(0)
        self.accountType = self.accountTypeComboBox.currentText()
        self.accountTypeComboBox.activated.connect(self.createFieldGui)
        self.createAccountPushButton.clicked.connect(self.createAccount)
        self.show()

        


    def createFieldGui(self, accountTypeIndex):
        # Fix account type
        if accountTypeIndex == 0:
            print(accountTypes[accountTypeIndex])
            self.termLineEdit.hide()
            self.termLabel.hide()
            self.durationLineEdit.show()
            # Duration label
            self.label_8.show()
            self.amountLineEdit.show()
            self.amountLabel.show()
            self.maturityAmountLabel.show()
            self.maturityAmountLineEdit.show()
            self.closingDateEdit.show()
            self.closingDateLabel.show()
            # Validations
            self.validator = Validator([
                Number(self.memberIdLineEdit),
                String(self.nameLineEdit),
                Money(self.amountLineEdit),
                Number(self.durationLineEdit),
                Money(self.rateLineEdit),
            ])
            self.accountNoLineEdit.setText(str(self.member.id)+'f')

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
            self.maturityAmountLabel.hide()
            self.maturityAmountLineEdit.hide()
            self.closingDateEdit.hide()
            self.closingDateLabel.hide()
            # Validations
            self.validator = Validator([
                Number(self.memberIdLineEdit),
                String(self.nameLineEdit),
                Money(self.rateLineEdit),
            ])
            self.accountNoLineEdit.setText(str(self.member.id)+'s')
        # Rec account type
        if accountTypeIndex == 2:
            self.termLineEdit.show()
            self.termLabel.show()
            self.durationLineEdit.show()
            # Duration label
            self.label_8.show()
            self.amountLineEdit.show()
            self.amountLabel.show()
            self.maturityAmountLabel.show()
            self.maturityAmountLineEdit.show()
            self.closingDateEdit.show()
            self.closingDateLabel.show()
            # Validations
            self.validator = Validator([
                Number(self.memberIdLineEdit),
                String(self.nameLineEdit),
                Number(self.termLineEdit),
                Money(self.amountLineEdit),
                Number(self.durationLineEdit),
                Money(self.rateLineEdit),
            ])
            self.accountNoLineEdit.setText(str(self.member.id)+'r')
            print(accountTypes[accountTypeIndex])
    
    def createAccount(self):
        # memberId=self.memberIdLineEdit.text()
        # name=self.nameLineEdit.text()
        print('CREATE ACCOUNT CALLED')
        accountType=self.accountTypeComboBox.currentText()
        if not self.validator.is_valid():
            return 
        # Fixed 
        if accountType == accountTypes[0]:
            fd = FixedDeposit()
            fd.member_id = self.member.id

            fd.account_no = self.accountNoLineEdit.text()
            fd.payed_amount = self.amountLineEdit.text()
            fd.interest_rate = self.rateLineEdit.text()
# term in months
            fd.duration = self.durationLineEdit.text()
            fd.final_matured_amount = self.maturityAmountLineEdit.text()
            fd.opening_Date = self.openningDateEdit.text()
            db.session.add(fd)
            db.session.commit()
            self.close()
        # Saving
        if accountType == accountTypes[1]:
            sa = Saving()
            sa.account_no = self.accountNoLineEdit.text()
            sa.member_id  = self.member.id
            sa.interest_rate = self.rateLineEdit.text()
            # term in months
            sa.current_balance = 0
            sa.interest_accumulated = 0
            # sa.account_status = ""
            sa.opening_Date = self.openningDateEdit.text()
            db.session.add(sa)
            db.session.commit()
            self.close()
        # Recurring 
        if accountType == accountTypes[2]:
            rd = FixedDeposit()
            rd.member_id = self.member.id
            rd.account_no = self.accountNoLineEdit.text()
            rd.monthly_payment = self.amountLineEdit.text()
            rd.interest_rate = self.rateLineEdit.text()
            # term in months
            rd.term = self.termLineEdit.text()
            rd.duration = self.durationLineEdit.text()
            rd.current_balance = 0
            rd.final_matured_amount = self.maturityAmountLineEdit.text()
            rd.interest_accumulated = 0
            # fd.account_status = ""
            rd.opening_Date = self.openningDateEdit.text()
            db.session.add(rd)
            db.session.commit()
            self.close()
