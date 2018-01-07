"""
Script permettant d'envoyer un sms avec comme argument le message et le numero
"""
#!/usr/bin/env python3.6

import os    
import time
import weakref
from sys import argv

script, message = argv


class Contact:
	totalContacts = 0
	listOfContacts = []

	def __init__(self, nom, telephone):
		self.nom = nom
		self.telephone = telephone
		self.__class__.listOfContacts.append(weakref.proxy(self))
		#Contact.totalContacts +=1

	def afficherContacts(self):
		return '{} {} '.format(self.nom, self.telephone)



if __name__ == '__main__':
	
	#Liste de mes contacts
	Sebastien = Contact("Sebastien", "+12157305881")

	try:
		for personne in Contact.listOfContacts:
			print('#'*70)
			print(f'Envoi a {personne.nom} le  message suivant: \n {message}')
			phone = personne.telephone
			mess = message
			os.system('gammu sendsms TEXT "%s"  -text "%s"' %(phone,mess)) 
			time.sleep(30)
	except Exception as e:
		print(e)
