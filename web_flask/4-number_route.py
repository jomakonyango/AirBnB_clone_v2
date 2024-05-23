#!/usr/bin/python3
"""
This is a simple Flask web application script.
It starts a Flask web app that listens on 0.0.0.0, port 5000.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function responds to the '/' route (homepage) and returns 'Hello HBNB!'.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function responds to the '/hbnb' route and returns 'HBNB'.
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function responds to the '/c/<text>' route and returns 'C ' followed by the value of the text variable.
    """
    return 'C %s' % text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    This function responds to the '/python/<text>' route and returns 'Python ' followed by the value of the text variable.
    """
    return 'Python %s' % text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    This function responds to the '/number/<n>' route and returns 'n is a number' only if n is an integer.
    """
    return '%d is a number' % n

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
