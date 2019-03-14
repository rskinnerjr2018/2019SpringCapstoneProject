# This is a practice script to detect if pan-python works
from pan import xapi
from paramiko import SSHClient
import getpass

password = getpass.getpass("Password: ")
port = 22

remote = SSHClient()
remote.load_system_host_keys()

remote.connect(hostname='172.16.203.251',port=22,username='admin',password=password)


def main():
    def __init__(self, arg1=None):
        self.arg1 = arg1
        xapi.PanXapi(api_username='audi_xml', api_password='admin', hostname='172.16.203.251',
                     api_key='LUFRPT14MW5xOEo1R09KVlBZNnpnemh0VHRBOWl6TGM9bXcwM3JHUGVhRlNiY0dCR0srNERUQT09', port='22')
        xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>')
        print(xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>'))


# Call main
if __name__ == '__main__':
    main()
