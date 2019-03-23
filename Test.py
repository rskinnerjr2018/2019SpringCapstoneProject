# This is a practice script to detect if pan-python works
from pan import xapi
from paramiko import SSHClient
import getpass
#hostname = raw_input('Hostname:')
#username = raw_input("Username:")
#password = getpass.getpass("Password: ")
#filename = raw_input(('File Path/Name:'))
generate_key = raw_input('Do you want to generate an API Key:?')
def connection(hostname,username,password):
    remote = SSHClient()
    remote.load_system_host_keys()
    remote.connect(hostname=hostname, port=22, username=username, password=password)
def api_call(gnerate_key, self):
    self.xapi.Panxapi.keygen = None
    if (generate_key == 'y') or (generate_key == 'Y') or (generate_key == 'yes') or (generate_key == 'YES')  or (generate_key == 'Yes'):
        xapi.PanXapi.keygen(self)
        return
def file(filename):
    create_file= open(filename,'w')
    create_file.write('hello')


# Call main
if __name__ == '__main__':
    api_call(generate_key,self)
    #connection(hostname,username,password)
    #file(filename)