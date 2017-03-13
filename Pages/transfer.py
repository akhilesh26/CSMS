from PyQt5 import QtWidgets, QtGui,QtCore
from Pages.UI.transferUi import Ui_fromBalanceLabel
from Pages.validators import *

class TransferForm(QtWidgets.QWidget, Ui_fromBalanceLabel):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.fromBalance = 10000.0
        self.fromBalanceLabel_2.setText(str(self.fromBalance))

        self.toBalance = 2000.0
        self.toBalance = self.toBalanceLabel.setText(str(self.toBalance))

        # test path for jpg; remove later
        self.fromPhotoPath = "Pages/UI/pranavDP.jpg" 
        self.fromPhotoLabel.setPixmap(QtGui.QPixmap(self.fromPhotoPath))

        self.toPhotoPath = "Pages/UI/pranavDP.jpg"
        self.toPhotoLabel.setPixmap(QtGui.QPixmap(self.toPhotoPath))

        # populate account types of receiving member
        # self.toAccountType

        self.submitPushButton.clicked.connect(self.getvalues)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())


        # LINK ALL VALIDATORS
        NumberValidator(self.fromMemberLineEdit)
        NumberValidator(self.toMemberLineEdit)
        NameWithSpaceValidator(self.formNameLineEdit)
        NameWithSpaceValidator(self.toNameLineEdit)
        MoneyValidator(self.fromAmountLineEdit)

    def getvalues(self):
        self.fromMember = self.fromMemberLineEdit.text()
        self.fromName = self.formNameLineEdit.text()
        self.fromAmount = self.fromAmountLineEdit.text()
        self.date = self.dateEdit.text()
        self.fromBalance = self.toMemberLineEdit.text()
        self.toName = self.toNameLineEdit.text()
        self.toAccountType = self.accountComboBox.currentText()

        print(self.fromMember, self.fromName, self.fromAmount, self.date, self.fromBalance, self.toName, self.toAccountType)
        self.close()
