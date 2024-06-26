#!/usr/bin/python3
"""
This is a simple Flask web application script.
It starts a Flask web app that listens on 0.0.0.0, port 5000.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello():
    """
    This function responds to the '/' route (homepage) and returns 'Hello HBNB!'.
    """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
