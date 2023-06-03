from __future__ import absolute_import, division, print_function
import os, shutil, glob
import subprocess
#!/usr/bin/env python3.7

"""
This function aims to automatically convert all the PDF files of the Journal
officiel. It is very laborious and tedious to copy and paste the content of all 
the text. 

STEPS:
1) Read all the download pdf files
2) Create folder based on the name of the file
3) Create subfolders (Decrets, Decisions, Annonces and Arretes)
4) Move files into the folder containing journal already converted
"""

# Variables of the script
JO_SRC = '/home/yankees/PROJECTS/Projects/JOURNAL_ORDINAIRE/DATA/DOWNLOAD/2020'
JO_DEST = '/home/yankees/PROJECTS/Projects/JOURNAL_ORDINAIRE/DATA/JOURNAUX_OFFICIELS/2020'
TREATED_DEST = '/home/yankees/PROJECTS/Projects/JOURNAL_ORDINAIRE/DATA/DOWNLOAD/2020/DEJA_TRAITES'

#Function to convert the pdf to txt file
def journal_extractor():
    for root, dirs, files in os.walk(JO_SRC, topdown=False):
        for journal in files:
            print(f'Journal: {journal}')
            print(f'Dossier: {os.path.join(root)}')
            print(f'fichier: {os.path.join(root, journal)}')

            print(f'Dossier distant: {os.path.join(JO_DEST,folder_creator(journal))}')
            distantFolder = os.path.join(JO_DEST,folder_creator(journal))
            print(f'fichier distant: {os.path.join(distantFolder, journal)}')
            
            #Create the journal folder
            folder_creator(journal)
            shutil.copyfile(os.path.join(root, journal), os.path.join(distantFolder, journal))

            #Convert
            subprocess.call(["pdftotext", "-raw", os.path.join(distantFolder, journal)])

            #Now, it is time to move the file into the folder of files already converted.
            shutil.move(os.path.join(root, journal), os.path.join(TREATED_DEST, journal))
           
           


#Function to create the folder based on the name of the journal for normal
#journal which filename looks like: jo_17_20200227_182523.pdf
def folder_creator(journal):
    if(len(journal) >= 1):
         path = os.path.join(JO_DEST, journal[0:-11])
         #Check if the folder exist
         if(not os.path.exists(path)):
             os.mkdir(path)
             #Creation of the folder Public
             public_path_folder = os.path.join(path, "Public")
             os.mkdir(public_path_folder)

             #Now, inside the created folder, we will create folder 
             # subfolders (Decrets, Decisions, Annonces and Arretes)
             subfolders = ["Decrets", "Decisions", "Annonces", "Arretes"]
             for subfolder in subfolders:
                 newPath = os.path.join(public_path_folder, subfolder)
                 os.mkdir(newPath)

    return path



#Main program
journal_extractor()
