from twython import Twython
from auth import (consumer_key,consumer_secret,access_token,access_token_secret)

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
message = "Greetings from tmm's Juillet-bot!"
twitter.update_status(status=message)
print("Tweeted: %s" % message)
