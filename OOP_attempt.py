from  paramiko import SSHClient
import getpass

class Paramaters(object):
    def __init__(self):
        self.hostname = raw_input('IP Address:')
        self.username = raw_input('Username:')
        self.password = getpass.getpass('Password:')
        self.filename = raw_input('File Path/Name:')