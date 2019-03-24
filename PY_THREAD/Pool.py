# Parallel versions of the map function are provided by two libraries:
# multiprocessing, and  ...
# little known step child: multiprocessing.dummy.

from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]

# make the Pool of workers
pool = ThreadPool(4) 

# open the urls in their own threads
# and return the results
results = pool.map(urlopen, urls)

# close the pool and wait for the work to finish 
pool.close() 
pool.join() 

## ~ TIMING RESULTS::
"""
Single thread:   14.4 seconds
       4 Pool:   3.1 seconds
       8 Pool:   1.4 seconds
      13 Pool:   1.3 seconds
"""
############################# multiple args #######
# results = pool.starmap(function, zip(list_a, list_b))
# results = pool.starmap(function, zip(itertools.repeat(constant), list_a))
