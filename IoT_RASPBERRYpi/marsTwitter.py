from twython import Twython
from auth import (consumer_key,consumer_secret,access_token,access_token_secret)

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

marsTemp = '''<Big, beautiful spiral galaxy NGC 1055 is a dominant member of a small galaxy
group a mere 60 million light-years away toward the aquatically intimidating constellation Cetus.>'''

message = 'Greetings from tom and louis' + marsTemp
twitter.update_status(status=message)
print("Tweeted: %s" % message)


