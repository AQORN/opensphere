# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prep_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrepCheckWindow(object):
    def setupUi(self, PrepCheckWindow):
        PrepCheckWindow.setObjectName("PrepCheckWindow")
        PrepCheckWindow.resize(238, 182)
        PrepCheckWindow.setWindowTitle("")
        self.label = QtWidgets.QLabel(PrepCheckWindow)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PrepCheckWindow)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 161, 20))
        self.label_2.setObjectName("label_2")
        self.configure_btn = QtWidgets.QPushButton(PrepCheckWindow)
        self.configure_btn.setGeometry(QtCore.QRect(20, 130, 91, 28))
        self.configure_btn.setObjectName("configure_btn")
        self.cancel_btn = QtWidgets.QPushButton(PrepCheckWindow)
        self.cancel_btn.setGeometry(QtCore.QRect(120, 130, 91, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.host_Label = QtWidgets.QLabel(PrepCheckWindow)
        self.host_Label.setGeometry(QtCore.QRect(20, 50, 191, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.host_Label.setFont(font)
        self.host_Label.setStyleSheet("color: rgb(0, 0, 255);")
        self.host_Label.setObjectName("host_Label")

        self.retranslateUi(PrepCheckWindow)
        QtCore.QMetaObject.connectSlotsByName(PrepCheckWindow)

    def retranslateUi(self, PrepCheckWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("PrepCheckWindow", "Looks like this is a new host:"))
        self.label_2.setText(_translate("PrepCheckWindow", "Configure it automatically?"))
        self.configure_btn.setText(_translate("PrepCheckWindow", "Configure"))
        self.cancel_btn.setText(_translate("PrepCheckWindow", "Leave Alone"))
        self.host_Label.setText(_translate("PrepCheckWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

