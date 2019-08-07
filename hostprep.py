import sys, os
from os import remove
from collections import deque
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTreeView, QFileSystemModel, QApplication, QMainWindow, qApp
from settings import settings
from functions import opensphere_functions, host_functions, vm_functions
from prep_ui import Ui_PrepCheckWindow
from prep_progress_ui import Ui_HostPrepProgressWindow

class PrepCheck(QMainWindow, Ui_PrepCheckWindow):

    def cancel_btn_clicked(self):
        sys.exit()

    def configure_btn_clicked(self):
        self.dialog = HostPrepProgress(self)
        self.dialog.show()
        self.hide()

    def __init__(self, parent=None):

        super(PrepCheck, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.configure_btn.clicked.connect(self.configure_btn_clicked)
        self.cancel_btn.clicked.connect(self.cancel_btn_clicked)
        cfg = settings.get_working_config()
        cfgList = cfg.split(':')
        host = cfgList[0].strip()
        self.host_Label.setText(host)
        self.show()



class HostPrepProgress(QMainWindow, Ui_HostPrepProgressWindow):

    def continue_btn_clicked(self):
        from opensphere import OpenSphere
        self.dialog = OpenSphere(self)
        self.dialog.show()
        self.hide()

    def __init__(self, parent=None):

        super(HostPrepProgress, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.continue_btn.clicked.connect(self.continue_btn_clicked)

        #self.host_Label.setText(host)
        self.show()
