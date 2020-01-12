
# URLs

from flask import Flask, render_template

my_app = Flask(__name__)

@my_app.route("/")
def homepage():
    return render_template("index.html")


@my_app.route("/more")
def more():
    return render_template("more.html")
