
from unidecode import unidecode
from clean_text import clean_text



def extract_prescription(text):
    cleaned_lines = clean_text(text)
    extracted_lines = []
    caract_debut = "Ordonnance"
    caract_fin = "Signature"

    # Recherche de l'indice de la ligne contenant "Ordonnance"
    indices_debut = [i for i, ligne in enumerate(cleaned_lines) if unidecode(caract_debut).lower() in unidecode(ligne).lower()]
    indices_fin = [i for i, ligne in enumerate(cleaned_lines) if unidecode(caract_fin).lower() in unidecode(ligne).lower()]

    if indices_debut:
        # Prendre la première occurrence de "Ordonnance" et ajouter 1 pour obtenir la ligne suivante
        indice_debut = indices_debut[0] + 1

    else:
        print(f"Indice de début : {caract_debut} non trouvé")
        return []

    # Vérification s'il y a au moins une ligne le caract de fin"
    if indices_fin:
        indice_fin = indices_fin[0]
    else:
        print(f"Indice de fin : {caract_fin} non trouvé")
        return []

    # Extraction de la partie entre "Ordonnance" et "Signature"
    prescription = cleaned_lines[indice_debut:indice_fin]

    for ligne in prescription:
        if ligne is not None:
            extracted_lines.append(ligne)

    return extracted_lines

