from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

# Extraction du html + decodage
html =  page.read().decode('utf-8')

def findValue(param1, param2):
    start_index = html.find(param1) + len(param1)
    end_index = html.find(param2)
    return html[start_index:end_index]

first = findValue("Name:", "</h2>")
print(first)

second = findValue("Favorite Color:", "</center>")
print(second)
