# This is a practice script to detect if pan-python works

import panxapi
def main():
    xapi.PanXapi(api_username='XML', api_password='xmladmin', hostname='192.168.1.254',
                 api_key='LUFRPT11YTVGTEF4NDNqb1FhNjhJTlo5ZFhiR3BWcjQ9VEZQUzlHQzlibTZNMklLTmMySUpNUT09')
    xapi.PanXapi.cmd_xml(self, cmd='show system info')
#Call main
if __name__ == '__main__':
    main()


	
# --------------------------------------------------------------------------------------------------------------------------------------------------	
	
	
user_choice = input('Save baseline or perform audit? ')


# practice code for file reading
# infile = open('file_name', 'r')
# file_contents = infile.read()
# infile.close()
# print(file_contents)


def decision(user_choice):
	if user_choice == 'Save baseline'
		baseline_file = open('Baseline.txt', 'w')
		baselineConfig = xapi.PanXapi.cmd_xml(self, cmd='show running config')
		baseline_file.write(baselineConfig)
	elif user_choice == 'perform audit'
		runningConfig_file = open('Running.txt', 'w')
		runningConfig = xapi.PanXapi.cmd_xml(self, cmd='show running config')
		runningConfig_file.write(runningConfig)
		comparison()

		
def comparison():
	baseline_file = open('Baseline.txt', 'r')
	runningConfig_file = open('Running.txt', 'r')
	
	
