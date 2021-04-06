import requests
from bs4 import BeautifulSoup

URL = 'http://michelletran.me'

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('div', class_='square')

formatted_links = []

print(links) # just contains the elements that meet findAll criteria

for link in links:
	data = {
		'class': link['class'],
	}
	formatted_links.append(data)

print(formatted_links)