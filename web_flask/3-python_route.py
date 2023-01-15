#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hbnb_route():
    """prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints Python is cool"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
