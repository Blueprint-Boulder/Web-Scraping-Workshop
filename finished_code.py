import requests
from bs4 import BeautifulSoup

# Step 1: Define URL to scrape and the item you would like to search
URL = 'https://removeandreplace.com/2013/09/24/complete-list-can-recycle/'
ITEM = input("Item to recycle?: ")
print('----------------')

# Step 2: Grab the data with a GET request
r = requests.get(URL)

# Step 3: Parse the HTML using Beautiful Soup
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll('strong')

# Step 4: Filter out items that can be recycled and clean output
recyclable = []
include = False
for item in items:
    if str(item) == '<strong>YOU <span style="text-decoration: underline;">CAN</span> RECYCLE:</strong>':
        include = True
    elif str(item) == '<strong>YOU <span style="text-decoration: underline;">CANNOT</span> RECYCLE:</strong>':
        include = False
    else:
        if include:
            recyclable.append(item.text)

# Step 5: Print out the relevant searched items
for item in recyclable:
    if ITEM in item:
        print(item)