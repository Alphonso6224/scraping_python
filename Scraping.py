import requests
from bs4 import BeautifulSoup
import re


class Scraping:
    def __init__ (self, url):
        self.url = url
        
    def connection(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Erreur lors de la requête pour la pagne principal: {response.status_code}")
            return None
            
            
    def scrape_and_save_content(self):
        try:
            main_html_content = self.connection(self.url)
        
            if main_html_content:
                # Analyse du HTML avec Beautifulsoup
                soup = BeautifulSoup(main_html_content, 'html.parser')
                
                # Récupération de tous les liens
                links = soup.find_all("a")
                
                # Ouvrir un seul fichier pour stocker le contenu de toutes les pages
                with open("contenu_global.txt", 'w', encoding='utf_8') as global_file:
                    # Parcours de chaque lien
                    for link in links:
                        link_url = link.get("href")
                        
                        if link_url and link_url.startswith("http"):
                            link_html_content = self.connection(link_url)
                            
                            if link_html_content:
                                link_soup = BeautifulSoup(link_html_content, 'html.parser')
                                text_content = link_soup.get_text()
                                cleaned_text = re.sub(r'\s+', ' ', text_content)
                                print(cleaned_text)
                                global_file.write(f"Contenu de {link_url}:\n{cleaned_text}\n\n")
                            else:
                                print(f"Impossible de récupérer le contenu de {link_url}")
            else:
                print("Erreur lors de la requête pour la page principale")
        except Exception as e:
            print(f"Erreur: {e}")
        
            
            
            
if __name__ == "__main__":
    # Instanciation de la classe Scraping
    scraper = Scraping("https://www.jeconomise.fr/")
    scraper.scrape_and_save_content()
    print("Le contenue de toutes les pages a été enregistré avec succès")