from Pages.UI.balanceSheetUi import Ui_Form 
from PyQt5 import QtWidgets

class BalanceSheetForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

    
