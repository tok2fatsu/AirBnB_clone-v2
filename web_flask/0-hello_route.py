#!/usr/bin/python3
"""Starts Flask web-app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_route():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
