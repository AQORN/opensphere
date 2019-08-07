import sys, os, paramiko
from paramiko import client
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QDialog
from PyQt5.QtCore import Qt, QEvent, QObject, QEventLoop, QTimer
from settings import settings
from ast import literal_eval

class login_functions():

    def testSSH (self, ip, pt, user, pwd):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname = ip, username = user, password = pwd, port = pt)
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

class host_functions():

    def _exe(self, cmd):
        cfg = settings.get_working_config()
        cfgList = cfg.split(':')
        ip = cfgList[0].strip()
        prt = cfgList[1].strip()
        usr = cfgList[2].strip()
        pwd = cfgList[3].strip()
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname = ip, username = usr, password = pwd, port = prt)
            (stdin, stdout, stderr) = ssh.exec_command(cmd)
            ln = stdout.readlines()
            ssh.close()
            return str(ln)

        except Exception as e:
            return str(e)

    def prep(self):
        os = getOS()
        if 'ubuntu' in os.lower:
            #https://wiki.libvirt.org/page/UbuntuKVMWalkthrough
            #UBUNTU:   sudo apt-get install qemu-kvm libvirt-bin libvirt-doc python-virtinst
            r = host_functions._exe(self, '')
        elseif 'ubuntu' in os.lower:
            #https://www.cyberciti.biz/faq/how-to-install-kvm-on-centos-7-rhel-7-headless-server/
            #CENTOS:   sudo yum install qemu-kvm libvirt libvirt-python libguestfs-tools virt-install
            r = host_functions._exe(self, '')

    def getOS(self):
        r = host_functions._exe(self, 'lsb_release -a')
        rd = literal_eval(r) #convert string input into dict
        ln = rd[1].strip()
        ln = ln.split(':')
        return ln[1].strip()

class vm_functions():

    def list_vms(self):
        r = host_functions._exe(self, 'virsh list --all')
        #rd = literal_eval(r)
        #ln = rd[1].strip()
        #ln = ln.split(':')
        return r #ln[1].strip()
