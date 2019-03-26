from  paramiko import SSHClient
import getpass

class CapstoneProject():
    def __init__(self):
        self.hostname = raw_input('IP Address:')
        self.username = raw_input('Username:')
        self.password = getpass.getpass('Password:')
        self.filename = open(raw_input('File Path/Name:'), 'w')
        self.words = self.filename.write('Hello There')
        self.port = 22
    def Connection(self, hostname, username, password):
        remote = SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=hostname, username=username, password=password)
def main():
    CapstoneProject()

if __name__ == '__main__':
    main()
