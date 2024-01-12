import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# Definition d'un pattern = "<title.*?>.*?</title.*>"
pattern = "<title.*?>.*?</title.*>"

match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()

print(title)
title = re.sub("<.*?>", "", title) # Remove html tags
print(title)

test = re.findall("ab*c", "ac")
print(re.findall("ab*c", "Abc", re.IGNORECASE))