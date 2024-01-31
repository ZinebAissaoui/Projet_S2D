# Nettoyage du texte

import re
from unidecode import unidecode

def clean_text(text):
    # Diviser le texte en lignes
    lines = text.split('\n')

    # Nettoyer chaque ligne
    cleaned_lines = []
    for line in lines:
        # Supprimer les caractères non alphanumériques (sauf les espaces)
        cleaned_line = re.sub(r'[^a-zA-Z0-9À-ÿ\s]', '', line)
        cleaned_lines.append(cleaned_line)


    return cleaned_lines
