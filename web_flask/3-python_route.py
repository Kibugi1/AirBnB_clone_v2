#!/usr/bin/python3
"""
A flask script that starts a Flask web application
and displays the routes '/' and '/HBNB' '/c/<text>'
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """A function for the web app hbnb route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """a function for the /HBNB web app route display"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Function that displays value of /c/<text> web app route"""
    text = text.replace("_", " ")
    return "C %s" % text

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Function that displays the value of /python/<text> web app route."""
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
