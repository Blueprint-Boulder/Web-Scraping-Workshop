import requests
from bs4 import BeautifulSoup

URL = 'https://removeandreplace.com/2013/09/24/complete-list-can-recycle/'
ITEM = 'box'

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('strong')

formatted_links = []

include = False
for link in links:

    if str(link) == '<strong>YOU <span style="text-decoration: underline;">CAN</span> RECYCLE:</strong>':
        include = True
    elif str(link) == '<strong>YOU <span style="text-decoration: underline;">CANNOT</span> RECYCLE:</strong>':
        include = False
    else:
        if include:
            formatted_links.append(link.text)

# Print findings
print("Results for: " + ITEM)
for item in formatted_links:
    if ITEM in item:
        print(item)


# NOTE: this is nowhere near comprehensive. This is where finding more sites to scrape would be useful! 
# Because then we could get an aggregate. But that's for next time. :)