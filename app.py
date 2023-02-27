import os
import logging
from flask import Flask, request, abort, redirect
from flask_redis import FlaskRedis
from hashlib import blake2b

app = Flask(__name__)

REDIS_URL = os.getenv('REDIS_URL')
if REDIS_URL is not None:
    app.config['REDIS_URL'] = REDIS_URL
redis_client = FlaskRedis(app)
redis_client.init_app(app)


@app.route('/urls/', methods=['POST'])
def urls():
    url = request.get_data()
    h = blake2b(digest_size=2)
    h.update(url)
    short_url = h.hexdigest()
    redis_client.set(short_url, url)
    short_url = '{host}{path}\n'.format(host=request.host_url, path=short_url)
    return short_url


@app.route('/<short_url>')
def url(short_url):
    url = redis_client.get(short_url)
    if url is None:
        abort(404)
    return redirect(url, code=302)

