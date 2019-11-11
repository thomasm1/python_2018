## Thoams Maestas
## 9-20-2018
## Protocol: http:, https:
## Host: 184.168.159.12 thomasmaestas.net
## Port: http=80, https=443
## Path: wiki/URL
## Querystring: key=vie&life=42
## Fragment: dataScraper.py

## request: open URLS
## response: 
## error: request exceptions
## parse: useful URL functions
## robotparser: robots.txt files

# 1
import urllib
dir(urllib)
## 'error', 'parse', 'request', 'response'

# 2 
from urllib import request
Files: open(file)
URLS: urlopen(url)
## 'urlopen'
type(resp)
##<class 'http.client.HTTPResponse'>
dir(resp)
resp.code
# 200 ok, 403 forbidden, 404 loco perdido, 402

resp = request.urlopen("ourdailytech.net")
type(resp)
resp.length

resp.peek()
#b'<!DOCTYPE html>\n<title> ...
data = resp.read()
type(data)
#<class 'bytes'>

len(data)
#3344

html = data.decode("UTF-8")
resp.read()
#b''

resp = request.urlopen("https://www.google.com/search?q=socratica")
# https://www.youtube.com/watch?v=EuC-yVzt=ddd
qs = "v=" + "Edklsje " + "&" + "t=" + "ddd"

from urllib import parse

