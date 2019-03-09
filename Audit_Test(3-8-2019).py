# Test Script to detect if pan-python works

from pan import xapi
class Connection(object):
	
	def __init__(self,ssh,xapi,api_key):
		self.ssh=ssh
		self.xapi=xapi
		self.api_key=api_key
		
	def start(__init__):
		xapi.PanXapi(api_username='XML', api_password='xmladmin', hostname='192.168.1.254', api_key='LUFRPT11YTVGTEF4NDNqb1FhNjhJTlo5ZFhiR3BWcjQ9VEZQUzlHQzlibTZNMklLTmMySUpNUT09')
		xapi.PanXapi.cmd_xml(self,cmd='show system info')
		

def main():
	print(xapi.PanXapi.cmd_xml(self.xapi, cmd='show system info'))
	
# Call main
if __name__ == '__main__':
	main()