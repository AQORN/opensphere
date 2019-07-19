# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(491, 611)
        LoginWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label = QtWidgets.QLabel(LoginWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 491, 161))
        self.label.setStyleSheet("background-color: rgb(73, 105, 146);")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(LoginWindow)
        self.textEdit.setGeometry(QtCore.QRect(40, 180, 391, 121))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(LoginWindow)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 330, 411, 61))
        self.textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit_2.setLineWidth(0)
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(LoginWindow)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 421, 1))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: rgb(126, 126, 126);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(LoginWindow)
        self.label_6.setGeometry(QtCore.QRect(360, 30, 111, 101))
        self.label_6.setStyleSheet("background-color: rgb(73, 105, 146);")
        self.label_6.setObjectName("label_6")
        self.login_btn = QtWidgets.QPushButton(LoginWindow)
        self.login_btn.setGeometry(QtCore.QRect(250, 570, 71, 28))
        self.login_btn.setAutoDefault(True)
        self.login_btn.setDefault(False)
        self.login_btn.setObjectName("login_btn")
        self.help_btn = QtWidgets.QPushButton(LoginWindow)
        self.help_btn.setGeometry(QtCore.QRect(410, 570, 71, 28))
        self.help_btn.setAutoDefault(False)
        self.help_btn.setObjectName("help_btn")
        self.label_2 = QtWidgets.QLabel(LoginWindow)
        self.label_2.setGeometry(QtCore.QRect(60, 410, 111, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.hostname_comboBox = QtWidgets.QComboBox(LoginWindow)
        self.hostname_comboBox.setGeometry(QtCore.QRect(190, 410, 221, 22))
        self.hostname_comboBox.setTabletTracking(False)
        self.hostname_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.hostname_comboBox.setEditable(True)
        self.hostname_comboBox.setObjectName("hostname_comboBox")
        self.password_lineEdit = QtWidgets.QLineEdit(LoginWindow)
        self.password_lineEdit.setGeometry(QtCore.QRect(190, 470, 221, 22))
        self.password_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.close_btn = QtWidgets.QPushButton(LoginWindow)
        self.close_btn.setGeometry(QtCore.QRect(330, 570, 71, 28))
        self.close_btn.setAutoDefault(False)
        self.close_btn.setObjectName("close_btn")
        self.checkBox = QtWidgets.QCheckBox(LoginWindow)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(190, 500, 221, 20))
        self.checkBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox.setObjectName("checkBox")
        self.username_lineEdit = QtWidgets.QLineEdit(LoginWindow)
        self.username_lineEdit.setGeometry(QtCore.QRect(190, 440, 221, 22))
        self.username_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.label_3 = QtWidgets.QLabel(LoginWindow)
        self.label_3.setGeometry(QtCore.QRect(60, 440, 111, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(LoginWindow)
        self.label_4.setGeometry(QtCore.QRect(60, 470, 111, 20))
        self.label_4.setObjectName("label_4")
        self.errorLabel = QtWidgets.QLabel(LoginWindow)
        self.errorLabel.setGeometry(QtCore.QRect(60, 535, 391, 20))
        self.errorLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setTabOrder(self.hostname_comboBox, self.username_lineEdit)
        LoginWindow.setTabOrder(self.username_lineEdit, self.password_lineEdit)
        LoginWindow.setTabOrder(self.password_lineEdit, self.checkBox)
        LoginWindow.setTabOrder(self.checkBox, self.login_btn)
        LoginWindow.setTabOrder(self.login_btn, self.close_btn)
        LoginWindow.setTabOrder(self.close_btn, self.help_btn)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "OpenSphere Client"))
        self.label.setText(_translate("LoginWindow", "<html><head/><body><p><br/></p><p><span style=\" font-size:14pt; color:#ffffff;\">  OpenSphere</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">  Client</span></p></body></html>"))
        self.textEdit.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">OpenSphere 1.0.0 is an open-source software client designed to manage a physical Linux-based virtualization host.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The latest version of this client can be downloaded from GitHub at https://github.com/AQORN/opensphere/STABLE or directly from the OpenX host itself on Port 8080 (i.e. http://10.20.30.40:8080).</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To directly manage a single host, enter the IP address or host name.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To manage multiple hosts, enter the IP address or name of an OpenStack Keystone endpoint.</span></p></body></html>"))
        self.label_6.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\":/images/images/globe.png\"/></p></body></html>"))
        self.login_btn.setText(_translate("LoginWindow", "Login"))
        self.help_btn.setText(_translate("LoginWindow", "Help"))
        self.label_2.setText(_translate("LoginWindow", "IP address / Name:"))
        self.close_btn.setText(_translate("LoginWindow", "Close"))
        self.checkBox.setText(_translate("LoginWindow", "Use Windows session credentials"))
        self.label_3.setText(_translate("LoginWindow", "User name:"))
        self.label_4.setText(_translate("LoginWindow", "Password:"))

import OpenSphere_rc