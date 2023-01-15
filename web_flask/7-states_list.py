#!/usr/bin/python3
"""Starts a Flask web app
"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Lists states
    Returns:
        string: simple message
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=list(states))


@app.teardown_appcontext
def teardown(self):
    """ Cleanup Db Session"""
    storage.close()


if __name__ == "__main__":
    storage.reload()
    app.run()
