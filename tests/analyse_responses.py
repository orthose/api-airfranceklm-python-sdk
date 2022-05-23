# Pour charger le fichier JSON de réponse dans un interpréteur
import pickle

with open('./reference_data', 'rb') as f:
    ref_data = pickle.load(f)

with open('./example_all_offers', 'rb') as f:
    all_offers = pickle.load(f)
