# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org"
page = urlopen(url + "/profiles")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())
test = soup.find_all("a")
print(test)
for i in test:
    print(url + i["href"])