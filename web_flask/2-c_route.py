#!/usr/bin/python3
"""starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)

def hello():
    """Start Flask web application"""
    return ('Hello HBNB!')

@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """Adding route /hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)

def cText(text):
    """Dynamic inputed text: replace _ for space and show text"""
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
