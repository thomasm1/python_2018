import sys
import pyperclip
import webbrowser
import requests, bs4

marsReader = requests.get('http://www.thomasmaestas.net/marsreader/index.php')
marsSoup = bs4.BeautifulSoup(marsReader.text, 'html.parser')
print(len(marsSoup))

#marsReader = open('http://www.thomasmaestas.net/marsreader/index.php')

#mmarsSoup = bs4.BeautifulSoup(marsReader, )
#print(marsSoup)
explanation = marsSoup.select('#returnObject')
print(len(explanation))
print(explanation)



'''
soup.select('div')
soup.select('#author')
soup.select('.notice')
soup.select('div span')
soup.select('div > span')
soup.select('input[name]')
soup.select('input[type="button"]')
'''


#downloading web page
'''def r():
    res = requests.get('https://www.thomasmaestas.net/marsreader/index.html')
    print(type(res))
    res.status_code == requests.codes.ok
    print(len(index.html[:140]))
#
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
    print(type(marsReader))'''
'''
soup.select('div')
soup.select('#author')
soup.select('.notice')
soup.select('div span')
soup.select('div > span')
soup.select('input[name]')
soup.select('input[type="button"]')
'''

           

 

