from paramiko import SSHClient
import getpass

hostname = raw_input('Hostname:')
username = raw_input('Username:')
password = getpass.getpass("Password: ")
filename = raw_input(('File Path/Name:'))
def connect(hostname,username,password):
        remote = SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=hostname, port=22, username=username, password=password)
def file(filename):
    create_file= open(filename, 'w')
    create_file.write('hello')
def main():
    connect(hostname,username,password)
    file(filename)
if __name__ == '___main___':
    main()