# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findMember.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 405)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.phoneRadioButton = QtWidgets.QRadioButton(Form)
        self.phoneRadioButton.setObjectName("phoneRadioButton")
        self.horizontalLayout.addWidget(self.phoneRadioButton)
        self.nameRadioButton = QtWidgets.QRadioButton(Form)
        self.nameRadioButton.setObjectName("nameRadioButton")
        self.horizontalLayout.addWidget(self.nameRadioButton)
        self.memberIdRadioButton = QtWidgets.QRadioButton(Form)
        self.memberIdRadioButton.setObjectName("memberIdRadioButton")
        self.horizontalLayout.addWidget(self.memberIdRadioButton)
        self.searchLineEdit = QtWidgets.QLineEdit(Form)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.membersList = QtWidgets.QListWidget(Form)
        self.membersList.setObjectName("membersList")
        self.horizontalLayout_2.addWidget(self.membersList)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.phoneRadioButton.setText(_translate("Form", "Phone "))
        self.nameRadioButton.setText(_translate("Form", "Name"))
        self.memberIdRadioButton.setText(_translate("Form", "Member Id"))
        self.searchLineEdit.setPlaceholderText(_translate("Form", "Type here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

