# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prep_progress_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HostPrepProgressWindow(object):
    def setupUi(self, HostPrepProgressWindow):
        HostPrepProgressWindow.setObjectName("HostPrepProgressWindow")
        HostPrepProgressWindow.resize(759, 810)
        self.scrollArea = QtWidgets.QScrollArea(HostPrepProgressWindow)
        self.scrollArea.setGeometry(QtCore.QRect(30, 50, 701, 701))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 699, 699))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(HostPrepProgressWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.continue_btn = QtWidgets.QPushButton(HostPrepProgressWindow)
        self.continue_btn.setEnabled(False)
        self.continue_btn.setGeometry(QtCore.QRect(630, 770, 101, 28))
        self.continue_btn.setObjectName("continue_btn")

        self.retranslateUi(HostPrepProgressWindow)
        QtCore.QMetaObject.connectSlotsByName(HostPrepProgressWindow)

    def retranslateUi(self, HostPrepProgressWindow):
        _translate = QtCore.QCoreApplication.translate
        HostPrepProgressWindow.setWindowTitle(_translate("HostPrepProgressWindow", "Host Prep - Progress"))
        self.label.setText(_translate("HostPrepProgressWindow", "Progress Log:"))
        self.continue_btn.setText(_translate("HostPrepProgressWindow", "Continue . . ."))

