import sys, os
from os import remove
from collections import deque
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from functions import opensphere_functions, host_functions, vm_functions
from settings import settings
from os_ui import Ui_OpenSphereWindow
from PyQt5.QtWidgets import QTreeView,QFileSystemModel,QApplication

class OpenSphere(QMainWindow, Ui_OpenSphereWindow):

    def change_host(self):
        for ix in self.vm_treeView.selectedIndexes():
            self.vm = ix.data(Qt.DisplayRole)
        self.versionLabel.setText(self.vm)

    def __init__(self, parent=None):

        super(OpenSphere, self).__init__(parent)
        self.setupUi(self)
        cfg = settings.get_working_config()
        cfgList = cfg.split(':')
        host = cfgList[0].strip()
        #dist = vm_functions.list_vms(self)
        dist = host_functions.getOS(self)
        self.versionLabel.setText(host + ' (' + dist + ') -  OpenSphere Version 0a')
        self.vm_treeView.setRootIsDecorated(False)
        self.vm_treeView.setAlternatingRowColors(True)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Hosts'])
        self.vm_treeView.setModel(model)
        self.vm_treeView.setUniformRowHeights(True)
        # populate data
        parent1 = QStandardItem(host)
        group_index = 0
        for j in range(5):
            child1 = QStandardItem('Child {}'.format(group_index*3+j))
            parent1.appendRow([child1])
        model.appendRow(parent1)
        # span container columns
        self.vm_treeView.setFirstColumnSpanned(group_index, self.vm_treeView.rootIndex(), True)
        index = model.indexFromItem(parent1)
        self.vm_treeView.expandAll()
        self.host = host
        self.show()

        self.vm_treeView.clicked.connect(self.change_host)


        """
        #Example:  select last row
        selmod = self.vm_treeView.selectionModel()
        index2 = model.indexFromItem(child3)
        selmod.select(index2, QItemSelectionModel.Select|QItemSelectionModel.Rows)
        """
