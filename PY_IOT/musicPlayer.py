import sys
import pyperclip
import webbrowser
import requests, bs4

res = requests.get('http://www.thomasmaestas.net/marsreader/index.php')
playFile = open('index.php','r')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    playFile.close()
'''
#downloading web page
def r():
    res = requests.get('https://www.thomasmaestas.net/marsreader/index.php')
    print(type(res))
    res.status_code == requests.codes.ok
    print(len(index.html[:140]))
r()

type(res)
try:
    res.raise_for_status()
except Exception as exc:
    res.status_code == requests.codes.ok
    print(len(res))
# SAVING DOWNLOADED FILES TO PI 

def r():
    res = requests.get('https://www.thomasmaestas.net/marsreader/index.html')
    res.raise_for_status()
    playFile = open('', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.write(chunk)
# Creating BeautifulSoup Object
import requests, bs4
def r():
    res = requests.get('https://www.thomasmaestas.net/marsreader/index.html')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(re.text)
    print(type(noStarchSoup))
def o():
    mars = open('https://www.thomasmaestas.net/marsreader/index.html')
    marsReader = bs4.BeautifulSoup(mars)
    print(type(marsReader))
'''
'''
soup.select('div')
soup.select('#author')
soup.select('.notice')
soup.select('div span')
soup.select('div > span')
soup.select('input[name]')
soup.select('input[type="button"]')
'''

           

 

