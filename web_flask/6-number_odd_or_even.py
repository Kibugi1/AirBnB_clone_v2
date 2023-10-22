#!/usr/bin/python3
"""
A flask script that starts a Flask web application
and displays the routes '/' and '/HBNB' '/c/<text>' '/python'
'/python/text' '/number/<int:n>' '/number_template/<int:n>'
'number_odd_or_even/<n>'
"""

from flask import Flask
from flask import render_template


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
@app.route("/python/<string:text>", strict_slashes=False)
def python_route(text="is cool"):
    """displays value of /python/(<text>) web app route"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Function that displays the value of /number/in n"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Function that displays a HTML page if n is int"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Function that displays n if its even or odd"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
