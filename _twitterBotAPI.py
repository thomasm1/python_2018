
##
#Twitter API  -setting up twitter tweeting-bot API
'''
sudo apt-get update
sudo apt-get upgrade
sudo pip3 install twython
# TWITTER Access Token, Access Token Secret
sudo date -s "1 MAY 2016 12:00:00"
'''
# auth.py #
consumer_key = 'ABCDEFGHIJKLKMNOPQRSTUVWXYZ'
consumer_secret = '1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ'
access_token = 'ZYXWVUTSRQPONMLKJIHFEDCBA'
access_token_secret = '0987654321ZYXWVUTSRQPONMLKJIHFEDCBA'
# twitter.py #
from twython import Twython
from auth import (
consumer_key,
consumer_secret,
access_token,
access_token_secret
)
## Twitter API Keys:
twitter = Twython(
consumer_key,
consumer_secret,
access_token,
access_token_secret
)
message = "Hello world!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
# random
import random
messages = [
"Hello world",
"Hi there",
"What's up?",
"How's it going?",
"Have you been here before?",
"Get a hair cut!",
]
message = random.choice(messages)
# picture
message = "Hello world - here's a picture!"
with open('/home/pi/Downloads/image.jpg', 'rb') as photo:
twitter.update_status_with_media(status=message, media=photo)
 # Twython Streamer
# stream.py #
from twython import TwythonStreamer
from auth import (
consumer_key,
consumer_secret,
access_token,
access_token_secret
) 
'''
The original TwythonStreamer class has a method (function) called on_success . This is the
code which is run when a matching tweet is found. A simple example is to just print out the
contents of a tweet found when we search the stream:
'''  
class MyStreamer(TwythonStreamer):
def on_success(self, data):
	if 'text' in data:
		print(data['text'])
#
stream = MyStreamer(
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret
)
stream.statuses.flter(track='raspberry pi')
#
