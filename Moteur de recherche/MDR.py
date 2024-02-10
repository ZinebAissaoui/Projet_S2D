from sentence_transformers import SentenceTransformer, util
import torch
import pandas as pd
import json
from scipy.spatial.distance import cosine
import heapq
import numpy as np
embedder = SentenceTransformer('all-MiniLM-L6-v2')  ## embedding 
def mdr(file):
##################################################################    
# Charger le fichier JSON de consultation
    with open(file, 'r') as f:
    #with open('data.json', 'r') as f:
        data = json.load(f)
#################################################################
#################################################################
    # Créer une liste pour stocker les valeurs à écrire dans le fichier JSON
    values_to_write = []
    # Parcourir chaque consultation
    for consultation in data['Consultations']:
        # Parcourir chaque clé et valeur de la consultation
        for key, value in consultation.items():
            if value is not None:  # Vérifiez si la valeur n'est pas None
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            for key2, value2 in item.items():
                                if not isinstance(value2, float) and value2 is not None:  # Vérifiez si la valeur2 n'est pas None
                                    encoded_value = embedder.encode(value2, convert_to_tensor=True)
                                    values_to_write.append({
                                        "key": key,
                                        "sub_key": key2,
                                        "value":value2,
                                        "encoded_value": encoded_value.tolist()  # Convertir le tenseur en une liste Python
                                    })
                        elif not isinstance(item, int) and item is not None:  # Vérifiez si l'item n'est pas None
                            encoded_value = embedder.encode(item, convert_to_tensor=True)
                            values_to_write.append({
                                "key": key,
                                "value":item,
                                "encoded_value": encoded_value.tolist()  # Convertir le tenseur en une liste Python
                            })
                else:
                    if not isinstance(value, int):
                        encoded_value = embedder.encode(value, convert_to_tensor=True)
                        values_to_write.append({
                            "key": key,
                            "value":value,
                            "encoded_value": encoded_value.tolist()  # Convertir le tenseur en une liste Python
                        })
#################################################################
#################################################################
    # Écrire les valeurs dans un fichier JSON
                        # Pour stocker les embeddings
    with open('output2.json', 'w') as json_file:
        json.dump(values_to_write, json_file)
    with open('output2.json', 'r') as json_file:
        data = json.load(json_file)
#################################################################
#################################################################
    # On choisi comme input de recherche Globule, et on la ecrit avec une faute pour s'assurer que notre approche est performante
    input_encoded = np.array(embedder.encode("globue", convert_to_tensor=True)) 

    # Valeurs initiales pour stocker les similarités cosinus les plus élevées
    top_similarities = []  # Utilisez un tas pour maintenir les 5 meilleures similarités

    # Parcourir les valeurs encodées
    for item in data:
        if 'encoded_value' in item:
            encoded_value = np.array(item['encoded_value'])
            key = item['key']
            value = item['value']
            if 'sub_key' in item:
                sub_key = item['sub_key']
            else:
                sub_key = ""

            # Vérifier que les vecteurs sont unidimensionnels
            if input_encoded.ndim == 1 and encoded_value.ndim == 1:
                # Calculer la similarité cosinus entre input_encoded et encoded_value
                similarity = 1 - cosine(input_encoded, encoded_value)

                # Mettre à jour les 5 meilleures similarités
                if len(top_similarities) < 5:
                    heapq.heappush(top_similarities, (similarity, value, key, sub_key))
                else:
                    heapq.heappushpop(top_similarities, (similarity, value, key, sub_key))
            else:
                print("Les dimensions des vecteurs ne sont pas correctes")

    # Tri des similarités par ordre décroissant
    top_similarities.sort(reverse=True)
#################################################################
#################################################################
    # Affichage des 5 meilleures similarités
    print("Les 5 valeurs encodées les plus proches sont :")
    for similarity, value, key, sub_key in top_similarities:
        print("Clé :", key)
        print("Sub_key :", sub_key)
        print("Valeur :", value)
        print("Similarité cosinus :", similarity)
        print()

mdr("Consultations.Json")          