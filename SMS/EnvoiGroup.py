"""
Script permettant d'envoyer un sms a un group de personnes (Associations, Club, Amis, etc...).
Les  arguments ce script va etre le nom du groupe et le message. 
Comment excecuter ce script :
$python3.6 EnvoiGroup.py Cebstjoseph "Reunion ce Dimanche chez la famille Bationo"
"""
#!/usr/bin/env python3.6


import os
import json
import time
import weakref
from sys import argv

script, association, msge = argv


class Associations:
	listDesAssociations = []

	def __init__(self, nomAssociation, descriptionAssociation, fichier):
            self.nomAssociation = nomAssociation
            self.descriptionAssociation = descriptionAssociation
            self.fichier = fichier
            self.__class__.listDesAssociations.append(weakref.proxy(self))

	def afficherAssociations(self):
		return '{} {} {}'.format(self.nomAssociation, self.descriptionAssociation, self.listContactsAssociation)



if __name__ == '__main__':
	
	#Liste des associations
    CebStJoseph = Associations("CebStJoseph", "CEB St Joseph de la Paroisse d'Attecoube", "Cebstjoseph.json")
    Csfx = Associations("Csfx", "Centre Catholique Saint Francois Xavier", "Csfx.json")
    
    try:

        taille = len(msge)
        print(f'Nombre caracteres sms01: {taille}')
        print(f'Message : {msge}')
        print(f'Destinataire groupe : {association}')
        print(f"Chargement du fichier de contacts de {association +'.json'} ... ")

        with open('association + ".json"') as contacts:
                listContacts = json.load(contacts)
        
        for contact in listContacts:
            print('#' * 79)
            print(f"Envoi message a : {contact['nom']} {contact['telephone']} ")
            os.system('gammu sendsms TEXT "%s" -text "%s"' %(contact['telephone'],msge))
            time.sleep(30)
    except Exception as e:
        print('Erreur' + str(e))
