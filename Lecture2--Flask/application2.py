
# The "render_template" function from flask

# To separate the HTML code (the View) from our logic code (the Controller) in our flask application, we use "render_template".


# index2.html and any other HTML template files NEED be stored in a directory named "templates"
# when using render_template, flask will only look for HTML templates inside the the directory called "templates"

from flask import Flask, render_template

my_app = Flask(__name__)



@my_app.route("/")
def homepage():
    return render_template("index2.html")




if __name__ == "__main__":
    my_app.run(debug=True, use_reloader=True)
