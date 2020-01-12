
# The way to use a separate HTML file in our flask application

# index2.html and any other HTML template files NEED be stored in a directory named "templates"
# When using render_template, flask will only look for HTML files inside the the directory called "templates"

from flask import Flask, render_template

my_app = Flask(__name__)



@my_app.route("/")
def homepage():
    return render_template("index2.html")
