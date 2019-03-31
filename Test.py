# This is a practice script to detect if pan-python works
from pan.xapi import PanXapi
from pan import xapi
from paramiko import SSHClient
import getpass
#hostname = raw_input('Hostname:')
#username = raw_input("Username:")
#password = getpass.getpass("Password: ")
filename = raw_input(('File Path/Name:'))

generate_key = raw_input('Do you want to generate an API Key?:)
def connection(hostname,username,password):
    remote = SSHClient()
    remote.load_system_host_keys()
    remote.connect(hostname=hostname, port=22, username=username, password=password)
class apikeygen:
    def __init__(self):
        self.PanXapi = PanXapi
        self.keygen = xapi.PanXapi
        self.if_yes = generate_key
    def api_call(__init__,generate_key,y):
        if (generate_key == 'y') or (generate_key == 'Y') or (generate_key == 'yes') or (generate_key == 'YES')  or (generate_key == 'Yes'):
            self.if_yes = apikeygen()
            y = if_yes
            return y
def file(filename, y):
    y = if_yes
    create_file= open(filename,'w')
    create_file.write(if_yes)


# Call main
if __name__ == '__main__':
    apikeygen()
    #connection(hostname,username,password)
    file(filename, y)