from paramiko import SSHClient
import getpass
def main(hostname,username,password):
        remote = SSHClient()
        remote.load_system_host_keys()
        remote.connect(hostname=hostname, port=22, username=username, password=password)
        remote.connect.close()
hostname = raw_input('Hostname:')
username = raw_input('Username:')
password = getpass.getpass("Password: ")
if __name__ == '___main___':
    main()