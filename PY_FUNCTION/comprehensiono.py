values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]

values = [x / (x - y) 
          for x in range(100) 
          if x > 50 
          for y in range(100) 
          if x - y != 0]

values = []
for x in range(100):
    if x > 50:
        for y in range(100):
            if x - y != 0:
                values.append(x / (x - y))
# 

[(x, y) for x in range(10) for y in range(x)]

result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))   
#

vals = [[y * 3 for y in range(x] for x in range(10)]

outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)

print(outer) 
#

{x * y for x in range(10) for y in range(10)}
#{0,1,2,3,...
g = ((x, y) for x in range(10) for y in range(x))
type(g)
# <class 'generator'>
list(g)
#[(1,0), (2.0), (2.1), (3,0 ...
    
# map()
map(ord, 'The quick brown fox') # ord->fx, str->input sequence

## TRACE ## 
# tracer.py
class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:    
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap
  #repl
  from tracer import Trace
  result = map(Trace()(ord), 'The quick brown fox')
    
    
