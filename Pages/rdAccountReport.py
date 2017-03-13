from PyQt5 import QtWidgets
from Pages.UI.rdAccountReportUi import Ui_Form

class RdAccountReport(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()