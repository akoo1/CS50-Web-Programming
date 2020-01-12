
# Sessions are how Flask can keep track of data that belongs to a particular user.
# Let’s take a note-taking app, for example. Users should only be able to see their own notes.

# Gives access to a variable called "session" which can be used to keep values that are specific to a particular user
from flask import Flask, render_template, request, session
from flask_session import Session   # an additional extension to sessions which allows them to be stored server-side


my_app = Flask(__name__)

my_app.config["SESSION_PERMANENT"] = False
my_app.config["SESSION_TYPE"] = "filesystem"
Session(my_app)


# notes = []     This global notes variable is no longer neeed

# session is a dictionary that belongs to only one user.
# Every user has a unique session dict, and therefore a unique notes list.
# The advantage here is that this server can have multiple different session going on, so each user is
# independant to each other, we don't have one global notes variable shared among all users.
@my_app.route("/", methods=["GET", "POST"])
def homepage():

    if session.get("notes") == None:     # This will create an empty list the first time someone adds a note
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])
