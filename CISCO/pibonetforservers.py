#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import json
import paramiko

servers = """
10.10.10.245
10.10.10.246
""".strip().splitlines()

#Definition of credentials for my pi to run commands
username='pi'
password='!PiNetw@rk2017!'

def sshUpdateMyServers(hostname, port, username, password, command):
    sshClient = paramiko.SSHClient()                                   # create SSHClient instance

    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # AutoAddPolicy automatically adding the hostname and new host key
    sshClient.load_system_host_keys()
    sshClient.connect(hostname, port, username, password)
    stdin, stdout, stderr = sshClient.exec_command(command)
    print(stdout.read())

if __name__ == '__main__':
    sshUpdateMyServers('10.10.10.246', 22, 'pi', '!PiNetw@rk2017!', 'sudo apt-get update')
