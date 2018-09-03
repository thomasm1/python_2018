from flask import Flask, render_template, url_for, request, Response, jsonify
from flask_redis import FlaskRedis
from random import randint
import requests
import json
import logging

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://redis:6379/0'

redis = FlaskRedis(app)

EMOJI_LIST = ["ಠ_ಠ", "(╯°□°）╯︵ ┻━┻", "(´・ω・｀)", "ᕕ( ᐛ )ᕗ", "ʕ •ᴥ•ʔ", "▼・ᴥ・▼"]


logger = logging.getLogger('emoji-engine.' + __name__)

@app.route('/')
def index():
    js_url = url_for('static', filename='script.js')
    emoji = EMOJI_LIST[randint(0, len(EMOJI_LIST) - 1)]
    counter = str(redis.incr('web2_counter'))

    return render_template('index.html', emoji=emoji, js_url=js_url, counter=counter)

@app.route('/starts-with', methods=['POST'])
def starts_with():
    req_data = request.get_json()
    logger.error(req_data['word'])
    r = requests.post('http://starts-with:8000', json=req_data)

    js = jsonify(r.json())
    return js 

@app.route('/photo-hub', methods=['GET'])
def photo_hub():
    r = requests.get('http://photo-hub:8000');

    js = jsonify({
        "photo": r.text
    })


    return js 
