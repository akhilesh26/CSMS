from PyQt5 import QtWidgets 
from Pages.UI.confirmDialogUi import Ui_Dialog

class ConfirmDialog(Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

		
