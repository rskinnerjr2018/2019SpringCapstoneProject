import getpass
from pan.xapi import PanXapi
class CapstoneProject():
    def __init__(self):
        self.hostname = raw_input('IP Address:')
        self.username = raw_input('Username:')
        self.password = getpass.getpass('Password:')
        self.filename = open(raw_input('File Path/Name:'), 'w')
        self.words = self.filename.write('Hello There')
        self.port = 22
        self.connection_info = PanXapi.keygen(PanXapi(api_username=self.username, api_password=self.password,
                                                       hostname=self.hostname))

    def Connection(self):
        self.connection_info()
        PanXapi.cmd_xml(self.connection_info, cmd='<show><system><info></info></system></show>')
        print (self.connection_info)

def main():
    CapstoneProject()

if __name__ == '__main__':
    main()
