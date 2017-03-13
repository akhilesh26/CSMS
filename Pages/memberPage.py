from Pages.UI.memberPageUi import Ui_memberPage
from Pages.createAccount import CreateAccountForm
from PyQt5 import QtWidgets, QtGui
from Models.fixedDeposit import FixedDeposit
from Models.recurring import Recurring
from Models.saving import Saving
from Models.database import db


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
            self.label_photo.setPixmap(QtGui.QPixmap(member.photo_path))
            self.label_signature.setPixmap(QtGui.QPixmap(member.signature_image_path))
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

        # Accounts Page!!
        f_view = self.fixedDepositWidget
        r_view = self.recurringWidget
        s_view = self.savingWidget

        f_view.hide()
        r_view.hide()
        s_view.hide()
        f = db.session.query(FixedDeposit).filter_by(member_id=self.member.id).first()
        if f:
            f_view.show()
            self.fAccountNoLineEdit.setText(f.account_no)
            self.fPrincipalAmountLineEdit.setText(str(f.payed_amount))
            # f.fOpeningDateEdit
            self.fMaturityAmountLineEdit.setText(str(f.final_matured_amount))
            self.fInterestRateLineEdit.setText(str(f.interest_rate))
            def deleteF():
                db.session.delete(f)
                db.session.commit()
                # Closes this so I don't have to update everything
                # This is a horrible solution. Correct it!!
                self.close()
            self.fDeletePushButton.clicked.connect(deleteF)
        r = db.session.query(Recurring).filter_by(member_id=self.member.id).first()
        if r:
            r_view.show()
            self.rAccountNoLineEdit.setText(r.account_no)
            self.rInterestRateLineEdit.setText(str(r.interest_rate))
            def deleteR():
                db.session.delete(r)
                db.session.commit()
                # Closes this so I don't have to update everything
                self.close()
            self.rDeletePushButton.clicked.connect(deleteR)
        s = db.session.query(Saving).filter_by(member_id=self.member.id).first()
        if s:
            s_view.show()
            self.sAccountNoLineEdit.setText(s.account_no)
            self.sInterestRateLineEdit.setText(str(s.interest_rate))
            def deleteS():
                db.session.delete(s)
                db.session.commit()
                # Closes this so I don't have to update everything
                self.close()
            self.sDeletePushButton.clicked.connect(deleteS)
        self.createAccountPushButton.clicked.connect(self.newAccountDialogOpen)

    def newAccountDialogOpen(self):
        self.window_create_account = CreateAccountForm(self.member)



