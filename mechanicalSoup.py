import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

# Obtention de chaque lien de la page
links = profiles_page.soup.select('a')
# Parcourons chaque lien et recupérons le href attribut
baseUrl = "http://olympus.realpython.org"
for link in links:
    address = baseUrl + link["href"]
    text = link.text
    print(f"{text}: {address}")   
