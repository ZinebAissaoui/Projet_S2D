## OCR -- PDF to text
import os

from PDF_To_Text.pdf_to_text import Extraction
#extracteur=Extraction("C:\Users\zaiss\OneDrive\Documents\GitHub\Projet_S2D\P0001\PDF\CRradio.pdf") # Insérer le nom de pdf, avant fait glisser le document dans la zone fichier à gauche
#export_lignes_fichier = extracteur.export_lignes("C:\Users\zaiss\OneDrive\Documents\GitHub\Projet_S2D\P0001\Text\CRradio.txt")



# Remplacez "Extraction" par le nom de votre classe

# Répertoire d'entrée pour les fichiers PDF
input_directory = r"C:\\Users\\zaiss\\OneDrive\\Documents\\GitHub\\Projet_S2D\\P0001\\PDF\\"

# Répertoire de sortie pour les fichiers texte
output_directory = r"C:\\Users\\zaiss\\OneDrive\\Documents\\GitHub\\Projet_S2D\\P0001\\Text\\"

# Parcours de tous les fichiers dans le répertoire d'entrée
for filename in os.listdir(input_directory):
    if filename.endswith(".pdf"):
        # Création du chemin complet pour le fichier PDF
        pdf_filepath = os.path.join(input_directory, filename)

        # Création du nom de fichier pour le fichier texte
        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_filepath = os.path.join(output_directory, txt_filename)

        # Création de l'instance de la classe Extraction
        extracteur = Extraction(pdf_filepath)

        # Exportation des lignes dans le fichier texte
        extracteur.export_lignes(txt_filepath)
