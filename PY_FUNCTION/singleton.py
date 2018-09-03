# singleton.py

class _Singleton_:
  def __init__(self):
    self.some_data = 12
    
instance = None 

def get_instance():
  global instance 
  if instance is None:
    instance = _Singleton_()
  return instance
  
 ## singleton_alter.py
 
 class Singleton:
  def __init__(self):
    self.some_data = 12
  
  instance = Singleton()
  del Singleton # No new instance
  
  ## >> import singleton
  ## >> singleton.instance.som_data
  12
  
  
