
# Variables, Jinja2

# Python variables can be used in HTML templates by passing them in as arguments to render_template.
# These templates are rendered using a separate "templating language" called "Jinja2".

# Jinja2 allows us to use Python like syntax such as variables, conditions, loops in our HTML files.
# SO we are able to dynamically generate different HTML code depending on the values of these variables.

from flask import Flask, render_template

my_app = Flask(__name__)


@my_app.route("/")
def homepage():
    my_headline = "Hello there! This is application3.py"
    return render_template("index3.html", headline=my_headline)

# We are saying, besides returning "index3.html", I also want the variable headline inside "index3.html"
# to be assigned the value of my_headline in this Python file



@my_app.route("/GoodBye")
def bye():
    my_headline = "Good Bye!"
    return render_template("index3.html", headline=my_headline)


if __name__ == '__main__':
    my_app.run(debug=True, use_reloader=True)