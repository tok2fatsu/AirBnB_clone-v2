#!/usr/bin/python3
"""Starts Flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hbnb_route():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run()
