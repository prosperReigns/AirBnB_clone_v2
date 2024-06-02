#!/usr/bin/python3
""" a script starts a Flask web application"""

from flask import Flask, render_template
from models import state
from models import storage

app = flask(__name__)


@app.teardown_appcontext(exception)
def close_session():
    storage.close()


@app.route("/states", defaults={"id": 1}, strict_slashes=False)
@app.route("/states/<int:id>", strict_slashes=False)
def show_city(id):
    if id == 1:
        states = storage.all(state)
        return render_template('9-states.html', states=states)
    for state in storage.all(states).value():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
