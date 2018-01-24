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
        print('\nListe of the devices in my network.\n')
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
        print('Setting Interface Description of the device.\n')
        ipAddress = input(
        interfaceName = input('Please enter the interface to set the description :')
        interfaceDescription = input


    def menuOfApplication():

            print(f'\nGestion Network Devices\n')
            print(f'\nPlease press any choice to proceed \n')
            print(f'\t Press[1] to display all the devices.')
            print(f'\t Press[2] to display basic infos Switch in the Network. eg. Version, flash, etc.')
            print(f'\t Press[3] to set an interface description.')
            print(f'\t Press[2] to check device time.')
            print(f'\t Press[3] to set device time.')
            print(f'\t Press[4] to display configuration of device.')
            print(f'\t Press[5] to display any section of the device configuration.')
            print(f'\t Press[6] to display any port configuration of  the device.')
            print(f'\t Press[7] to display any section of the device configuration.')
            print(f'\t Press[8] to Backup up all the configuration.')
            print(f'\t Press[0] to quit the application.\n')


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
            optionUser = input('Enter your choice :')
            if optionUser == '0':
                done = True
            elif optionUser == '1':
                Device.commandShowClock(username,password)
            elif optionUser == '2':
                Device.verificationCommandsSwitch()


    except Exception as excpt:
        print(str(excpt.message))
