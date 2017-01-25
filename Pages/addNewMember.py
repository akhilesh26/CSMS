from Pages.UI.addNewMemberUi import Ui_Form 
from PyQt5 import QtWidgets, QtGui, QtCore
from Pages.confirmDialog import ConfirmDialog

class AddNewMemberForm(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.cancelPushButton.clicked.connect(self.cancel)
        self.addNewPushButton.clicked.connect(self.addNew)
        self.updatePushButton.clicked.connect(self.update)

    def ignore(self):
                    self.dialog.destroy()

    def cancel(self):

            def dialogAccept():
                    self.close()
                    self.dialog.destroy()

            print('Cancel button clicked')
            self.dialog=ConfirmDialog()
            self.dialog.accept=dialogAccept
            self.dialog.reject=self.ignore

    

    def update(self):
            self.filename = QtWidgets.QFileDialog.getOpenFileName(self,'Open File', '.')
            print(self.filename)
            self.label_14.setPixmap(QtGui.QPixmap(self.filename[0]))
            self.label_14.setMaximumSize(QtCore.QSize(100, 100))
            self.label_14.setScaledContents(True)
            print("update button clicked")

    def addNew(self):
            self.dialog=ConfirmDialog()
            
            def dialogAccept():
                    print("add New button clicked")
                    name=self.nameLineEdit.text()
                    father=self.fatherLineEdit.text()
                    dob=self.dobDateEdit.text()
                    gender=self.genderComboBox.currentText()

                    village=self.villageLineEdit.text()
                    block=self.blockLineEdit.text()
                    district=self.districtLineEdit.text()
                    state=self.stateLineEdit.text()
                    pin=self.pinCodeLineEdit.text()

                    mobile=self.mobileLineEdit.text()
                    email=self.emailLineEdit.text()
                    profession=self.professionLineEdit.text()
                    office=self.officeLineEdit.text()

                    membershipType=self.membershipTypeComboBox.currentText()
                    membershipFee=self.membershipFeeLineEdit.text()
                    numberOfShare=self.numberOfShareLineEdit.text()

                    currentRate=self.currentRateLineEdit.text()
                    paybleAmount=self.paybleAmountLineEdit.text()
                    openingDate=self.openingDateEdit.text()

                    print(name,father,dob,gender,village,block,district,state,pin,mobile,email,\
                            profession,membershipType,numberOfShare,currentRate,paybleAmount,openingDate)

                    self.close()
                    self.dialog.destroy()

            self.dialog.accept=dialogAccept
            self.dialog.reject=self.ignore
