# without_dependency_injection.py
from mail import send_mail

class Mailer: 
  def __init__(self, from_address):
    self.from_address = from_address
    
  def send(self, address, message):
    send_mail(to_address, from_address, message)
    
 ## With 
 
 class Mailer:
  def __init__(self, mail_sender, from_address):
    self.mail_sender = mail_sender
    self.from_address = from_address
    
 def send(self, address, message):
  self.mail_sender.send_mail(to_address, from_address, message)
  
 
 # short
 
 def new_send_mail(to, frm, message):
  pass
  
 from function_dependency_injection import Mailer
 Mailer(new_send_mail, "thomasm1.maestas@gmail.com")
