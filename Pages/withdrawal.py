from Pages.UI.withdrawalUi import Ui_Form
from PyQt5 import QtWidgets, QtCore,QtGui
from Pages.validators import *
from Models.withdrawal import Withdrawal
from Models.database import db
from Models.member import Member
from Models.saving import Saving

class WithdrawalForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.withdrawal=Withdrawal()
        self.withdrawalPushButton.clicked.connect(self.withdraw)
        self.withdrawalDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.memberIdLineEdit.textChanged.connect(self.queryUser)

        # LINK ALL VALIDATORS
        self.validator = Validator([
            Number(self.memberIdLineEdit),
            String(self.nameLineEdit),
            #Money(self.amountLineEdit),
            Number(self.voucherNoLineEdit)
        ])
    def queryUser(self,id):
        print(id)
        self.member=db.session.query(Member).filter_by(id=id).first()
        if self.member==None:
            self.nameLineEdit.setText("")
            self.photoLabel.setPixmap(QtGui.QPixmap(""))
            self.signatureLabel.setPixmap(QtGui.QPixmap(""))
            self.accountTypeComboBox.clear()
            self.currentBalanceLineEdit.setText("")
            return
        self.nameLineEdit.setText(self.member.name)
        print('photo path: ', self.member.photo_path)
        self.photoLabel.setPixmap(QtGui.QPixmap(self.member.photo_path))
        self.signatureLabel.setPixmap(QtGui.QPixmap(self.member.signature_image_path))
        self.saving = db.session.query(Saving).filter_by(member_id=id).first()
        if self.saving==None:
            self.currentBalanceLineEdit.setText("")
            return
        self.currentBalanceLineEdit.setText(str(self.saving.current_balance))
        self.accountTypeComboBox.addItem("Saving ")
        curbal=float(self.currentBalanceLineEdit.text())
        InRange(self.amountLineEdit, 0,curbal )

    def withdraw(self):
        if self.validator.is_valid():
            self.withdrawal.member_id=self.memberIdLineEdit.text()
            #name=self.nameLineEdit.text()
            self.withdrawal.account_type=self.accountTypeComboBox.currentText()
            #currentBalance=self.currentBalanceLineEdit.text()
            self.withdrawal.amount=self.amountLineEdit.text()
            self.withdrawal.payment_mode=self.paymentModeComboBox.currentText()
            self.withdrawal.date=self.withdrawalDateEdit.text()
            self.withdrawal.voucher_no=self.voucherNoLineEdit.text()
            self.withdrawal.comment=self.commentLineEdit.text()
            db.session.add(self.withdrawal)
            db.session.commit()
            self.close()
        print('IS VALID ? ', self.validator.is_valid())
        #print(member_id,name,account_type,amount,payment_mode,currentBalance,date,voucherNo,comment)
