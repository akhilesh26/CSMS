from Pages.UI.mainWindowUi import Ui_MainWindow as mainWindow
from Pages.addNewMember import AddNewMemberForm
from PyQt5 import QtWidgets
from Pages.balanceSheet import BalanceSheetForm

# main application window
class CSMSMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = mainWindow()
        self.ui.setupUi(self)

        # A method for exiting application
        self.ui.menuExit.mouseReleaseEvent = self.exitsafely

        # Close tabs
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)

        # # Setup callback for Members
        self.ui.actionAdd_New.triggered.connect(self.openAdd_New)
        # self.ui.actionFind.triggered.connect(self.openFind)

        # # Setup callback for Loan
        # self.ui.actionNew_Loan.triggered.connect(self.openNew_Loan)
        # self.ui.actionView_Loans.triggered.connect(self.openView_Loans)
        # # Setup callback for Transaction
        # self.ui.actionVoucher.triggered.connect(self.openVoucher)
        # self.ui.actionPay_Slip.triggered.connect(self.openPay_Slip)
        
        # Setup callback for all Reports
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

        # # Setup callback for Expense
        # self.ui.actionNew_Expense.triggered.connect(self.openNew_Expense)
        # self.ui.actionView_Expense.triggered.connect(self.openView_Expense)

        # # Setup callback for Backup
        # self.ui.actionSync.triggered.connect(self.openSync)
        # self.ui.actionRestore.triggered.connect(sefl.openRestore)

        # # Setup callback for Restore
        # self.ui.actionHelp.triggered.connect(self.openHelp)
        # self.ui.actionAbout.triggered.connect(self.openAbout)

    def openAdd_New(self,*args):
        self.window_addNewMember = AddNewMemberForm()

    def openBalance_Sheet(self,*args):
        self.tab_balanceSheet = BalanceSheetForm()
        self.ui.tabWidget.addTab(self.tab_balanceSheet,"Balance Sheet")

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

