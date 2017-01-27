from UI.memberPageUi import Ui_memberPage
from PyQt5 import QtWidgets


class MemberProfile(QtWidgets.QWidget,Ui_memberPage):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()

