from Pages.UI.fdAccountReportUi import Ui_Form
from PyQt5 import QtWidgets

class FdAccountReport(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()