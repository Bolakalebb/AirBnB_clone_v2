#!/usr/bin/python3
"""
    Script that starts a Flask web application
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """
        Teardown SQLAlchemy Session
    """
    storage.close()
    
    
@app.route('/states', strict_slashes=False)
def states():
    """
        Display a HTML page with a list of all State objects sorted by name (A->Z)
    """
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """
        Display a HTML page with a list of City objects linked to a State object
    """
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', state=None)

    cities = state.cities if type(storage).__name__ == "DBStorage" else state.cities
    cities_sorted = sorted(cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
