#!/usr/bin/python3
“””Starts Flask web app
    / - display “Hello HBNB!”
    /hbnb – display “HBNB”
    /c/<text> - display “C <text>”
“””
From flask import Flask

App = Flask(__name__)


@app.route(‘/’, strict_slashes=False)
Def hbnb_route():
    “””display Hello HBNB”””
    Return “Hello HBNB!”


@app.route(‘/hbnb’, strict_slashes=False)
Def hbnb():
    “””display HBNB”””
    Return “HBNB”


@app.route(‘/c/<string:text>’, strict_slashes=False)
Def c_text(text):
    “””display C followed by <text> content”””
    Text = text.replace(“_”, “ “)
    Return “C %s” % text


If __name__ == “__main__”:
    App.run(host=”0.0.0.0”)
