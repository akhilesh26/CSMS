from Pages.UI.memberPageUi import Ui_memberPage
from PyQt5 import QtWidgets, QtGui


class MemberProfile(QtWidgets.QWidget,Ui_memberPage):
    def __init__(self, member):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.member = member

        self.label_nameField.setText(member.name)
        self.label_fatherHusbandField.setText(member.father_name)
        # self.label_dobField.setText(member.dob)
        self.label_genderField.setText(member.gender)
        self.label_villageField.setText(member.village)
        self.label_blockField.setText(member.block)
        self.label_districtField.setText(member.district)
        self.label_stateField.setText(member.state)
        self.label_pincodeField.setText(str(member.pincode))
        self.label_mobileField.setText(member.phone)
        try:
            self.label_photoField.setPixmap(QtGui.QPixmap(member.photo_path))
            self.label_signatureField.setPixmap(QtGui.QPixmap(member.signature_image_path))
        except:
            pass
        self.label_emailField.setText(member.email)
        self.label_idProof.setText(member.id_proof)
        self.label_idNumber.setText(member.id_number)
        self.label_professionField.setText(member.job)
        self.label_officeField.setText(member.office)
        self.label_membershipTypeField.setText(member.membership_type)
        self.label_sharesField.setText(str(member.no_of_share))
        # self.label_openingDateField = QtWidgets.QLabel(self.infoTab)


