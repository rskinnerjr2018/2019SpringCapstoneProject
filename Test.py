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
        self.show = PanXapi.show(PanXapi(api_username=self.username, api_password=self.password, hostname=self.hostname)
                                 , xpath='/config/devices/entry/network/interface')

    def connection(self):
        self.connection_info()
    def api_call(self):
        if (self.generate_key == 'y') or (self.generate_key == 'Y') or \
                (self.generate_key == 'yes') or (self.generate_key == 'YES') or (self.generate_key == 'Yes'):
            filename = open(raw_input('Filename/Path:'), 'w')
            filename.write(self.connection_info)
            show_file = open(raw_input('What file do you want to write the show command to?:'), 'w')
            show_file.write(self.show)
            PanXapi.keygen(self.connection_info)
            PanXapi.show(self.show)
        if (self.generate_key == 'n') or (self.generate_key == 'N') or (self.generate_key == 'No') or (self.generate_key
         == 'NO'):
            show_file = open(raw_input('What file do you want to write the show command to?:'), 'w')
            show_file.write(self.show)
            PanXapi.show(self.show)
def main():
    CapstoneProject()

if __name__ == '__main__':
    main()
