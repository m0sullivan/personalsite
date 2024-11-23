from flask import Flask, send_from_directory

from flask_svelte import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="Flask Svelte")

@app.route("/public/<path:path>")
def home(path):
    return send_from_directory('public', path)