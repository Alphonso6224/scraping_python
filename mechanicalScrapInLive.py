import mechanicalsoup
import time
browser = mechanicalsoup.Browser()

for i in range(4):

    # Connectons nous à notre url
    page = browser.get("http://olympus.realpython.org/dice")

    # Recuperons la balise taguer #result
    tag = page.soup.select("#result")[0]
    result = tag.text

    print(f"The result of  your dice roll is: {result}")
    
    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)