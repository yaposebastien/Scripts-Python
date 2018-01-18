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
from getpass import getpass


#Creation de la Classe Device

class Device:
    liste_Of_Devices = []
    def __init__(self, ipDevice, typeOfDevice, descriptionDevice):
        self.ipDevice = ipDevice
        self.typeOfDevice = typeOfDevice
        self.descriptionDevice = descriptionDevice
        self.__class__.liste_Of_Devices.append(weakref.proxy(self))

    def listOfDevices(self):
        return 'IP: {} -- TYPE: {} -- DESC: {}'.format(self.ipDevice, self.typeOfDevice, self.descriptionDevice)

    def displayDevices():
        print('\nListe of the devices in my network.\n')
        for device in Device.liste_Of_Devices:
            print(Device.listOfDevices(device))


    def menuOfApplication():

            print(f'\nGestion Network Devices\n')
            print(f'\nPlease press any choice to proceed \n')
            print(f'\t Press[1] to ping device.')
            print(f'\t Press[2] to check device time.')
            print(f'\t Press[3] to set device time.')
            print(f'\t Press[4] to display configuration of device.')
            print(f'\t Press[5] to display any section of the device configuration.')
            print(f'\t Press[6] to display any port configuration of  the device.')
            print(f'\t Press[7] to display any section of the device configuration.')
            print(f'\t Press[8] to Backup up all the configuration.')
            print(f'\t Press[0] to quit the application.\n')


    def pingDevice(ipDevice):
        #Going to ping the device ten times
        os.system('sudo ping -c 10 "%s"' %(ipDevice))


    def checkTime():
        print(f'Checking the time of the device....')
        Connexion = netmiko.ConnectHandler(ip=ipDevice, device_type=typeOfDevice, username=username, password=password)
        print(Connexion.send_command('show clock')
        connexion.disconnect()

    def setTime():
        print(f'Setting the time of the device....')

    def displayDeviceConfiguration():
        print(f'Display the configuration of the device ....')





if __name__ == '__main__':

    #Instanciation of device class
    Conversion = Device('192.168.10.2', 'cisco_ios', 'Swicth 3650 and hostname Conversion')
    Faith = Device('192.168.30.3', 'cisco_ios', 'Router 3825 and hostname Faith First Router')
    Charity = Device('192.168.40.3', 'cisco_ios', 'Router 3825 and hostname Charity Second Router')

    username = get_entree('Username:')
    password = get_entree('Password:')

    done = False


    try:

        while done == False: #Cette loop permets d'executer le block suivant car done = False
            Device.displayDevices()
            print('\n')
            Device.menuOfApplication()
            print(f"Choice : ", end=' ')
            option = input()
            if option == "1":
                     print('Pinging device......')
                     for device in Device.liste_Of_Devices:
                        print('#'*80)
                        print(f'Ping the device: {device.descriptionDevice}\n')
                        Device.pingDevice(device.ipDevice)

            elif option == "0":
                print('End of application Gestion Network. Thanks!')
                done = True

    except Exception as expt:
        print(f'Error Application: {expt.message}')
