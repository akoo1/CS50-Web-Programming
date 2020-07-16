
# To start a flask application, just run "python application.py" like you would to run any other python scripts.
# But unlike your typical Python script, this script, thanks to the Flask library, will start a local webserver.
# with the following message in the terminal,
#   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

# Now your computer is serving (hosting) the flask application on this particular URL
# http://127.0.0.1:5000/
# (127.0.0.1 always refers to your own machine)

# Whenever someone (a web browser) visits the homepage, the following message is the response by your web server,
# 127.0.0.1 - - [14/Jul/2020 01:06:56] "GET / HTTP/1.1" 200 -

# Whenever someone (a web browser) tries to visits a web page that doesn't exist,
# 127.0.0.1 - - [14/Jul/2020 01:09:08] "GET /wtf HTTP/1.1" 404 -

# This web app will run forever until you shut down your computer or use "ctrl + c" to shut down the web server

from flask import Flask   # Import the class `Flask` from the `flask` module

my_app = Flask(__name__)  # create a new web application object called `my_app`, with `__name__` representing the current file


# The decorator function @app.route() will "decorate" the view function that comes after it.
# (but that's kind of beyond the scope for now)

# The my_app object's route method defines what URL the application should respond to
# And when the specified URL is visited by a browser, the view function will execute and display content to the user.
# (It doesn't matter what we name the view functions)

@my_app.route("/")          # The default route, which is the homepage (index.html) of our flask app
def homepage():
    return " Hello, local world! "



@my_app.route("/hello/Alfred")
def hello_page():
    return """ 
            <h1> What's up Alfred! </h1>  
            <p> Here comes an image: </p> 
            <img src=http://stash.compjour.org/assets/images/sunset.jpg> """


# Dynamic routes => Creating routes with variables in the path name
# We want our simple web app to respond to any URLs dynamically under the the same domain http://127.0.0.1:5000/
# Based on the variable in the path, we then pass the variable as an argument to the function.
@my_app.route("/<your_name>")
def hello_someone_page(your_name):
    your_name = your_name.capitalize()
    return f"<h1> Hello, {your_name} </h1>"     # Functions in flask can return HTML code
                                                  # This way we can style the words, instead of just using regular python strings


# This will run the flask app when we run this file --> python application.py
if __name__ == "__main__":
    my_app.run(debug=True, use_reloader=True)

# Setting the run method's parameter debug=True, will allow the flask app to display error messages in the web browser
# Setting the run method's parameter use_reloader=True, will make the flask app restart itself when it detects a code change




#####################################################################################################################
# If you’re on the Anaconda distribution, you should already have flask installed.

# To start up a flask application in the terminal, run "flask run" in the directory
# where application.py is located, with flask being the web server. Flask will print
# out the URL the server is running on, which is where the website can be accessed at.

# Run "export FLASK_ENV=development" to turn on debug mode

# If "flask run" produces an error, try running "export FLASK_APP=application.py" to make sure it
# knows to look for application.py as the web server.
