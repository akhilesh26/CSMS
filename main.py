from firstdialog import Ui_Form as welcomeForm
from MainWindow import Ui_MainWindow as mainWindow

# experimental
# -------------------------------------------------
from savings import Ui_Form as savingsForm
from balancesheet import Ui_Form as balancesheetForm
from recurringdeposit import Ui_Form as recurringdepositForm
# -------------------------------------------------

import sys
from PyQt5 import QtWidgets

# implement later; return root info from databse
def getRootInfo():
    # username, password
    return "ut","12"

# first dialog box; username password verify`
class CSMSWelcome(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = welcomeForm()
        self.ui.setupUi(self)
        self.setWindowTitle('CSMS Software')
        self.ui.enterPushButton.clicked.connect(self.verify)

    def verify(self):
        usernameInput = self.ui.usernameLineEdit.text()
        passwordInput = self.ui.passwordLineEdit.text()
        print(usernameInput,passwordInput)
        if (usernameInput,passwordInput)==getRootInfo():
            text = "Congrats! You can come in"
            # implement root user coming code
            self.close()
            self.initialiseMain()
        else:
            text = "Wrong username or password! Try again"
        text = "<b>"+text+"</b"
        self.ui.welcomeMessageLabel.setText(text)

    def initialiseMain(self):
        csms2.show()

# main application window
class CSMSMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainWindow()
        self.ui.setupUi(self)

        # A method for exiting application
        self.ui.menuExit.mouseReleaseEvent = self.exitsafely

        # Open new tabs for all reports
        self.ui.actionRecurring_Deposit.triggered.connect(self.openRecurring_Deposit)
        self.ui.actionFixed_Deposit.triggered.connect(self.openBalance_Sheet)
        self.ui.actionSavings.triggered.connect(self.openSavings)
        self.ui.actionAdvance.triggered.connect(self.openBalance_Sheet)
        self.ui.actionOutstanding.triggered.connect(self.openBalance_Sheet)
        self.ui.actionBalance_Sheet.triggered.connect(self.openBalance_Sheet)
        self.ui.actionProfit_and_Loss.triggered.connect(self.openBalance_Sheet)
        self.ui.actionReceipt_and_Disbursment.triggered.connect(self.openBalance_Sheet)
        self.ui.actionShareholders.triggered.connect(self.openBalance_Sheet)
        self.ui.actionTerm_Deposit_Account.triggered.connect(self.openBalance_Sheet)
        self.ui.actionMisc.triggered.connect(self.openBalance_Sheet)


        # Close tabs
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)

        
    def openBalance_Sheet(self,*args):
        self.tab_balancesheet = QtWidgets.QWidget()
        self.tab_balancesheet.ui = balancesheetForm()
        self.tab_balancesheet.ui.setupUi(self.tab_balancesheet)
        self.ui.tabWidget.addTab(self.tab_balancesheet,"Balance Sheet")

    def openSavings(self,*args):
        self.tabSavings = QtWidgets.QWidget()
        self.tabSavings.ui = savingsForm()
        self.tabSavings.ui.setupUi(self.tabSavings)
        self.ui.tabWidget.addTab(self.tabSavings,"Savings")

    def openRecurring_Deposit(self,*args):
        self.tabRecurring_Deposit = QtWidgets.QWidget()
        self.tabRecurring_Deposit.ui = recurringdepositForm()
        self.tabRecurring_Deposit.ui.setupUi(self.tabRecurring_Deposit)
        self.ui.tabWidget.addTab(self.tabRecurring_Deposit,"Recurring Deposit")

    def exitsafely(self,*args):
        # implement a "are you sure dialog box" later
        self.close()

if __name__=='__main__':
    # initialise the application
    app = QtWidgets.QApplication(sys.argv)
    # login screen
    csmsLogin = CSMSWelcome()
    csmsLogin.show()
    # main window
    csms2 = CSMSMain()
    sys.exit(app.exec_())



