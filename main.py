# ################################################################################################ #
# ACCESS VM CONSOLE VIA JAVA APPLET VIA QT WEBKIT: https://www.tightvnc.com/release-jviewer2.php   #
# ################################################################################################ #

import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QDialog
from PyQt5.QtCore import Qt, QEvent, QObject, QEventLoop, QTimer
from functions import login_functions
from settings import settings

#Keep these lines during development so the UI to PY file conversion doesn't have to be performed over and over
os.system("pyuic5 start_ui.ui > start_ui.py") # Converts the ui to py on every launch
os.system("pyuic5 os_ui.ui > os_ui.py") # Converts the ui to py on every launch
os.system("pyuic5 prep_ui.ui > prep_ui.py") # Converts the ui to py on every launch
os.system("pyuic5 prep_progress_ui.ui > prep_progress_ui.py") # Converts the ui to py on every launch

from start_ui import Ui_LoginWindow

# When adding images within QT Designer, run:
# 'pyrcc5 -o OpenSphere_rc.py OpenSphere.qrc'
# to add/update the QRC file as python code for the project so it can be imported and display the image(s)

class Login(QDialog, Ui_LoginWindow):

    def __init__(self, parent=None):

        super(Login, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.close_btn.clicked.connect(self.close_btn_clicked)
        self.login_btn.clicked.connect(self.login_btn_clicked)

        #set combobox with previous hostnames
        hostnames = settings.get_hosts()
        if hostnames is not None:
            hostnames = hostnames.strip().split(',')
            for host in hostnames:
                self.hostname_comboBox.addItem(host)
        self.hostname_comboBox.setFocus()
        self.show()

    """ [ENTER] KEYPRESS CAPTURE """
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Enter:
                self.login_btn.clicked.connect(self.login_btn_clicked)
        return super(Login, self).eventFilter(obj, event)

    def close_btn_clicked(self):
        sys.exit()

    def login_btn_clicked(self):

        #################
        FASTLOGIN = True
        #################
        if FASTLOGIN == True:
            userText = 'openx'
            passText = 'openx'
            hostText = '127.0.0.1'
            portText = '2221'
        else:
            userText = self.username_lineEdit.text()
            passText = self.password_lineEdit.text()
            hostText = self.hostname_comboBox.currentText()
            portText = self.port_lineEdit.text()

        if userText=="":
            self.username_lineEdit.setFocus()
            self.password_lineEdit.setText('')
            login_functions.StatusMsg(self, 'A username is required.')
        elif passText=="":
            self.password_lineEdit.setFocus()
            self.password_lineEdit.setText('')
            login_functions.StatusMsg(self, 'A password is required.')
        elif hostText=="":
            self.hostname_comboBox.setFocus()
            self.password_lineEdit.setText('')
            login_functions.StatusMsg(self, 'A hostname or IP is required.')
        elif portText=="":
            self.port_lineEdit.setFocus()
            self.password_lineEdit.setText('')
            login_functions.StatusMsg(self, 'A port for SSH access to the host is required.')
        else:   ### LOGIN ROUTINE ###
            login_functions.StatusMsg(self, 'Testing connection...')
            pingResult = login_functions.testPing(hostText)
            if pingResult == True:
                login_functions.StatusMsg(self, 'Testing credentials...')
                testResult = login_functions.testSSH(self, hostText, portText, userText, passText)
                if testResult == True:
                    new_host = settings.add_host(hostText, portText, userText, passText)
                    from hostprep import PrepCheck
                    self.dialog = PrepCheck(self)
                    self.dialog.show()
                    self.hide()

                    """
                    from opensphere import OpenSphere
                    self.dialog = OpenSphere(self)
                    self.dialog.show()
                    self.hide()
                    """
                else:
                    self.password_lineEdit.setText('')
                    login_functions.StatusMsg(self, testResult)
            else:
                login_functions.StatusMsg(self, pingResult)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Login()
    #win = OpenSphere()
    sys.exit(app.exec_())


