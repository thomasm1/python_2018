# things.py

# Let's get this party started!
import falcon
import json
import logging


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class PhotosResource(object):
    def __init__(self):
        self.logger = logging.getLogger('starts-with.' + __name__);
        self.logger.setLevel(logging.INFO)

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = "https://www.w3schools.com/howto/img_fjords.jpg"

        
# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
photos = PhotosResource()

# things will handle all requests to the '/things' URL path
app.add_route('/', photos)
