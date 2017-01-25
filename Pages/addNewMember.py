from Pages.UI.addNewMemberUi import Ui_Form 
from PyQt5 import QtWidgets, QtGui, QtCore
from Pages.confirmDialog import ConfirmDialog
from Pages.Database.member import Member
from Pages.Database.database import Database 

class AddNewMemberForm(Ui_Form, QtWidgets.QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.parent = parent
        self.setupUi(self)
        self.show()
        self.cancelPushButton.clicked.connect(self.cancel)
        self.addNewPushButton.clicked.connect(self.addNew)
        self.updatePushButton.clicked.connect(self.update)

        self.uploadPhotoPushButton.clicked.connect(self.uploadPhoto)
        self.uploadSignPushButton.clicked.connect(self.uploadSign)
        self.member = Member()
   

    def update(self):
        print("update button clicked")

    def addNew(self):
       
        
        print("add New button clicked")
        self.member.set('Name', self.nameLineEdit.text())

        self.member.set('Father',self.fatherLineEdit.text())
        self.member.set('DOB',self.dobDateEdit.text())
        self.member.set('Gender',self.genderComboBox.currentText())

        self.member.set('Village',self.villageLineEdit.text())

        self.member.set('Block',self.blockLineEdit.text())
        self.member.set('District',self.districtLineEdit.text())
        self.member.set('State',self.stateLineEdit.text())
        self.member.set('Pin',self.pinCodeLineEdit.text())

        self.member.set('Mobile',self.mobileLineEdit.text())
        self.member.set('Email',self.emailLineEdit.text())
        self.member.set('Profession',self.professionLineEdit.text())
        self.member.set('Office',self.officeLineEdit.text())

        self.member.set('MembershipType',self.membershipTypeComboBox.currentText())
        self.member.set('MembershipFee',self.membershipFeeLineEdit.text())
        self.member.set('NumberOfShare',self.numberOfShareLineEdit.text())

        self.member.set('CurrentRate',self.currentRateLineEdit.text())
        self.member.set('PaybleAmount',self.paybleAmountLineEdit.text())
        self.member.set('OpeningDate',self.openingDateEdit.text())

        self.dialog=ConfirmDialog()
        
        self.dialog.accepted.connect(self.dialogAccept)
        self.dialog.rejected.connect(self.ignore)
        # now storing in member
        

    def dialogAccept(self):
        self.member.print()

        self.dialog.close()
        self.close()

    def ignore(self):
        self.dialog.close()
            
    def setValues():
        pass


    def uploadPhoto(self):
        self.fileName=QtWidgets.QFileDialog.getOpenFileName(self,'Open File','.')[0]
        self.photoLabel.setPixmap(QtGui.QPixmap(self.fileName))
    
    def uploadSign(self):
        self.fileName=QtWidgets.QFileDialog.getOpenFileName(self,'Open File','.')[0]
        self.signatureLabel.setPixmap(QtGui.QPixmap(self.fileName))
