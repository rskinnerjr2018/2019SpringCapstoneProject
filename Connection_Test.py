#Test connection to Palo Alto Firewall
from pan import xapi

def main():

    xapi.PanXapi(api_username= 'XML', api_password='xmladmin',
                 api_key='LUFRPT11YTVGTEF4NDNqb1FhNjhJTlo5ZFhiR3BWcjQ9VEZQUzlHQzlibTZNMklLTmMySUpNUT09',
                 hostname='192.168.1.254')

    xapi.PanXapi.cmd_xml(cmd='show system info')

    print(xapi.PanXapi.cmd_xml(cmd='show system info'))


main()