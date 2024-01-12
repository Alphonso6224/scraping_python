import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
connection = browser.get(url)
page = connection.soup

# Recuperation du seul formulaire de la page
recup_form_of_page = page.select('form')[0]

# Recuperation de tous les inputs de la page
recup_input_in_form = recup_form_of_page.select('input')

# Premier input
first_input = recup_input_in_form[0]
# second et dernier input
last_input = recup_input_in_form[1]

# Renseignons les differents champs du formulaire
first_input['value'] = 'zeus'
last_input['value'] = 'ThunderDude'

# Soumission du formulaire
page_after_soumission_form = browser.submit(recup_form_of_page, connection.url)

# Recuperons le contenue de notre nouvelle page
newPage = page_after_soumission_form.soup

# Recuperons le texte imprimer <title>All Profiles</title>
title = newPage.select('title')[0]

# Affichage du résultat
print(title.text)