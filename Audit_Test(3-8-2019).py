# Test Script to detect if pan-python works
from pan import xapi
x=''
y=''
class Connection(object):


	def __init__(self,xapi,api_username,api_password,hostname,api_key):
		self.xapi=xapi
		self.api_username=api_username
		self.api_password=api_password
		self.hostname=hostname
		self.api_key=api_key
		
	def start(__init__):
		x = xapi.PanXapi(api_username='XML', api_password='xmladmin', hostname='192.168.1.254',
					 api_key='LUFRPT11YTVGTEF4NDNqb1FhNjhJTlo5ZFhiR3BWcjQ9VEZQUzlHQzlibTZNMklLTmMySUpNUT09')
		y = xapi.PanXapi.cmd_xml(self.xapi, cmd='show system info')
		

def main():
	call=Connection(xapi, 'XML', 'xmladmin', '192.168.1.254',
					'LUFRPT11YTVGTEF4NDNqb1FhNjhJTlo5ZFhiR3BWcjQ9VEZQUzlHQzlibTZNMklLTmMySUpNUT09')
	print(Connection.start(__init__))

# Call main
if __name__ == '__main__':
	main()