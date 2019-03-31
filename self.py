from pan.xapi import PanXapi
def main():
    PanXapi.keygen(PanXapi(api_username='admin', api_password='admin', hostname='192.168.1.254'))
    PanXapi.port = 22
    PanXapi.cmd_xml(PanXapi(api_username='admin', api_password='admin', hostname='192.168.1.254'),cmd='<show><system><info></info></system></show>')
if __name__ == '__main__':
    main()

