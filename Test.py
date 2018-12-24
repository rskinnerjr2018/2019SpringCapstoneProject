#This is a practice script to detect if pan-python works
from pan import xapi
def main():
    def __init__(self, arg1=None):
        self.arg1 = arg1
        xapi.PanXapi(api_username='admin', api_password='admin', hostname='192.168.1.2',
                 api_key='LUFRPT14MW5xOEo1R09KVlBZNnpnemh0VHRBOWl6TGM9bXcwM3JHUGVhRlNiY0dCR0srNERUQT09')
        xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>')
        print(xapi.PanXapi.cmd_xml(self, cmd='<show><system><info></info></system></show>'))
#Call main
if __name__ == '__main__':
    main()
