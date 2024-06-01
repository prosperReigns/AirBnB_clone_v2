#!/usr/bin/python3
""" a script starts a Flask web application"""

from flask import Flask, render_template
from models import state
from models import storage

app = flask(__name__)

@app.teardown_appcontext(exception)
def close_session():
    storage.close()


@app.route("cities_by_states`", strict_slashes=False)
def start_flask_application():
    states = storage.all(state)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
