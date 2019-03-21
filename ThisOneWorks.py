from pan import xapi
from paramiko import SSHClient
import getpass

def connect():
    hostname = input("Hostname:")
    username = input("Username:")
    password = getpass.getpass("Password: ")
    remote = SSHClient()
    remote.load_system_host_keys()
    remote.connect(hostname=hostname, port=22, username=username, password=password)
    remote.connect.close()

def main():
    connect()

if __name__ == '___main___':
    main()