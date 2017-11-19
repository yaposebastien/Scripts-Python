#Creer un fichier et ajoute des nombres de 10 a 10000

fichier = open("createfile.txt", "w")

for i in range(10,1000) :
	fichier.write(str(i) + "\n")

fichier.close()
