#!/usr/bin/python3
"""Starts Flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hbnb_route():
    return "Hello HBNB"


@app.route('/', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()

