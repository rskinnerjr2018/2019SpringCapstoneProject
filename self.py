from pan.xapi import PanXapi
def main():
    PanXapi.keygen(PanXapi(api_username='admin', api_password='admin', hostname='172.16.203.251'))
    PanXapi.port = 22
    #if PanXapi.cmd_xml(PanXapi(api_username='admin', api_password='admin', hostname='172.16.203.251'),
                  #  cmd='<show><system><info></info></system></show>'):
        #PanXapi.cmd_xml(PanXapi(api_username='admin', api_password='admin', hostname='172.16.203.251'),
                       # cmd='<show><system><info></info></system></show>')



if __name__ == '__main__':
    main()

