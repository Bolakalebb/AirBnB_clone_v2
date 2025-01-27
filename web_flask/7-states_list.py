#!/usr/bin/python3
"""Import flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
  """Render 7-state_list.html page to display States created"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
