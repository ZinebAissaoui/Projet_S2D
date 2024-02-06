## OCR -- PDF to text
import os

from PDF_To_Text.pdf_to_text import Extraction
from CR.CR import extraction_CR_main
from Ordonnance.Data_Extraction import extract_prescription

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
print("######### Fin OCR ################")
# Compte rendu traitement
for filename in os.listdir(output_directory):
    if "cr" in filename.lower():
        print("----------début traitement compte rendu -----------")
        chemin_du_fichier = os.path.join(output_directory, filename) 
        caract_debut=input("entrez le premier mot du titre du compte rendu:")
        caract_fin=input("entrez le premier mot du pied du compte rendu:")
        dict_CR=extraction_CR_main(chemin_du_fichier,caract_fin,caract_debut)
        print("----------Fin traitement compte rendu ---------------")
        print(dict_CR)
    if "ordo" in filename.lower():
        print("----------début traitement ordonance ----------------")
        output_file_path=os.path.join(output_directory, filename) 
        text = None
        try:
            with open(output_file_path, 'r', encoding="windows-1252") as output_file:
                text = output_file.read()
                print(text)
        except FileNotFoundError:
            print(f"File '{output_file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


        # Extraire la prescription
        prescription= extract_prescription(text)

        # Stockage des métadonnées
        dictionnaire_Prescription = {
            "Prescription": prescription
        }
        print(dictionnaire_Prescription)
        print("----------Fin traitement compte rendu ---------------")
    





