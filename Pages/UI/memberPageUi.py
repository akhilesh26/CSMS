# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memberPage.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_memberPage(object):
    def setupUi(self, memberPage):
        memberPage.setObjectName("memberPage")
        memberPage.resize(779, 554)
        self.gridLayout = QtWidgets.QGridLayout(memberPage)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(memberPage)
        self.tabWidget.setObjectName("tabWidget")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.infoTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_photo = QtWidgets.QLabel(self.infoTab)
        self.label_photo.setObjectName("label_photo")
        self.verticalLayout.addWidget(self.label_photo)
        self.label_photoField = QtWidgets.QLabel(self.infoTab)
        self.label_photoField.setMaximumSize(QtCore.QSize(200, 200))
        self.label_photoField.setText("")
        self.label_photoField.setObjectName("label_photoField")
        self.verticalLayout.addWidget(self.label_photoField)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_signature = QtWidgets.QLabel(self.infoTab)
        self.label_signature.setObjectName("label_signature")
        self.verticalLayout.addWidget(self.label_signature)
        self.label_signatureField = QtWidgets.QLabel(self.infoTab)
        self.label_signatureField.setMaximumSize(QtCore.QSize(200, 200))
        self.label_signatureField.setText("")
        self.label_signatureField.setObjectName("label_signatureField")
        self.verticalLayout.addWidget(self.label_signatureField)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(-1, 20, -1, -1)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.infoTab)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.label_nameField = QtWidgets.QLabel(self.infoTab)
        self.label_nameField.setObjectName("label_nameField")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_nameField)
        self.label_fatherHusband = QtWidgets.QLabel(self.infoTab)
        self.label_fatherHusband.setObjectName("label_fatherHusband")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_fatherHusband)
        self.label_fatherHusbandField = QtWidgets.QLabel(self.infoTab)
        self.label_fatherHusbandField.setObjectName("label_fatherHusbandField")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_fatherHusbandField)
        self.label_dob = QtWidgets.QLabel(self.infoTab)
        self.label_dob.setObjectName("label_dob")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_dob)
        self.label_dobField = QtWidgets.QLabel(self.infoTab)
        self.label_dobField.setObjectName("label_dobField")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_dobField)
        self.label_gender = QtWidgets.QLabel(self.infoTab)
        self.label_gender.setObjectName("label_gender")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_gender)
        self.label_genderField = QtWidgets.QLabel(self.infoTab)
        self.label_genderField.setObjectName("label_genderField")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_genderField)
        self.label_village = QtWidgets.QLabel(self.infoTab)
        self.label_village.setObjectName("label_village")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_village)
        self.label_villageField = QtWidgets.QLabel(self.infoTab)
        self.label_villageField.setObjectName("label_villageField")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_villageField)
        self.label_block = QtWidgets.QLabel(self.infoTab)
        self.label_block.setObjectName("label_block")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_block)
        self.label_blockField = QtWidgets.QLabel(self.infoTab)
        self.label_blockField.setObjectName("label_blockField")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_blockField)
        self.label_district = QtWidgets.QLabel(self.infoTab)
        self.label_district.setObjectName("label_district")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_district)
        self.label_districtField = QtWidgets.QLabel(self.infoTab)
        self.label_districtField.setObjectName("label_districtField")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_districtField)
        self.label_state = QtWidgets.QLabel(self.infoTab)
        self.label_state.setObjectName("label_state")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_state)
        self.label_stateField = QtWidgets.QLabel(self.infoTab)
        self.label_stateField.setObjectName("label_stateField")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_stateField)
        self.label_pincode = QtWidgets.QLabel(self.infoTab)
        self.label_pincode.setObjectName("label_pincode")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_pincode)
        self.label_pincodeField = QtWidgets.QLabel(self.infoTab)
        self.label_pincodeField.setObjectName("label_pincodeField")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.label_pincodeField)
        self.label_mobile = QtWidgets.QLabel(self.infoTab)
        self.label_mobile.setObjectName("label_mobile")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_mobile)
        self.label_mobileField = QtWidgets.QLabel(self.infoTab)
        self.label_mobileField.setObjectName("label_mobileField")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.label_mobileField)
        self.label_email = QtWidgets.QLabel(self.infoTab)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.label_emailField = QtWidgets.QLabel(self.infoTab)
        self.label_emailField.setObjectName("label_emailField")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.label_emailField)
        self.label_profession = QtWidgets.QLabel(self.infoTab)
        self.label_profession.setObjectName("label_profession")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_profession)
        self.label_professionField = QtWidgets.QLabel(self.infoTab)
        self.label_professionField.setObjectName("label_professionField")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.label_professionField)
        self.label_office = QtWidgets.QLabel(self.infoTab)
        self.label_office.setObjectName("label_office")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_office)
        self.label_officeField = QtWidgets.QLabel(self.infoTab)
        self.label_officeField.setObjectName("label_officeField")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.label_officeField)
        self.label_membershipType = QtWidgets.QLabel(self.infoTab)
        self.label_membershipType.setObjectName("label_membershipType")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_membershipType)
        self.label_membershipTypeField = QtWidgets.QLabel(self.infoTab)
        self.label_membershipTypeField.setObjectName("label_membershipTypeField")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.label_membershipTypeField)
        self.label_shares = QtWidgets.QLabel(self.infoTab)
        self.label_shares.setObjectName("label_shares")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_shares)
        self.label_sharesField = QtWidgets.QLabel(self.infoTab)
        self.label_sharesField.setObjectName("label_sharesField")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.label_sharesField)
        self.label_openingDate = QtWidgets.QLabel(self.infoTab)
        self.label_openingDate.setObjectName("label_openingDate")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_openingDate)
        self.label_openingDateField = QtWidgets.QLabel(self.infoTab)
        self.label_openingDateField.setObjectName("label_openingDateField")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.label_openingDateField)
        self.editButton = QtWidgets.QPushButton(self.infoTab)
        self.editButton.setObjectName("editButton")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.editButton)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.tabWidget.addTab(self.infoTab, "")
        self.loanTab = QtWidgets.QWidget()
        self.loanTab.setObjectName("loanTab")
        self.tabWidget.addTab(self.loanTab, "")
        self.transactionTab = QtWidgets.QWidget()
        self.transactionTab.setObjectName("transactionTab")
        self.tabWidget.addTab(self.transactionTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(memberPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(memberPage)

    def retranslateUi(self, memberPage):
        _translate = QtCore.QCoreApplication.translate
        memberPage.setWindowTitle(_translate("memberPage", "memberName"))
        self.label_photo.setText(_translate("memberPage", "Photo"))
        self.label_signature.setText(_translate("memberPage", "Signature"))
        self.label_name.setText(_translate("memberPage", "NAME :"))
        self.label_nameField.setText(_translate("memberPage", "TextLabel"))
        self.label_fatherHusband.setText(_translate("memberPage", "FATHER/HUSBAND :"))
        self.label_fatherHusbandField.setText(_translate("memberPage", "TextLabel"))
        self.label_dob.setText(_translate("memberPage", "DOB :"))
        self.label_dobField.setText(_translate("memberPage", "TextLabel"))
        self.label_gender.setText(_translate("memberPage", "GENDER :"))
        self.label_genderField.setText(_translate("memberPage", "TextLabel"))
        self.label_village.setText(_translate("memberPage", "VILLAGE :"))
        self.label_villageField.setText(_translate("memberPage", "TextLabel"))
        self.label_block.setText(_translate("memberPage", "BLOCK :"))
        self.label_blockField.setText(_translate("memberPage", "TextLabel"))
        self.label_district.setText(_translate("memberPage", "DISTRICT :"))
        self.label_districtField.setText(_translate("memberPage", "TextLabel"))
        self.label_state.setText(_translate("memberPage", "STATE :"))
        self.label_stateField.setText(_translate("memberPage", "TextLabel"))
        self.label_pincode.setText(_translate("memberPage", "PINCODE :"))
        self.label_pincodeField.setText(_translate("memberPage", "TextLabel"))
        self.label_mobile.setText(_translate("memberPage", "MOBILE :"))
        self.label_mobileField.setText(_translate("memberPage", "TextLabel"))
        self.label_email.setText(_translate("memberPage", "EMAIL :"))
        self.label_emailField.setText(_translate("memberPage", "TextLabel"))
        self.label_profession.setText(_translate("memberPage", "PROFESSION :"))
        self.label_professionField.setText(_translate("memberPage", "TextLabel"))
        self.label_office.setText(_translate("memberPage", "OFFICE :"))
        self.label_officeField.setText(_translate("memberPage", "TextLabel"))
        self.label_membershipType.setText(_translate("memberPage", "MEMBERSHIP TYPE :"))
        self.label_membershipTypeField.setText(_translate("memberPage", "TextLabel"))
        self.label_shares.setText(_translate("memberPage", "SHARES :"))
        self.label_sharesField.setText(_translate("memberPage", "TextLabel"))
        self.label_openingDate.setText(_translate("memberPage", "OPENING DATE :"))
        self.label_openingDateField.setText(_translate("memberPage", "TextLabel"))
        self.editButton.setText(_translate("memberPage", "Edit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.infoTab), _translate("memberPage", "Info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.loanTab), _translate("memberPage", "Loans"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transactionTab), _translate("memberPage", "Transactions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    memberPage = QtWidgets.QWidget()
    ui = Ui_memberPage()
    ui.setupUi(memberPage)
    memberPage.show()
    sys.exit(app.exec_())

