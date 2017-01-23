from Pages.UI.findMemberUi import Ui_Form
from PyQt5 import QtWidgets

class FindMemberForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Get input values
        # self.methodSelected = 
        self.SearchLineEdit.textChanged.connect(self.getsearchresult)
        self.show()

    def getsearchresult(self,*args):
        print('Input search args',args)

