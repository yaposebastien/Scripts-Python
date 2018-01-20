#!/usr/bin/env python3.6
from __future__ import absolute_import, division, print_function

"""
Ce programme permets de gerer le parc de switchs et routers dans ton reseau.
Par exemple: Afficher configuration equipements, Configurer le temps, etc...
"""

#Importation des librairies
from getpass import getpass



def identification():
    username = input('Username : ')
    password = None
    while not password:
        password = getpass()
        password_test = getpass('Saisie encore mot de passe :')
        if password != password_test:
            print('Les deux mots de passe ne correspondent pas!')
            password = None
    return username, password


def saisie(curseur=''):
    try:
        line = input(curseur)
    except erreurNom:
        line = input(curseur)
    return line
