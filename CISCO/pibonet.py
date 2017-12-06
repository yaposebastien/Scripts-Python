from __future__ import absolute_import, division, print_function
#!/usr/bin/env python3

"""
Cette ligne suivante permet d'executer les scripts quelque soit la version de Python
les functions concernees par ce dualisme de version sont absolute, divison, print_funtion.
"""
#import de librairies
import netmiko
import json


print('Beginning of Pi Bot network')

#Creation de la connection
connection = netmiko.ConnectHandler(ip='192.168.10.2', device_type='cisco_ios', 
                                    username='pi', password='!PiNetw@rk2017!')
print(connection.send_command('show clock'))
connection.disconnect()
