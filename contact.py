import tkinter as tk
import sqlite3
import os

#Variables pour la taille de l'application
HAUTEUR = 800
LARGEUR = 800

#Fonction pour la creation de notre base de donnees
def base_donnees():
    global db, curseur
    db = sqlite3.connect('davidVersion3.db')
    curseur = db.cursor()
    curseur.execute('CREATE TABLE IF NOT EXISTS `utilisateur` (nom text, prenoms text, contact text )')

#Fonction pour sauvegarder un enregistrement
def enregistrer_utilisateur():
    if ( saisie_nom.get() != "" and saisie_prenoms.get() != ""):
        base_donnees()
        #Afficher valeur des champs saisis dans le formulaire
        print("Nom", saisie_nom.get())
        print("Prenoms", saisie_prenoms.get())
        print("Contact", saisie_telephone.get())
        curseur.execute("INSERT INTO `utilisateur` (nom, prenoms, contact) VALUES ( ?, ?, ?)", 
                        (saisie_nom.get(), saisie_prenoms.get(), saisie_telephone.get()))
        

        #Fermer la base de donnees
        db.commit()
        curseur.close()
        db.close()

       

   

#Fonction pour afficher tous les enregistrements
def afficher():
    #Reutiliser notre base de donnees et notre curseur
    
    base_donnees()
    curseur.execute("SELECT *, oid FROM utilisateur")
    liste = curseur.fetchall() #Permet de faire une requete et de recuperer tous les enregistrements dans la base de donnees
    enregistrements = ''

    for element in liste:
        enregistrements += str(element[3]) + "-" + " " + element[0] + " " + element[1] + " " + element[2] + "\n"
        print(element[0] + " " + element[1] + " " + element[2])
    
    #Affichage dans l'application
    affichage_libelle = tk.Label(zone_application, text=enregistrements)
    affichage_libelle.grid(row=16, column=0, columnspan=2)
   

     #Fermer la base de donnees
    db.commit()
    curseur.close()
    db.close()
       
    



#Fonction pour modifier un enregistrement
def modifier():

    utilisateur_id = saisie_oid.get()
    base_donnees()
    curseur.execute("SELECT * FROM utilisateur WHERE oid = " + utilisateur_id)

    #Recuperer l'unique utilisateur ayant cet identifiant
    utilisateurs = curseur.fetchall()
    
    #Fermer la base de donnees
    db.commit()
    curseur.close()
    db.close()


    #Creation d'une nouvelle fenetre pour la modification
    root = tk.Tk()
    root.title("Modifier Utilisateur")

    #Definition de la taille de la fenetre et son initialisation
    fenetre_principale = tk.Canvas(root, height=600, width=750)
    fenetre_principale.pack()

    #Fenetre zone de travail application
    zone_application = tk.Frame(root, bg='blue')
    zone_application.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
    #Definition de la taille de la fenetre et son initialisation
    fenetre_modification = tk.Canvas(root, height=700, width=700)
    fenetre_modification.pack()

    #Fenetre zone de travail application
    zone_modification = tk.Frame(root, bg='blue')
    zone_modification.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

    #Definition des champs

    global saisie_nom_modif
    global saisie_prenoms_modif
    global saisie_telephone_modif

    #Nom
    nom = tk.Label(zone_modification, text='Nom utilisateur: ', width=5, anchor="e", justify="left")
    nom.grid(row=0, column=0, columnspan=1, padx=1, pady=5, ipadx=50, sticky="W")

    saisie_nom_modif = tk.Entry(zone_modification, width=14)
    saisie_nom_modif.grid(row=0, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

    #Prenoms
    prenoms = tk.Label(zone_modification, text='Prenoms utilisateur: ', width=5, anchor="e", justify="left")
    prenoms.grid(row=1, column=0, columnspan=1, padx=2, pady=10, ipadx=50, sticky="W")

    saisie_prenoms_modif = tk.Entry(zone_modification, width=14)
    saisie_prenoms_modif.grid(row=1, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

    #Contact
    telephone = tk.Label(zone_modification, text='Telephone utilisateur: ', width=5, anchor="e", justify="left")
    telephone.grid(row=2, column=0, columnspan=1, padx=2, pady=10, ipadx=50, sticky="W")

    saisie_telephone_modif = tk.Entry(zone_modification, width=14)
    saisie_telephone_modif.grid(row=2, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

    #Parcourir liste des utilisateurs
    for utilisateur in utilisateurs:
        saisie_nom_modif.insert(0, utilisateur[0])
        saisie_prenoms_modif.insert(0, utilisateur[1])
        saisie_telephone_modif.insert(0, utilisateur[2])


    #Code pour le button enregistrer modification
    button_enregistrer = tk.Button(zone_modification, text="Sauvegarder modification", bg="blue", command=sauvegarder)
    button_enregistrer.grid(row=3, column=0, columnspan=1, padx=10, pady=10, ipadx=100)


#Fonction pour le bouton sauvegarder modification
def sauvegarder():
    base_donnees()
    utilisateur_id = saisie_oid.get()
    print("oid to sauvegarde" +utilisateur_id)
    curseur.execute("""UPDATE utilisateur SET 
                    nom = :nom_modif,
                    prenoms = :prenoms_modif,
                    contact = :contact_modif
                    WHERE oid = :oid """,
                    {
                        'nom_modif': saisie_nom_modif.get() ,
                        'prenoms_modif': saisie_prenoms_modif.get(),
                        'contact_modif': saisie_telephone_modif.get(),
                        'oid': utilisateur_id
                    })

    print("nouveau nom prenoms contact" + saisie_nom.get())
    #Recuperer l'unique utilisateur ayant cet identifiant
    utilisateurs = curseur.fetchall()

    
   
    
    #Fermer la base de donnees
    db.commit()
    curseur.close()
    db.close()

   


#Fonction pour supprimer un enregistrement
def supprimer():
  
    base_donnees()
    curseur.execute("DELETE FROM utilisateur WHERE oid = " + saisie_oid.get())
                     
    #Fermer la base de donnees
    db.commit()
    curseur.close()
    db.close()


#Variable pour definir la fenetre principale de l'application
root = tk.Tk()
root.title("Enregistreur de contacts")

#Definition de la taille de la fenetre et son initialisation
fenetre_principale = tk.Canvas(root, height=HAUTEUR, width=LARGEUR)
fenetre_principale.pack()

#Fenetre zone de travail application
zone_application = tk.Frame(root, bg='blue')
zone_application.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

#Definition des champs





#Nom
nom = tk.Label(zone_application, text='Nom utilisateur: ', width=5, anchor="e", justify="left")
nom.grid(row=0, column=0, columnspan=1, padx=1, pady=5, ipadx=50, sticky="W")

saisie_nom = tk.Entry(zone_application, width=14)
saisie_nom.grid(row=0, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

#Prenoms
prenoms = tk.Label(zone_application, text='Prenoms utilisateur: ', width=5, anchor="e", justify="left")
prenoms.grid(row=1, column=0, columnspan=1, padx=2, pady=10, ipadx=50, sticky="W")

saisie_prenoms = tk.Entry(zone_application, width=14)
saisie_prenoms.grid(row=1, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

#Contact
telephone = tk.Label(zone_application, text='Telephone utilisateur: ', width=5, anchor="e", justify="left")
telephone.grid(row=2, column=0, columnspan=1, padx=2, pady=10, ipadx=50, sticky="W")

saisie_telephone = tk.Entry(zone_application, width=14)
saisie_telephone.grid(row=2, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

#Code pour le button enregistrer
button_enregistrer = tk.Button(zone_application, text="Enregistrer", bg="blue", command=enregistrer_utilisateur)
button_enregistrer.grid(row=6, column=0, columnspan=1, padx=10, pady=10, ipadx=100)

#Code pour le button afficher la liste des contacts
button_afficher = tk.Button(zone_application, text="Afficher", bg="blue", command=afficher)
button_afficher.grid(row=7, column=0, columnspan=1, padx=10, pady=10, ipadx=100)

#Code pour supprimer un enregistrement
button_supprimer = tk.Button(zone_application, text="Supprimer utilisateur", bg="red", command=supprimer)
button_supprimer.grid(row=12, column=0, columnspan=1, padx=10, pady=10, ipadx=100)

#Code pour modifier un enregistrement
button_supprimer = tk.Button(zone_application, text="modifier utilisateur", bg="green", command=modifier)
button_supprimer.grid(row=13, column=0, columnspan=1, padx=10, pady=10, ipadx=100)

#Zone de saisie id a supprimer
oid = tk.Label(zone_application, text='ID utilisateur: ', width=5, anchor="e", justify="left")
oid.grid(row=11, column=0, columnspan=1, padx=2, pady=10, ipadx=50, sticky="W")
saisie_oid = tk.Entry(zone_application, width=14)
saisie_oid.grid(row=11, column=1, columnspan=1, padx=10, pady=10, ipadx=135)

root.mainloop()
