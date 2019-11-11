from urllib import parse
dir(parse)
# 'urlencode'

params = {"v": "Eerjp","t": "4m33s"}
querystring = parse.urlencode(params)
querystring
#'v=dkfj#t=4m33s'
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
resp.isclosed()
#False
resp.code
html = resp.read().decode("utf-8")
html[:500]
'<!DOCTYPE ...

