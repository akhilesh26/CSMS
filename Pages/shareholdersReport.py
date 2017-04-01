from PyQt5 import QtWidgets
from Pages.UI.shareholdersReportUi import Ui_Form

class ShareholdersReport(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()