# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newExpense.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(462, 313)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.expenseIdLabel = QtWidgets.QLabel(Form)
        self.expenseIdLabel.setObjectName("expenseIdLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.expenseIdLabel)
        self.expenseIdLineEdit = QtWidgets.QLineEdit(Form)
        self.expenseIdLineEdit.setObjectName("expenseIdLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.expenseIdLineEdit)
        self.expenditureTypeLabel = QtWidgets.QLabel(Form)
        self.expenditureTypeLabel.setObjectName("expenditureTypeLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.expenditureTypeLabel)
        self.expenditureTypeComboBox = QtWidgets.QComboBox(Form)
        self.expenditureTypeComboBox.setObjectName("expenditureTypeComboBox")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.expenditureTypeComboBox.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.expenditureTypeComboBox)
        self.expenditureCostLabel = QtWidgets.QLabel(Form)
        self.expenditureCostLabel.setObjectName("expenditureCostLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.expenditureCostLabel)
        self.expenditureCostLineEdit = QtWidgets.QLineEdit(Form)
        self.expenditureCostLineEdit.setObjectName("expenditureCostLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.expenditureCostLineEdit)
        self.paymentMethodLabel = QtWidgets.QLabel(Form)
        self.paymentMethodLabel.setObjectName("paymentMethodLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.paymentMethodLabel)
        self.paymentMethodComboBox = QtWidgets.QComboBox(Form)
        self.paymentMethodComboBox.setObjectName("paymentMethodComboBox")
        self.paymentMethodComboBox.addItem("")
        self.paymentMethodComboBox.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.paymentMethodComboBox)
        self.dateLabel = QtWidgets.QLabel(Form)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateDateEdit = QtWidgets.QDateEdit(Form)
        self.dateDateEdit.setProperty("showGroupSeparator", False)
        self.dateDateEdit.setCalendarPopup(True)
        self.dateDateEdit.setObjectName("dateDateEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dateDateEdit)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.submitButton = QtWidgets.QPushButton(Form)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout.addWidget(self.submitButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Expense"))
        self.expenseIdLabel.setText(_translate("Form", "Expense Id"))
        self.expenditureTypeLabel.setText(_translate("Form", "Expenditure Type"))
        self.expenditureTypeComboBox.setItemText(0, _translate("Form", "Furniture"))
        self.expenditureTypeComboBox.setItemText(1, _translate("Form", "Stationary"))
        self.expenditureTypeComboBox.setItemText(2, _translate("Form", "Computer"))
        self.expenditureTypeComboBox.setItemText(3, _translate("Form", "Rent"))
        self.expenditureTypeComboBox.setItemText(4, _translate("Form", "Employee Salary"))
        self.expenditureTypeComboBox.setItemText(5, _translate("Form", "Rent"))
        self.expenditureTypeComboBox.setItemText(6, _translate("Form", "Maintainance "))
        self.expenditureTypeComboBox.setItemText(7, _translate("Form", "Postage"))
        self.expenditureTypeComboBox.setItemText(8, _translate("Form", "Audit"))
        self.expenditureTypeComboBox.setItemText(9, _translate("Form", "Misc"))
        self.expenditureCostLabel.setText(_translate("Form", "Expenditure Cost"))
        self.paymentMethodLabel.setText(_translate("Form", "Payment Method"))
        self.paymentMethodComboBox.setItemText(0, _translate("Form", "Cash"))
        self.paymentMethodComboBox.setItemText(1, _translate("Form", "Cheque"))
        self.dateLabel.setText(_translate("Form", "Date"))
        self.submitButton.setText(_translate("Form", "Sumbit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

