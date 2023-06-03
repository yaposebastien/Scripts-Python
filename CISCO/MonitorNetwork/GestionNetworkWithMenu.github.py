'''
Features:
    check configuration of all devices
    Configure device
    Send alert sms and email to superUser
    Save in postgresql database each login and function excecute by the user

'''
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
import time
import smtplib
import subprocess



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

#Function allowing to list all the devices in my network
    def listOfDevices(self):
        return 'IP: {} -- TYPE: {} -- DESC: {} -- DEVIC: {}'.format(self.ipDevice, self.device_type, self.descriptionDevice, self.ciscoDevice)

#Funct
    def verificationAddress(ipToVerif):
        for device in Device.liste_Of_Devices:
            if device.ipDevice == ipToVerif:
                return True

    def displayDevices():
        print('###List of the devices in my network....###\n')
        for device in Device.liste_Of_Devices:
            print(Device.listOfDevices(device))


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

    def assignPortVlan():
        print('###Assigning port to a Vlan...###\n')
        ipAddress = input('Enter the IP address of the device:')
        vlanNumber = input('Enter your Vlan number :')
        answer = 'y'
        for device in Device.liste_Of_Devices:
            if device.ipDevice == ipAddress:
                while answer == 'y':
                    interfVlan = input('Enter the interface number : ')
                    connection = netmiko.ConnectHandler(ip=device.ipDevice, device_type=device.device_type, username=username, password=password)
                    print(connection.send_command('configure terminal'))
                    print(connection.send_command('interface {interfVlan}'))
                    print(connection.send_command('switchport mode access'))
                    print(connection.send_command('switchport access vlan {vlanNumber}'))
                    print(connection.send_command('exit'))
                    connection.close()
                    answer = input('Do you want to add another interface? y/n')

    def menuOfApplication():

            print(f'\n\t Part I: Switching Technologies.')
            print(f'\t\t Press[1] to display basic infos Switch in the Network. eg. Version, flash, etc.')
            print(f'\t\t Press[2] to set an interface description.')
            print(f'\t\t Press[3] to set Duplex Operation on the device.')
            print(f'\t\t Press[4] to set Operation Speed.')
            print(f'\t\t Press[5] to create Static VLAN.')
            print(f'\t\t Press[6] to assign Ports to a VLAN.')
            print(f'\n\t Part II: Routing Technologies: IPv4 and IPv6')
            print(f'\t\t Press[7] to display static route')
            print(f'\n\t Part III: WAN Technologies')
            print(f'\n\t Part IV: Infrastructure Services')
            print(f'\n\t Part V: Infrastructure Security')
            print(f'\n\t Part VI: Infrastructure Management')
            print(f'\n\t Press[Q]uit the application.\n')

            optionUser = input('Enter your choice : ')
            return optionUser


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

    def excecuteCommandes(ipAddress, *listeCommandes):
        if Device.verificationAddress(ipAddress):
            connection = netmiko.ConnectHandler(ip=ipAddress, device_type='cisco_ios', username=username, password=password)
            #Creating the folder to receive the output of commands of device
            folder_Of_Device = connection.base_prompt #Creates folder which name is hostname of Device
            os.mkdir(folder_Of_Device)
            for cmde in listeCommandes:
                print(f'\n ~~~~~Running the command : {cmde}')
                file_output = cmde.rstrip().replace(' ', '_') + '.conf'
                file_output = os.path.join(folder_Of_Device, file_output)
                with open(file_output, 'w') as output_cmde:
                    print(connection.send_command(cmde))
                    output_cmde.write(connection.send_command(cmde))
                    output_cmde.close()
        time.sleep(10)
        connection.disconnect()

    #This function sends me an email
    def sendMeAlertEmail(msg):
        servergmail = smtplib.SMTP('smtp.gmail.com', 587)
        servergmail.starttls()
        servergmail.login('youremail@gmail.com', 'passw0rd')
        servergmail.sendmail('youremail@gmail.com', 'youremail@gmail.com', msg)
        servergmail.quit()

    def formattingCiscoCommand(keyword, interface):
        subCommand = str(keyword) + ' ' +str(interface)
        return subCommand

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
            ##Catch which user who is logging and send me an alert with username and date
            logging_infos = subprocess.check_output("whoami && date ", shell=True)
            Device.sendMeAlertEmail(logging_infos)

            ###This option permits to display basic infos of the Switch
            if Device.menuOfApplication()== '1':
                Device.displayDevices()
                ipAddress = input('\t\t Enter Device IP address : ')
                Device.excecuteCommandes(ipAddress,'terminal length 0', 'show flash:', 'show version',
                                         'show mac-address-table', 'show running','show vlan')

            ###This option permits to set the interface description
            elif Device.menuOfApplication() == '2':
                Device.displayDevices()
                Device.setInterfaceDescription()




    except Exception as excpt:
        print(str(excpt.message))
