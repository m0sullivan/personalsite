from flask import Flask, send_from_directory
from gevent.pywsgi import WSGIServer

from flask_svelte import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="Flask Svelte")

@app.route("/public/<path:path>")
def home(path):
    return send_from_directory('public', path)

if __name__ == '__main__':
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()