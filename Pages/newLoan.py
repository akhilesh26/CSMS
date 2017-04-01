from Pages.UI.newLoanUi import Ui_Form
from PyQt5 import QtWidgets,QtCore

class NewLoanForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.submitPushButton.clicked.connect(self.getvalues)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())

    def getvalues(self):
        # Get values from form
        self.memberId = self.memberIdLineEdit.text() 
        self.name = self.nameLineEdit.text()
        self.phone = self.phoneLineEdit.text()
        self.loanType = self.loanTypeComboBox.currentText()
        self.interestRate = self.interestRateLineEdit.text()
        # get compound method in months
        self.compoundMethod = self.compoundMethodComboBox.currentText()
        self.compoundMethod = int(self.compoundMethod.split()[0])

        
        self.principalAmount = self.principalAmountLineEdit.text()
        self.termMonths = self.termLineEdit.text()
        self.date = self.dateEdit.text()

        print(self.memberId,self.name,self.phone,self.loanType,self.interestRate,self.compoundMethod,self.principalAmount,self.termMonths,self.date)
        self.close()

