# things.py

# Let's get this party started!
import falcon
import json
import logging


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def __init__(self):
        self.logger = logging.getLogger('starts-with.' + __name__);
        self.logger.setLevel(logging.INFO)

    def on_post(self, req, resp):
        reqj = json.loads(req.stream.read().decode('utf-8'))
        try:
            word = reqj['word']
            start = reqj['start']
        except Exception as ex:
            self.logger.error("Body does not conform to API");
            raise falcon.HTTPBadRequest(
                    'Missing Body Params',
                    'You must include a word and start in your body')

        resp.status = falcon.HTTP_200

        body = { "starts-with": word.startswith(start) }
        resp.body = json.dumps(body)

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/', things)
