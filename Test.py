#This is a practice script to detect if pan-python works
from pan import xapi
from paramiko import SSHClient
import getpass
username=input('Username:')
password= getpass.getpass("Password: ")
port=22
def main():
    def __init__(self, arg1=None):
        self.arg1 = arg1
        remote = SSHClient()
        remote.set_missing_host_key_policy(AutoAddPolicy())
        remote.connect(ip, username=username,password=password)
        xapi.PanXapi(api_username='audi_xml', api_password='admin', hostname='172.16.203.251',
                 api_key='LUFRPT14MW5xOEo1R09KVlBZNnpnemh0VHRBOWl6TGM9bXcwM3JHUGVhRlNiY0dCR0srNERUQT09',port='22')
        xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>')
        print(xapi.PanXapi.cmd_xml(self, cmd= '<show><system><info></info></system></show>'))

#Call main
if __name__ == '__main__':
    main()
