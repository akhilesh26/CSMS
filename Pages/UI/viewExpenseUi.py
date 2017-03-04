# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewExpense.ui'
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
        self.costRadioButton = QtWidgets.QRadioButton(Form)
        self.costRadioButton.setObjectName("costRadioButton")
        self.horizontalLayout.addWidget(self.costRadioButton)
        self.typeRadioButton = QtWidgets.QRadioButton(Form)
        self.typeRadioButton.setObjectName("typeRadioButton")
        self.horizontalLayout.addWidget(self.typeRadioButton)
        self.expenseIdRadioButton = QtWidgets.QRadioButton(Form)
        self.expenseIdRadioButton.setObjectName("expenseIdRadioButton")
        self.horizontalLayout.addWidget(self.expenseIdRadioButton)
        self.searchLineEdit = QtWidgets.QLineEdit(Form)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.expenseList = QtWidgets.QListWidget(Form)
        self.expenseList.setObjectName("expenseList")
        self.horizontalLayout_2.addWidget(self.expenseList)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "View Expense"))
        self.costRadioButton.setText(_translate("Form", "Cost"))
        self.typeRadioButton.setText(_translate("Form", "Type"))
        self.expenseIdRadioButton.setText(_translate("Form", "Expense Id"))
        self.searchLineEdit.setPlaceholderText(_translate("Form", "Type here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

