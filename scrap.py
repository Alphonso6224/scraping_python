import requests
from bs4 import BeautifulSoup
import re

url = "https://www.jeconomise.fr/"
response = requests.get(url)

if response.status_code == 200: 
    # Recupération du contenue de la page
    html_content = response.content
    
    # Analyse du html avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Recupérons tous les liens
    links= soup.find_all("a")


    # Ouvrir un seul fichier pour stocker le contenu de toutes les pages
    with open("contenu_global.txt", 'w', encoding='utf_8') as global_file:
    
        # Parcours de chaque lien
        for link in links:
            # Récupération l'url du lien
            link_url = link.get("href")
            
            # Vérification de la validiter de l'url
            if link_url and link_url.startswith("http"):
                # Envoi d'une nouvelle requête pour récuépérer le contenu de la page liée
                link_response = requests.get(link_url)
                
                # Vérification du statut de la requête
                if link_response.status_code == 200:
                    # Récupération du contenue de la page liée
                    link_html_content = link_response.content
                    
                    # Analyse du Html de la page liée
                    link_soup = BeautifulSoup(link_html_content, 'html.parser')
                    
                    # Extraction du texte brut (sans balises html)
                    text_content = link_soup.get_text()
                    
                    # Suppression des espaces répétés avec une expression régulière
                    cleaned_text = re.sub(r'\s+', ' ', text_content)
                    
                    # Traitement du contenu
                    
                    # Ecriture du texte nettoyé dans le ficher global
                    global_file.write(f"Contenue de {link_url}:\n{cleaned_text}\n\n")
                    
                    # print(f"Contenue de {link_url}:\n{cleaned_text}")
                else:
                    print(f"Erreur lors de la requête pour {link_url}: {link_response.status_code}")
                    
    print("Le contenu de toutes les pages a été enregistré dans le fichier contenu_global.txt.")
else: 
    print(f"Erreur lors de la requête pour la page principal: {response.status_code}")
    
