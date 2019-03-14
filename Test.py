# This is a practice script to detect if pan-python works
from pan import xapi
from paramiko import SSHClient
import getpass
Username = input('Username: ')
password = getpass.getpass("Password: ")
port = 22

remote = SSHClient()
remote.load_system_host_keys()

remote.connect(hostname='172.16.203.251',port=22,username=Username,password=password)


def main():
    def __init__(self, arg1=None):
        self.arg1 = arg1
        xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>')
        return



# Call main
if __name__ == '__main__':
    main()
