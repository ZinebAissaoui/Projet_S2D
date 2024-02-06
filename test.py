import os

from CR.CR import extraction_CR_main
from Ordonnance.Data_Extraction import extract_prescription
# Répertoire d'entrée pour les fichiers PDF
input_directory = r"C:\\Users\\zaiss\\OneDrive\\Documents\\GitHub\\Projet_S2D\\P0001\\PDF\\"

# Répertoire de sortie pour les fichiers texte
output_directory = r"C:\\Users\\zaiss\\OneDrive\\Documents\\GitHub\\Projet_S2D\\P0001\\Text\\"
for filename in os.listdir(output_directory):
    
    if "ordonnance" in filename.lower():
        print("----------début traitement ordonance ----------------")
        output_file_path=os.path.join(output_directory, filename) 
        print(output_file_path)
        text = None
        try:
            with open(output_file_path, 'r') as output_file:
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
    