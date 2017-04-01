from Pages.UI.addNewMemberUi import Ui_Form 
from PyQt5 import QtWidgets, QtGui, QtCore
from Pages.confirmDialog import ConfirmDialog
# Shikhar's member class
# from Pages.Database.member import Member2
# from Pages.Database.database import Database 
# Utkarsh's member class
from Models.member import Member
from Models.database import db
from Pages.validators import *

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
        self.openingDateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.member2 = Member2()
        
        # Validation
        print(self.pinCodeLineEdit)
        self.validator = Validator([
            String(self.nameLineEdit),
            String(self.fatherLineEdit),
            String(self.villageLineEdit),
            String(self.blockLineEdit),
            String(self.districtLineEdit),
            String(self.stateLineEdit),
            Pincode(self.pinCodeLineEdit),
            MobileNo(self.mobileLineEdit),
            Money(self.membershipFeeLineEdit),
            Number(self.numberOfShareLineEdit),
            Money(self.currentRateLineEdit),
            Money(self.paybleAmountLineEdit),
            Required(self.IdNumberLineEdit)


        ])
   
    def cancel(self):
        self.close()

    def update(self):
        print("update button clicked")

    def addNew(self):
        print("add New button clicked")
        print('Valid ? ', self.validator.is_valid())
        if self.validator.is_valid():
            self.member.name  =  self.nameLineEdit.text()
            self.member.father_name = self.fatherLineEdit.text()
            self.member.dob = self.dobDateEdit.text()
            self.member.gender = self.genderComboBox.currentText()

            self.member.village = self.villageLineEdit.text()
            self.member.block = self.blockLineEdit.text()
            self.member.district = self.districtLineEdit.text()
            self.member.state = self.stateLineEdit.text()

            self.member.pincode = int(self.pinCodeLineEdit.text())
            self.member.phone = self.mobileLineEdit.text()
            try:
                self.member.photo_path = self.photoFileName
            except:
                self.member.photo_path = ""
            try:
                self.member.signature_image_path = self.signatureFileName
            except:
                self.member.signature_image_path = ""
            self.member.email = self.emailLineEdit.text()
            self.member.id_proof = self.idProofComboBox.currentText()
            self.member.id_number = self.IdNumberLineEdit.text()
            self.member.job = self.professionLineEdit.text()
            self.member.office = self.officeLineEdit.text()

            self.member.membership_type = self.membershipTypeComboBox.currentText()
            self.member.membership_fee = self.membershipFeeLineEdit.text()
            self.member.no_of_share = self.numberOfShareLineEdit.text()
            self.member.rate_at_the_time_of_buying = self.currentRateLineEdit.text()
            self.member.payable_amount = self.paybleAmountLineEdit.text()
            self.member.opening_Date = self.openingDateEdit.text()

            self.dialog=ConfirmDialog()
            self.dialog.accepted.connect(self.dialogAccept)
            self.dialog.rejected.connect(self.ignore)

            # now storing in member
        

    def dialogAccept(self):
        # self.member2.print()
        print(self.member)
        db.session.add(self.member)
        db.session.commit()
        # print(self.member2.get('Name'))
        self.dialog.close()
        self.close()

    def ignore(self):
        self.dialog.close()
            
    def setValues():
        pass

    def uploadPhoto(self):
        self.photoFileName=QtWidgets.QFileDialog.getOpenFileName(self,'Open File','.')[0]
        self.photoLabel.setPixmap(QtGui.QPixmap(self.photoFileName))
    
    def uploadSign(self):
        self.signatureFileName=QtWidgets.QFileDialog.getOpenFileName(self,'Open File','.')[0]
        self.signatureLabel.setPixmap(QtGui.QPixmap(self.signatureFileName))
