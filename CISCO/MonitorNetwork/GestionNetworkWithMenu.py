#!/usr/bin/env python3.6
from __future__ import absolute_import, division, print_function

"""
Ce programme permets de gerer le parc de switchs et routers dans ton reseau.
Par exemple: Afficher configuration equipements, Configurer le temps, etc...
"""

#Importation des librairies
import netmiko
import weakref
import os
import json
import identification
import signal

#Les deux lignes suivantes permettent la non apparution a l'ecran des  messages d interruptions
signal.signal(signal.SIGPIPE, signal.SIG_DFL) # IOError for Broken Pipe
signal.signal(signal.SIGINT, signal.SIG_DFL) # Interruption de clavier


#Creation de la Classe Device

class Device:
    liste_Of_Devices = []
    def __init__(self, ipDevice, device_type, descriptionDevice, ciscoDevice):
        self.ipDevice = ipDevice
        self.device_type = device_type #To Specify "cisco_ios"
        self.descriptionDevice = descriptionDevice
        self.ciscoDevice = ciscoDevice
        self.__class__.liste_Of_Devices.append(weakref.proxy(self))

    def listOfDevices(self):
        return 'IP: {} -- TYPE: {} -- DESC: {} -- DEVIC: {}'.format(self.ipDevice, self.device_type, self.descriptionDevice, self.ciscoDevice)

    def displayDevices():
        print('###List of the devices in my network....###\n')
        for device in Device.liste_Of_Devices:
            print(Device.listOfDevices(device))

    def verificationCommandsSwitch():
        with open('verificationCommandsSwitch.txt', 'r') as fichier_commandes_Switch:
            commandes = fichier_commandes_Switch.readlines()
            for singleCommand in commandes:
                for device in Device.liste_Of_Devices:
                    if device.ciscoDevice == 'Switch':
                        print(f'Excecution de la commande --> {singleCommand} sur le Switch : "%s"' %(device.ipDevice))
                        connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
                        dossier = connection.base_prompt
                        os.mkdir(dossier)
                        fichier = singleCommand.replace(' ','_')+ '.conf'
                        fichier = '/'.join((dossier, fichier))
                        with open(fichier, 'w') as sortie_commande:
                            sortie_commande.write(connection.send_command(singleCommand))
                        connection.close()
                        print()

    def setInterfaceDescription():
        print('###Setting Interface Description of the device....###\n')
        ipAddress = input('Please enter the IP address of the device:')
        interfaceName = input('Please enter the interface to set the description :')
        interfaceDescription = input('Enter the interface description:')
        for device in Device.liste_Of_Devices:
            if device.ipDevice == ipAddress:
                connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
                print(connection.send_command('configure terminal'))
                print(connection.send_command('interface {interfaceName}'))
                print(connection.send_command('description {interfaceDescription}'))
                connection.close()
            else:
                print(f'This IP address {ipAddress} does not exist in the network')

    def setDuplexOperation():
        print('###Setting the Duplex Operation of the device...###\n')
        ipAddress = input('Enter the IP address of the device:')
        interfaceName = input('Enter the interface to set the description :')
        duplexOperation = input('In which Duplex Operation do you want to set? full, auto or half')
        for device in Device.liste_Of_Devices:
            if device.ipDevice == ipAddress:
                connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
                print(connection.send_command('configure terminal'))
                print(connection.send_command('interface {interfaceName}'))
                print(connection.send_command('duplex {duplexOperation}'))
                connection.close()

    def setOperationSpeed():
        print('###Setting the Operation Speed  of the device...###\n')
        ipAddress = input('Enter the IP address of the device:')
        interfaceName = input('Enter the interface to set the speed :')
        speedOperation = input('In which Speed Operation do you want to set? 10, 100 or auto')
        for device in Device.liste_Of_Devices:
            if device.ipDevice == ipAddress:
                connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
                print(connection.send_command('configure terminal'))
                print(connection.send_command('interface {interfaceName}'))
                print(connection.send_command('speed {speedOperation}'))
                connection.close()

    def createStaticVlan():
        print('###Creating static Vlan of the device...###\n')
        ipAddress = input('Enter the IP address of the device:')
        vlanNumber = input('Enter your Vlan number :')
        vlanName = input('Enter your Vlan name :')

        for device in Device.liste_Of_Devices:
            if device.ipDevice == ipAddress:
                connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
                print(connection.send_command('configure terminal'))
                print(connection.send_command('vlan {vlanNumber}'))
                print(connection.send_command('name {vlanName}'))
                print(connection.send_command('exit'))
                connection.close()
    def menuOfApplication():

            print(f'\t Press[D]isplay all the devices.')
            print(f'\t Press[S]witching Technologies.')
            print(f'\t\t Press[1] to display basic infos Switch in the Network. eg. Version, flash, etc.')
            print(f'\t\t Press[2] to set an interface description.')
            print(f'\t\t Press[3] to set Duplex Operation on the device.')
            print(f'\t\t Press[4] to set Operation Speed.')
            print(f'\t\t Press[5] to create Static VLAN.')
            print(f'\t Press[R]outing Technologies: IPv4 and IPv6')
            print(f'\t Press[W]AN Technologies')
            print(f'\t Press[I]nfrastructure Services')
            print(f'\t Press[C]Infrastructure Security')
            print(f'\t Press[M]infrastructure Management')
            print(f'\t Press[Q]uit the application.\n')


    def pingDevice():
        #Going to ping the device ten times
        for device in Device.liste_Of_Devices:
            print(f'Pinging device : {device.ipDevice} {device.descriptionDevice}')
            os.system('sudo ping -c 10 "%s"' %(device.ipDevice))


    def commandShowClock( username, password):
        for device in Device.liste_Of_Devices:
            print('#'*80)
            print(f'Getting time of the device : {device.ipDevice} -- {device.descriptionDevice}')
            connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
            print(connection.send_command('show clock'))
            connection.disconnect()

if __name__ == '__main__' :

    print('#'*30 + "Application Network Monitor" + '#'*30)

    #Instanciation de la classe Device
    Conversion = Device('192.168.10.2', 'cisco_ios', 'Switch 3650 hostname conversiona', 'Switch')
    Faith = Device('192.168.30.3', 'cisco_ios', 'Router 3825 hostname Faith', 'Router')
    Charity = Device('192.168.40.3', 'cisco_ios', 'Router 3825 hostname Charity', 'Router')



    try:
        username, password = identification.identification()
        done = False
        while done == False:
            ##Insert sending sms to me for alert
            Device.menuOfApplication()
            optionUser = input('Enter your menu choice {D, S, I , etc.} :')
            optionSubMenu = input('Enter your subMenu choice {1, 2, 3, etc.} :')

            if optionUser == 'Q' or 'q':
                print(f'Exit Application Gestion Network')
                done = True
            elif optionUser == 'D':
                Device.displayDevices()
            elif optionUser == 'S' or 's' and optionSubMenu == '1':
                Device.verificationCommandsSwitch()
            elif optionUser == 'S' or 's' and optionSubMenu == '2':
                Device.setInterfaceDescription()
            elif optionUser == 'S' or 's' and optionSubMenu == '3':
                Device.setDuplexOperation()
            elif optionUser == 'S' or 's' and optionSubMenu == '4':
                Device.setOperationSpeed()


    except Exception as excpt:
        print(str(excpt.message))
