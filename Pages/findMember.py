from Pages.UI.findMemberUi import Ui_Form
from Models.member import Member
from Models.database import db
from Pages.memberPage import MemberProfile
from PyQt5 import QtWidgets

class FindMemberForm(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi(self)

        for member in db.session.query(Member).order_by(Member.name.desc()):
            item = QtWidgets.QListWidgetItem("Id: {}, Name: {}".format(member.id, member.name),\
                    self.membersList, member.id)

        self.membersList.itemDoubleClicked.connect(self.getUserInfo)

        # Get input values
        self.methodSelected = self.nameRadioButton.isEnabled()
        self.searchLineEdit.textChanged.connect(self.getSearchResult)
        print(self.methodSelected)
        self.nameRadioButton.clicked.connect(self.membersList.clear)
        self.phoneRadioButton.clicked.connect(self.membersList.clear)
        self.memberIdRadioButton.clicked.connect(self.membersList.clear)
        self.show()

    def getUserInfo(self,item):
        id = item.type()
        member = db.session.query(Member).filter_by(id=id).first()
        print(member)
        self.memberProfilePage = MemberProfile(member)

    def getSearchResult(self,str):
        # choose from buttons
        if(self.nameRadioButton.isChecked()):
            #search by name and print list
            updateByName()
        elif(self.phoneRadioButton.isChecked()):
            #search by name and print list
            updateByPhone()
        elif(self.memberIdRadioButton.isChecked()):
            #search by name and print list
            updateByMemberId()
        else:
            pass

        self.membersList.clear()
        self.membersList.addItem(str)

    def openMemberPage():
        pass

    def updateByName():
        pass
    def updateByPhone():
        pass
    def updateBymemberId():
        pass
        


