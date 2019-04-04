import getpass
from pan.xapi import PanXapi
class CapstoneProject():
    def __init__(self):
        self.hostname = raw_input('IP Address:')
        self.username = raw_input('Username:')
        self.password = getpass.getpass('Password:')
        self.generate_key = raw_input('Do you want to generate an API Key:?')
        self.port = 22
        self.connection_info = PanXapi.keygen(PanXapi(api_username=self.username, api_password=self.password,
                                                      hostname=self.hostname))
        self.filename = open(raw_input('File Path/Name:'), 'w')
        self.words = self.filename.write(self.connection_info)
        self.show = PanXapi.show(PanXapi(api_username=self.username, api_password=self.password,
                                                      hostname=self.hostname), xpath='/config/devices/entry/network/interface')

        self.show_file = open(raw_input('What file do you want the show command to?:'), 'w')
        self.show_write = self.show_file.write(str(self.show))
    def Connection(self):
        self.connection_info()
    def api_call(self):
        if (self.generate_key == 'y') or (self.generate_key == 'Y') or \
                (self.generate_key == 'yes') or (self.generate_key == 'YES') or \
                (self.generate_key == 'Yes'):
            PanXapi.keygen(self.connection_info)
            PanXapi.show(self.show)
        else:
            PanXapi.show(self.show)

def main():
    CapstoneProject()

if __name__ == '__main__':
    main()
