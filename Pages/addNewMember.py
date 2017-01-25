from Pages.UI.addNewMemberUi import Ui_Form 
from PyQt5 import QtWidgets

class AddNewMemberForm(QtWidgets.QWidget,Ui_Form):
	def __init__(self,parent = None):
		super().__init__(parent)
		print(parent)
		self.setupUi(self)
		self.show()
		self.parent = parent

		# callback functions
		self.cancelPushButton.clicked.connect(self.cancel)
		self.addNewPushButton.clicked.connect(self.addNew)
		self.updatePushButton.clicked.connect(self.update)

	def cancel(self):
		print('Cancel button clicked')
		self.close()
	def update(self):
		print("update button clicked")

	def addNew(self):
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

		print(name,father,dob,gender,village,block,district,state,pin,mobile,email,profession,membershipType,numberOfShare,currentRate,paybleAmount,openingDate)