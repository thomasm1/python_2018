class Range:
  def __init__(self, a, end=None, step=None):
    self.start = 0 if end is None else a
    self.end = a if end is None else a
    self.step = 1 if step is None else step
    
  def __iter__(self):
    return RangeIterator(self)
 
 
 ## 
 
 class RangeIterator:
  def __init__(self, range):
    self.range = range
    self.current = self.range.start
    
  def __next__(self):
    if not self.has_next():
      raise StopIteration
    
    next = self.current
    self.current += self.range.step
    return next
    
  def has_next(self):
     return self.current < self.range.end
  
  
  ## 
  i = Range(10).__iter__()
  while i.has_next():
    print(i.next())
  
  
 ## 
 i = iter(Range(10))
 while True:
  try:
    print(i.next())
  except StopIteration:
    break
  
 for i in Range(10):
  print(i)
  
   
