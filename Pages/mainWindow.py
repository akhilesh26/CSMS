from Pages.UI.mainWindowUi import Ui_MainWindow 
from Pages.addNewMember import AddNewMemberForm
from Pages.transfer import TransferForm
from Pages.newLoan import NewLoanForm
from Pages.deposit import DepositForm
from Pages.withdrawal import WithdrawalForm
from PyQt5 import QtWidgets
from Pages.balanceSheet import BalanceSheetForm
from Pages.findMember import FindMemberForm
from Pages.UI.addNewMemberUi import Ui_Form 
#from Pages.Database.database import Database


# main application window
class CSMSMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        print('here')

        # A method for exiting application
        self.menuExit.mouseReleaseEvent = self.exitsafely

        # Close tabs
        self.tabWidget.tabCloseRequested.connect(self.tabWidget.removeTab)

        # # Setup callback for Members
        self.actionAdd_New.triggered.connect(self.openAdd_New)
        self.actionFind.triggered.connect(self.openFind)

        # # Setup callback for Loan
        self.actionNew_Loan.triggered.connect(self.openNew_Loan)
        # self.actionView_Loans.triggered.connect(self.openView_Loans)
        # # Setup callback for Transaction
        self.actionTransfer.triggered.connect(self.openTransfer)
        self.actionDeposit.triggered.connect(self.openDeposit)
        self.actionWithdraw.triggered.connect(self.openWithdrawal)
        
        # Setup callback for all Reports
        self.actionRecurring_Deposit.triggered.connect(self.openRecurring_Deposit)
        self.actionFixed_Deposit.triggered.connect(self.openBalance_Sheet)
        self.actionSavings.triggered.connect(self.openSavings)
        self.actionAdvance.triggered.connect(self.openBalance_Sheet)
        self.actionOutstanding.triggered.connect(self.openBalance_Sheet)
        self.actionBalance_Sheet.triggered.connect(self.openBalance_Sheet)
        self.actionProfit_and_Loss.triggered.connect(self.openBalance_Sheet)
        self.actionReceipt_and_Disbursment.triggered.connect(self.openBalance_Sheet)
        self.actionShareholders.triggered.connect(self.openBalance_Sheet)
        self.actionTerm_Deposit_Account.triggered.connect(self.openBalance_Sheet)
        self.actionMisc.triggered.connect(self.openBalance_Sheet)

        # # Setup callback for Expense
        # self.actionNew_Expense.triggered.connect(self.openNew_Expense)
        # self.actionView_Expense.triggered.connect(self.openView_Expense)

        # # Setup callback for Backup
        # self.actionSync.triggered.connect(self.openSync)
        # self.actionRestore.triggered.connect(sefl.openRestore)

        # # Setup callback for Restore
        # self.actionHelp.triggered.connect(self.openHelp)
        # self.actionAbout.triggered.connect(self.openAbout)

    def openNew_Loan(self, *args):
        print('new loan page opened')
        self.windown_newLoan = NewLoanForm()

    def openAdd_New(self,*args):
        print(self)
        self.window_addNewMember = AddNewMemberForm()

    def openDeposit(self,*args):
        self.window_deposit = DepositForm()

    def openWithdrawal(self,*args):
        self.window_withdrawal = WithdrawalForm()

    def openFind(self,*args):
        print('Open find window')
        self.window_find = FindMemberForm()
    
    def openBalance_Sheet(self,*args):
        self.tab_balanceSheet = BalanceSheetForm()
        self.tabWidget.addTab(self.tab_balanceSheet,"Balance Sheet")

    def openSavings(self,*args):
        self.tabSavings = QtWidgets.QWidget()
        self.tabSavings.ui = savingsForm()
        self.tabSavings.ui.setupUi(self.tabSavings)
        self.tabWidget.addTab(self.tabSavings,"Savings")

    def openRecurring_Deposit(self,*args):
        self.tabRecurring_Deposit = QtWidgets.QWidget()
        self.tabRecurring_Deposit.ui = recurringdepositForm()
        self.tabRecurring_Deposit.ui.setupUi(self.tabRecurring_Deposit)
        self.tabWidget.addTab(self.tabRecurring_Deposit,"Recurring Deposit")

    def openTransfer(self, *args):
        self.window_transfer = TransferForm()

    def exitsafely(self,*args):
        # implement a "are you sure dialog box" later
        self.close()
        
    #confirmation for close mainWindow

    def closeEvent(self, event):
        
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            self.close()
        else:
            event.ignore()   

    def loadDatabase():
        pass

