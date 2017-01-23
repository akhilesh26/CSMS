from Pages.UI.welcomeFormUi import Ui_Form as welcomeForm
from Pages.mainWindow import CSMSMain
from PyQt5 import QtWidgets

# implement later; return root info from databse
def getRootInfo():
    # username, password
    return "ut","12"

# first dialog box; username password verify`
class CSMSWelcome(QtWidgets.QDialog,welcomeForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('CSMS Software')
        self.enterPushButton.clicked.connect(self.verify)

    def verify(self):
        usernameInput = self.usernameLineEdit.text()
        passwordInput = self.passwordLineEdit.text()
        print(usernameInput,passwordInput)
        if (usernameInput,passwordInput)==getRootInfo():
            text = "Congrats! You can come in"
            # implement root user coming code
            self.close()
            self.initialiseMain()
        else:
            text = "Wrong username or password! Try again"
        text = "<b>"+text+"</b"
        self.welcomeMessageLabel.setText(text)

    def initialiseMain(self):
        csms2 = CSMSMain()
        csms2.show()

