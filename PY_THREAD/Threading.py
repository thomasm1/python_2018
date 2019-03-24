// python 3.6 



import queue
import threading
from urllib.request import urlopen

# called by each thread
def get_url(q, url):
    q.put(urlopen(url).read())

theurls = ["http://google.com", "http://yahoo.com"]

q = queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

s = q.get()
print(s)
