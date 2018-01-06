"""
The goal of this script is to automate certain tasks of system
administration by using the concept of POO
"""
import weakref  #Module permettant d'ajouter les elements de la classe Servers dans la liste(listOfServers)

class Servers:
    
    listOfServers = [] #Creation d'une liste qui va recevoir les addresses IP des servers

    def __init__(self, ipServer, detailServer):
        self.ipServer = ipServer
        self.detailServer = detailServer
        
        self.__class__.listOfServers.append(weakref.proxy(self))
        
        Servers.Total_Servers += 1

    def displayMyServers(self):
        return '{} {} '.format(self.ipServer, self.detailServer)


if __name__ == '__main__':

    #Instanciation of class Servres or adding some servers to my class servers
    srvTomcat = Servers('10.10.10.245', 'Debian Jessie')
    srvYunohost = Servers('10.10.10.246', 'Debian Jessie')
    srvSms = Servers('10.10.10.244', 'Debian Jessie')

    #Usage of the function displayMyServers() to check the list
    #print(srvTomcat.displayMyServers()) 
    print(Servers.displayMyServers(srvTomcat))
    print(srvTomcat.ipServer)
    print(Servers.Total_Servers)

    for server in Servers.listOfServers:
        print(server.ipServer)
