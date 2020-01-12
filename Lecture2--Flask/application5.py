
# Loops

from flask import Flask, render_template

my_app = Flask(__name__)


@my_app.route("/")
def homepage():
    names = ["Alice", "Bob", "Charlie", "David"]
    return render_template("index5.html", names=names)
