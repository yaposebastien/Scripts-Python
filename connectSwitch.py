import paramiko

#Setting client connection

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.10.2', port=22, username='pi', password='!PiNetw@rk2017!')
stdin, stdout, stderr = ssh.exec_command('show users')
output = stdout.readlines()
print '\n'.join(output)
