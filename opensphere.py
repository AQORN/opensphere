import sys, os
from os import remove
from collections import deque
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from functions import opensphere_functions
from settings import settings
from os_ui import Ui_OpenSphereWindow

class OpenSphere(QMainWindow, Ui_OpenSphereWindow):
    def __init__(self, parent=None):

        super(OpenSphere, self).__init__(parent)
        self.setupUi(self)
        host = settings.get_working_config()
        self.versionLabel.setText(host + ' - OpenSphere 0.0a build 1')
        self.vm_treeView.setRootIsDecorated(False)
        self.vm_treeView.setAlternatingRowColors(True)

        model = QStandardItemModel()
        self.vm_treeView.setModel(model)
        self.vm_treeView.setUniformRowHeights(True)

        parent1 = QStandardItem(host)
        child1 = QStandardItem('vm1')
        parent1.appendRow([child1])
        model.appendRow(parent1)

        # span container columns
        #self.vm_treeView.setFirstColumnSpanned(0, self.vm_treeView.rootIndex(), True)
        self.show()

