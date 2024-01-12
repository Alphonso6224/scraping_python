from urllib.request import urlopen

# Url du site
url = "http://olympus.realpython.org/profiles/aphrodite"
url1 ="http://olympus.realpython.org/profiles/poseidon"

# Utilisons urlopen() pour ouvrir la page web
page = urlopen(url)

# urlopen retourne une réponse http
print(page)

# Extraction du html
html_bytes = page.read()

# Decodage de bytes en string en utilisant utf8
html = html_bytes.decode("utf-8")
# print(html)

title_index = html.find("<title>") #index de la balise <title>

start_index = title_index + len("<title>") # index du titre lui même

end_index = html.find("</title>") # index de la balise fermante

# Extraction du titre
title = html[start_index:end_index]
print(title_index, start_index, end_index, title)