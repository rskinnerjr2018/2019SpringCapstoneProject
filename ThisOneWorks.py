from paramiko import SSHClient
import getpass
from pan import xapi
def connect(hostname,username,password):
        remote = SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=hostname, port=22, username=username, password=password)
def api(self,y, x):
    self.xapi=show
    x = xapi.PanXapi.show(self,xpath='show system info')
    print(x)
def main():
    connect()
    api()
hostname = raw_input('Hostname:')
username = raw_input('Username:')
password = getpass.getpass("Password: ")
if __name__ == '___main___':
    main()