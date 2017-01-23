import sys
from PyQt5 import QtWidgets

from Pages.welcomeForm import CSMSWelcome

if __name__=='__main__':
    # initialise the application
    app = QtWidgets.QApplication(sys.argv)
    # login screen
    csmsLogin = CSMSWelcome()
    csmsLogin.show()
    # main window
    sys.exit(app.exec_())



