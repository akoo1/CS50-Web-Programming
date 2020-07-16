
# With Flask and Jinja2, the results from HTML forms can now be actually stored and used.

from flask import Flask, render_template, request



my_app = Flask(__name__)


@my_app.route("/")
def homepage():
    return render_template("index.html")



@my_app.route("/hello", methods=["POST"])
def greet():
    # we are gonna get the value of name from the form tag, and assign it to the variable user_name
    user_name = request.form.get("name")
    # And then we pass that name into the "hello.html" file
    return render_template("hello.html", name=user_name)




if __name__ == '__main__':
    my_app.run(debug=True, use_reloader=True)