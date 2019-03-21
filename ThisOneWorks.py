from paramiko import SSHClient
import getpass
from pan import xapi
def connect(hostname,username,password):
        remote = SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=hostname, port=22, username=username, password=password)
def api(self):
    self.xapi=xapi
    y = xapi.PanXapi.cmd_xml(self, cmd='show system info')
    print(y)
hostname = raw_input('Hostname:')
username = raw_input('Username:')
password = getpass.getpass("Password: ")
if __name__ == '___main___':
    main()