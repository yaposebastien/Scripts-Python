"""
The goal of this script is to automate certain tasks of system
administration by using the concept of POO
"""
import weakref  #Module permettant d'ajouter les elements de la classe Servers dans la liste(listOfServers)
import paramiko
import os
import smtplib

#Credentials to log into the servers
username = 'pi'
password = '!PiNetw@rk2017!'
port = 5555


##Creation de la classe Servers
class Servers:
    Total_Des_Servers = 0   
    listOfServers = [] #Creation d'une liste qui va recevoir les addresses IP des servers

    def __init__(self, ipServer, detailServer):
        self.ipServer = ipServer
        self.detailServer = detailServer
        #Cette ligne permet d'ajouter un server cree dans la liste listOfServers       
        self.__class__.listOfServers.append(weakref.proxy(self))
        Servers.Total_Des_Servers += 1 #Incremente le nombre de servers fonctionels apres creation

    def displayMyServers(self):
        return '{} {} '.format(self.ipServer, self.detailServer)


    def updatedServers(hostname, port, username, password):
        sshConnexion = paramiko.SSHClient()
        sshConnexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshConnexion.load_system_host_keys()
        sshConnexion.connect(hostname, port, username, password)
        stdin, stdout, stderr = sshConnexion.exec_command('sudo apt-get update -y ')
        print(stdout.read())
        sshConnexion.close()




if __name__ == '__main__':

    #Instanciation of class Servres or adding some servers to my class servers
    srvTomcat = Servers('10.10.10.245', 'Debian Jessie')
    srvYunohost = Servers('10.10.10.246', 'Debian Jessie')
    srvSms = Servers('10.10.10.244', 'Debian Jessie')

    #Usage of the function displayMyServers() to check the list
    #print(srvTomcat.displayMyServers()) 
    print(Servers.displayMyServers(srvTomcat))
    print(srvTomcat.ipServer)
    print(Servers.Total_Des_Servers)

    try:

        for server in Servers.listOfServers:
            print('#'*79)
            print(f'Connection au server : {server.ipServer}')
            Servers.updatedServers(server.ipServer, port, username, password)
    
    except Exception as ex:
        print(ex.message) 
