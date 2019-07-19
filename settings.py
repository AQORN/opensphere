import configparser, os.path
from os import path
from PyQt5.QtWidgets import QWidget

class settings(QWidget):

    def put_working_config(hst):
        config = configparser.ConfigParser()
        config['DEFAULT']['host'] = hst
        with open('.working', 'w') as configfile:
            config.write(configfile)

    def get_working_config():
        if path.exists(".working"):
            config = configparser.ConfigParser()
            config.read('.working')
            cfg = config['DEFAULT']['host']
            return cfg

    def get_hosts():
        if path.exists("settings.ini"):
            config = configparser.ConfigParser()
            config.read('settings.ini')
            hosts = config['DEFAULT']['hosts']
            #for host in config.items( "hosts" ):
                #do something
            return hosts

    def add_host(h):
        if not path.exists("settings.ini"):
            config = configparser.ConfigParser()
            config['DEFAULT']['hosts'] = h
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
            create_working = settings.put_working_config(h)
        else:
            dont_add = False
            config = configparser.ConfigParser()
            config.read('settings.ini')
            a = config['DEFAULT']['hosts']
            s = a.strip().split(',')
            for x in s:
                x = x.strip()
                if h == x :
                    dont_add = True
            if dont_add == False:
                config['DEFAULT']['hosts'] = a + ',' + h
                with open('settings.ini', 'w') as configfile:
                    config.write(configfile)
                create_working = put_working_config(h)


