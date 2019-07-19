import sys, os, paramiko
from paramiko import client
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QDialog
from PyQt5.QtCore import Qt, QEvent, QObject, QEventLoop, QTimer
from settings import settings

class login_functions():

    def testSSH(self, ip, user, pwd):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname = ip, username = user, password = pwd, port = '2221')
            ssh.close()
            return True
        except Exception as e:
            return str(e)

    def testPing(host):
        response = os.system("ping " + host)
        if response == 0:
            return True
        else:
            return 'Host not reachable.'

    def StatusMsg(self, msg):
        self.errorLabel.setText(msg)
        loop = QEventLoop()
        QTimer.singleShot(5000, loop.quit)
        loop.exec_()
        self.errorLabel.setText('')

class opensphere_functions():

    def menu():
        self.errorLabel.setText(msg)
        loop = QEventLoop()
        QTimer.singleShot(5000, loop.quit)
        loop.exec_()
        self.errorLabel.setText('')
