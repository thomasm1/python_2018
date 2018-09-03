import sys
import pyperclip
import webbrowser.sys 

def comm(sa):
    if len(sys.argv)>1:
        address = ''.join(sys.argv[1:])
    else:
        address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)
    print('...window opening!')
comm('2300 Calle de Real, Albuquerque, NM 87104')
#pip install requests
import requests
res = requests.get('https://www.google.com/maps/place/')

#downloading web page
def r():
    res = requests.get('https://www.thomasmaestas.net/_For_Cat_Eyes_Only_/index.html')
    print(type(res))
    res.status_code == requests.codes.ok
    print(len(index.html[:250]))
#
type(res)
try:
    res.raise_for_status()
except Exception as exc:
    res.status_code == requests.codes.ok
    print(len(res))
# SAVING DOWNLOADED FILES TO HD
import requests
def r():
    res = requests.get('https://www.thomasmaestas.net/_For_Cat_Eyes_Only_/index.html')
    res.raise_for_status()
    playFile = open('', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.write(chunk)
# Creating BeautifulSoup Object
import requests,bs4
def r():
    res = requests.get('http://www.wired.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(re.text)
    print(type(noStarchSoup))
def o():
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile)
    print(type(exampleSoup))
'''
soup.select('div')
soup.select('#author')
soup.select('.notice')
soup.select('div span')
soup.select('div > span')
soup.select('input[name]')
soup.select('input[type="button"]')
'''



                       

 
