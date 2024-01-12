import json
import boto3

# questions = {
#     "Intentions de quitter le pays": ["Oui", "Non", "Incertain"],
#     "Tranche d'âge": ["Moins de 20 ans", "20-24 ans", "25-29 ans", "30-34 ans", "35 ans et plus"],
#     "Niveau d'études": ["Licence 1", "Licence 2", "Licence 3", "Licence 4", "DUT 1", "DUT 2"],
#     "Pays visé": ["États-Unis", "Canada", "Royaume-Uni", "Australie", "France", "Autre (précisez)"],
#     "Raison du départ": ["Opportunités professionnelles", "Recherche académique", "Qualité de vie", "Autre (précisez)"],
#     "Objectif du départ": ["Études supplémentaires", "Raisons professionnelles", "Raisons personnelles"],
#     "Durée prévue à l'étranger": ["Moins d'un an", "1-2 ans", "3-5 ans", "Plus de 5 ans"],
#     "Intention de retour dans le pays d'origine": ["Oui", "Non", "Incertain"]
# }

# # Affichage des questions et saisie des réponses
# reponses = {}
# for question, options in questions.items():
#     print(question)
#     for i, option in enumerate(options, 1):
#         print(f"{i}. {option}")

#     while True:
#         reponse = input("\nVotre réponse (entrez le numéro correspondant) : ")
#         try:
#             reponse = int(reponse)
#             if 1 <= reponse <= len(options):
#                 reponses[question] = options[reponse - 1]
#                 break
#             else:
#                 print("Veuillez entrer un numéro valide.")
#         except ValueError:
#             print("Veuillez entrer un numéro.")

# # Affichage des réponses
# data=[]
# print("\nRéponses enregistrées :")
# for question, reponse in reponses.items():
#     data.append(f"{question}: {reponse}")


# file_name="file.json"

# try:
#     with open(file_name, "r") as f:
#         load_data = json.load(f)
# except FileNotFoundError:
#     # Si le fichier n'existe pas, initialisez load_data avec un dictionnaire vide
#     load_data = {}

# # ... Votre code ...
# # print(data)

# # Pour enregistrer des données
# load_data[len(load_data)]=data
# with open(file_name, "w") as f:
#     json.dump(load_data, f)

# with open(file_name, "r") as f:
#     load_data = json.load(f)
    
# print(load_data) 

aws_access_key_id = 'AKIA4MTWNDW3BWTY3GGR'
aws_secret_access_key = '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'

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
# s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)


# lyen kote fichye a ye sou AWS
bucket_name = 'abellard'
object_key = 'file.json'

# Lekti fichye a
# response = s3.get_object(Bucket=bucket_name, Key=object_key) 
# file_content = response['Body'].read().decode('utf-8')

# televèse konti nan yon fichye
# updated_content = 
s3.put_object(Bucket=bucket_name, Key=object_key)