import requests
from bs4 import BeautifulSoup

# get the data
##data = requests.get('https://thomasmaestas.net')
data = requests.get('https://www.wired.com')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

root = soup.find('div', { 'id': 'app-root' })
section = root.find('div')

for section in root.find_all('itemProp="author"'):
    place = section.find_all('itemProp="author"')[0].text.strip()
    username = place.find_all('itemProp="author"')[0].text.strip()
    print(place)
    print(username)

    
