# This is a practice script to detect if pan-python works
from pan import xapi
from paramiko import SSHClient
import getpass
hostname = raw_input('Hostname:')
Username = raw_input("Username:")
password = getpass.getpass("Password: ")
def connection(hostname,username,password)
    remote = SSHClient()
    remote.load_system_host_keys()
    remote.connect(hostname=hostname, port=22, username=username, password=password)
def main():
    def __init__(self, arg1=None):
        self.arg1 = arg1
        xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>')
        print(xapi.PanXapi.cmd_xml(self,cmd='<show><system><info></info></system></show>'))

# Call main
if __name__ == '__main__':
    connection()
    main()
