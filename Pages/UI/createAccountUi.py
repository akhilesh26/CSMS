# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pages/UI/createAccount.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 374)
        Form.setStyleSheet("margin:5px;\n"
"padding:3px;\n"
"\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.memberIdLineEdit = QtWidgets.QLineEdit(Form)
        self.memberIdLineEdit.setReadOnly(True)
        self.memberIdLineEdit.setObjectName("memberIdLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.memberIdLineEdit)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nameLineEdit = QtWidgets.QLineEdit(Form)
        self.nameLineEdit.setReadOnly(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.accountTypeComboBox = QtWidgets.QComboBox(Form)
        self.accountTypeComboBox.setObjectName("accountTypeComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.accountTypeComboBox)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.termLineEdit = QtWidgets.QLineEdit(Form)
        self.termLineEdit.setObjectName("termLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.termLineEdit)
        self.amountLineEdit = QtWidgets.QLineEdit(Form)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.amountLineEdit)
        self.durationLineEdit = QtWidgets.QLineEdit(Form)
        self.durationLineEdit.setObjectName("durationLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.durationLineEdit)
        self.accountNoLineEdit = QtWidgets.QLineEdit(Form)
        self.accountNoLineEdit.setObjectName("accountNoLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.accountNoLineEdit)
        self.openningDateEdit = QtWidgets.QDateEdit(Form)
        self.openningDateEdit.setObjectName("openningDateEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.openningDateEdit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.createAccountPushButton = QtWidgets.QPushButton(Form)
        self.createAccountPushButton.setObjectName("createAccountPushButton")
        self.verticalLayout.addWidget(self.createAccountPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Deposit Form"))
        self.label.setText(_translate("Form", "Member Id:"))
        self.label_3.setText(_translate("Form", "Name:"))
        self.label_4.setText(_translate("Form", "Account Type:"))
        self.label_5.setText(_translate("Form", "Account No:"))
        self.label_7.setText(_translate("Form", "Openning Date:"))
        self.label_2.setText(_translate("Form", "Term (in months): "))
        self.label_6.setText(_translate("Form", "Amount:"))
        self.label_8.setText(_translate("Form", "Duration (in months):"))
        self.createAccountPushButton.setText(_translate("Form", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

