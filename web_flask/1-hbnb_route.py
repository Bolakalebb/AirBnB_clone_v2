#!/usr/bin/python
"""starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello():
    """prints Hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """add a specific route /hbnb"""
    return "HBNB"

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)
