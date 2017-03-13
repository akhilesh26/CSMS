from Pages.UI.createAccountUi import Ui_Form
from PyQt5 import QtWidgets, QtCore

class CreateAccountForm(Ui_Form,QtWidgets.QWidget):
    def __init__(self, member):
        super().__init__()
        self.setupUi(self)
        self.member = member
        self.show()
        self.memberIdLineEdit.setText(str(self.member.id))
        self.nameLineEdit.setText(self.member.name)
        self.createAccountPushButton.clicked.connect(self.createAccount)
        self.openningDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    def createAccount(self):
        # memberId=self.memberIdLineEdit.text()
        # name=self.nameLineEdit.text()
        accountType=self.accountTypeComboBox.currentText()
        accountNo = self.accountNoLineEdit.text()
        date=self.openningDateEdit.text()
        print(memberId, name, accountType, accountNo, date)
