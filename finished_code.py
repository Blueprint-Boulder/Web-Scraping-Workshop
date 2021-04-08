import requests
from bs4 import BeautifulSoup

# Part A: Define URL to scrape and the item you would like to search
URL = 'https://removeandreplace.com/2013/09/24/complete-list-can-recycle/'
ITEM = input("Item to recycle?: ")

# Part B: Grab the data with a GET request
r = requests.get(URL)

# Part C: Parse the HTML using Beautiful Soup
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll('strong')

# Part D: Filter out items that can be recycled and clean output
recyclable = []
include = False
for item in items:
    val = item.text                     # Extract text from the HTML tag
    if val == 'YOU CAN RECYCLE:':       # Include items following this tag
        include = True
    elif val == 'YOU CANNOT RECYCLE:':  # Stop including items when you encounter this tag
        include = False
    else:
        if include:
            recyclable.append(val)

# Part E: Print out the relevant searched items
print('----------------')
for item in recyclable:
    if ITEM in item:
        print('> ' + item)
print('----------------')
print('-End of Results-')