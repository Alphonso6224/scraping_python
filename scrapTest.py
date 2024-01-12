import requests
from bs4 import BeautifulSoup
 
# en tête utilisateur
headers = {'User-Agent': 'RobinsonRobot/1.0'}
url = "https://www.lemonde.fr/sante/"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Recupération du contenu de la page
    html_content = response.content
    # print(html_content)
else:
    print(f"Erreur lors de la requête: {response.status_code}")
    
# Analyse du Html avec BeautifulSoup:
soup = BeautifulSoup(html_content, 'html.parser')

# Exemple : Trouver tous les liens sur la page
# links = soup.find_all('a')
# for link in links: 
#     print(link.get('href'))

# Exemple : Extraire le texte de tous les paragraphes de la class "teaser_desc"
descriptions = soup.find_all('p', class_='teaser__desc')
# print(descriptions)
for description in descriptions:
    print(description.get_text())