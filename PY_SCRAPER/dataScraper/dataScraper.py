import requests
from bs4 import BeautifulSoup

print('bs4 loaded')
# get the data
# data = requests.get('https://thomasmaestas.net')
data = requests.get('https://www.wired.com')
#print(data.text)

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

root = soup.find('div', { 'id': 'app-root' })
# print(root)
section = root.find('a')
print(section)

for section in root.find_all('itemProp="href"'):
    place = section.find_all('itemProp="href"')[0].text.strip()
    username = place.find_all('itemProp="href"')[0].text.strip()
    print(place)
    print(username)
