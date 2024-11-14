from flask import Flask

from flask_svelte import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", name="Flask Svelte")

@app.route("/lang")
def lang():
    return render_template("index.html", name="Flask Svelte")