import configparser, os.path, base64
from os import path
from PyQt5.QtWidgets import QWidget

class settings(QWidget):

    def encode(clear):
        key = '5W0chKHKjrkTOHBwkPJpASHZALtCbeazCPYPQrSyDsvmQArmCBDbLcbzex1g63OG'
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def decode(enc):
        key = '5W0chKHKjrkTOHBwkPJpASHZALtCbeazCPYPQrSyDsvmQArmCBDbLcbzex1g63OG'
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)

    def put_working_config(hst, prt, usr, pwd):
        ln = hst + ':' + prt + ':' + usr + ':' + pwd.rjust(32)
        cfg = settings.encode(ln)
        f = open('.working','w')
        f.write(cfg)
        f.close

    def get_working_config():
        if path.exists(".working"):
            f = open('.working', 'r')
            ln = f.read()
            f.close
            ln = str(ln)
            cfg = settings.decode(ln)
            return cfg

    def get_hosts():
        if path.exists("settings.ini"):
            config = configparser.ConfigParser()
            config.read('settings.ini')
            hosts = config['DEFAULT']['hosts']
            #for host in config.items( "hosts" ):
                #do something
            return hosts

    def add_host(h, prt, usr, pwd):
        if not path.exists("settings.ini"):
            config = configparser.ConfigParser()
            config['DEFAULT']['hosts'] = h
            with open('settings.ini', 'w') as configfile:
                config.write(configfile)
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
            create_working = settings.put_working_config(h, prt, usr, pwd)


