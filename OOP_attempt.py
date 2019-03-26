from  paramiko import SSHClient
import getpass

class CapstoneProject(object):
    def __init__(self):
        self.hostname = raw_input('IP Address:')
        self.username = raw_input('Username:')
        self.password = getpass.getpass('Password:')
        self.filename = raw_input('File Path/Name:')
        self.port = 22
    def Connection(hostname,username,password):
        remote = SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=hostname, username=username, password=password)
    def file(filename):
        create_file = open(filename, 'w')
        create_file.write('Hello World')
def main():
    CapstoneProject()

if __name__ == '__main__':
    main()
