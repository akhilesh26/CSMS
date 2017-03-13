import sys
from PyQt5 import QtWidgets
from Pages.mainWindow import CSMSMain

from Pages.welcomeForm import CSMSWelcome


if __name__=='__main__':
    try:
        from Models.database import db
        from Models.member import Member
        print(db.session.query(Member).all())
    except Exception as e:
        print(e)
        print('Exitting safely')
        sys.exit(3)
    # initialise the application
    app = QtWidgets.QApplication(sys.argv)
    # login screen
    # csmsLogin = CSMSWelcome()
    # csmsLogin.show()
    # TEMP: UNCOMMENT 2 LINES ABOVE, COMMENT LINE BELOW
    try:
        csmsMain = CSMSMain()
    except Exception(e):
        print(e)
        sys.exit(2)
    csmsMain.show()
    # main window
    sys.exit(app.exec_())



