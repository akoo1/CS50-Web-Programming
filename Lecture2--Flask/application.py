
# If you’re on the Anaconda distribution, you should already have flask installed.

# To start up a flask application, run "flask run" in the directory where application.py is located,
# with flask being the web server. Flask will print out the URL the server is running on and where
# the website can be accessed at. If "flask run" produces an error, try running "export FLASK_APP=application.py"
# to make sure it knows to look for application.py as the web server.

# Run "export FLASK_ENV=development" to turn on debug mode
# After running "flask run", your computer is serving the flask application, and it's runnign it on this paticular
# URL http://127.0.0.1:5000/

from flask import Flask   # Import the class `Flask` from the `flask` module, written by someone else.

my_app = Flask(__name__)  # create a new web application object called `my_app`, with `__name__` representing the current file



# A decorator; when the user goes to the route (location)(URL) `/`, exceute the function immediately below
# Defining locations for application to go to, and flask will serve it up, excecute functions accordingly


@my_app.route("/")          # Our default route. The homepage for our flask app
def homepage():
    return "Hello, local world!"


@my_app.route("/hello/alfred")
def hello():
    return "What's up Alfred!"


# Dynamic routes. We want our simple web app to respond to different URLs
@my_app.route("/hello/<your_name>")
def hello_someone(your_name):
    your_name = your_name.capitalize()
    return f"<h1>Hello, {your_name}</h1>"       # You can even add HTML code to the return value
