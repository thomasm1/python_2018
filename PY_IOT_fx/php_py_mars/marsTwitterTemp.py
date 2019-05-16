from twython import Twython
from auth import (consumer_key,consumer_secret,access_token,access_token_secret)
twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)



# NASA API for data.input
marsTemp = "<data.input>"

message = "Greetings from tmm! The temp on Mars today is " + marsTemp
twitter.update_status(status=message)
print("Tweeted: %s" % message)


