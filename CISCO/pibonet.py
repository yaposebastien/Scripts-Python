from __future__ import absolute_import, division, print_function
#!/usr/bin/env python3

"""
Cette ligne suivante permet d'executer les scripts quelque soit la version de Python
les functions concernees par ce dualisme de version sont absolute, divison, print_funtion.
"""
#import de librairies
import netmiko
import json

#Listing Cisco devices

devices = """
192.168.10.3
192.168.10.4
""".strip().splitlines()

#Creditentials
device_type='cisco_ios'
username='pi'
password='!PiNetw@rk2017!'

#List of functions 

def menuOfActions():
    print('Please Make A Selection To Proceed : \n'
            +'\t Press [1] To Display the time'
            )
    

print('Beginning of Pi Bot network')

#Adding Exception handling for any issues with the connection or other reasons

menuOfActions()
    
#Calling the function and loop to display the time
for device in devices:
    try:   
        #Creation de la connection
        connection = netmiko.ConnectHandler(ip=device,device_type=device_type ,username=username, password=password)
        print(connection.send_command('show clock'))
        connection.disconnect()
    except Exception as e:
        print('ERROR SYSTEM : ' +e.message)
