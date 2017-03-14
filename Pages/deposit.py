from Pages.UI.depositUi import Ui_Form
from Pages.validators import *
from PyQt5 import QtWidgets,QtCore,QtGui
from Models.deposit import Deposit
from Models.database import db
from Models.member import Member
from Models.fixedDeposit import FixedDeposit
from Models.recurring import Recurring
from Models.saving import Saving

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

        self.memberIdLineEdit.textChanged.connect(self.queryUser)



    def queryUser(self,id):
        print(id)
        self.member=db.session.query(Member).filter_by(id=id).first()
        if self.member==None:
            self.nameLineEdit.setText("")
            self.photoLabel.setPixmap(QtGui.QPixmap(""))
            self.accountTypeComboBox.clear()

            return
        self.nameLineEdit.setText(self.member.name)
        print('photo path: ', self.member.photo_path)
        self.photoLabel.setPixmap(QtGui.QPixmap(self.member.photo_path))

        #l=db.session.query(FixedDeposit).filter_by(member_id=id).first()
        s = db.session.query(Saving).filter_by(member_id=id).first()
        print('printing###########  s',s)
        r = db.session.query(Recurring).filter_by(member_id=id).first()
        print('printing@@@@@@@@@@@@  r', r)
        if s!=None:
            self.accountTypeComboBox.addItem("Saving ")
        if r!=None:
            self.accountTypeComboBox.addItem("Recurring Account")



    def depositMoney(self):
        valid = self.validator.is_valid()
        print('IS VALID ? ', valid)
        if self.validator.is_valid():

            self.deposit.member_id=self.memberIdLineEdit.text()
            #self.deposit.name=self.nameLineEdit.text()
            self.deposit.account_type=self.accountTypeComboBox.currentText()
            self.deposit.amount=self.amountLineEdit.text()
            self.deposit.payment_mode=self.paymentModeComboBox.currentText()
            self.deposit.date=self.depositeDateEdit.text()
            self.deposit.voucher_no=self.voucherNoLineEdit.text()
            self.deposit.comment=self.commentLineEdit.text()

            db.session.add(self.deposit)
            db.session.commit()
            self.close()


