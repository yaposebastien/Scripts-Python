#Creer une variable afficher en Hexadecimal

var = 1981
print(var)
print(id(var))
print(hex(id(var)))

#Declaration chaines

name = "Yapo \n Sebastien"
name
print(name)

#Declare une chaine sur plusieurs lignes avec """
phrase = """ Je tiens a maitriser ce langage
	de programmation pour l'ecriture de script reseau
	et de securite informatique """
print(phrase)

#Combiner deux chaines de characteres

nom = "Paul"
prenom = "Landry"

nom_complet = nom + ' ' + prenom
print nom_complet
 
#Manipulation de characteres
	#afficher les trois prmemiers characters de phrase

print phrase[0:2]

	#Afficher les 20 premiers en espacant de deux characteres
print phrase[0:20:2] 

#afficher Paul 20 fois
print nom*20
 
#Rechercher un charactere dans une chaine

print(phrase.find("ce"))
 
#Diviser une chaine de carac
print(phrase.split())
 
#Diviser en precisant le delimiteur
print(phrase.split("e"))
 
#Remplacer par un charactere precis

print(phrase.replace("e","klklklklk"))
 
#Affichage de variable
domain = "www.google.com"
ip = "8.8.8.8"
etoile = 2
print("Le nom de domaine est : %s" %domain + "IP address : %s" %ip + "etoile : %d" %etoile)

#Creation d'une liste
maListe = [1,"Abidjan", "Cote d'ivoire"]
print("La taille de ma liste" +str(len(maListe)))
 
#Afficher le second element de la liste
print("Le second element de ma liste est :" +maListe[1])
 
#Ajout d'un element a ma liste
maListe.append("Anyama")
print(maListe)

#Renverser ma liste
maListe.reverse()
print(maListe)
 
#Supprimer le dernier element de ma liste
maListe.pop()
print(maListe)
 
#Inserer a une position precise de ma liste
maListe.insert(2,"Abobo")
print(maListe)

#Supprimer un element a un emplacement specific
del maListe[3]
print(maListe)
