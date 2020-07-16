
# Loops

from flask import Flask, render_template

my_app = Flask(__name__)


@my_app.route("/")
def homepage():
    name_list = ["Alice", "Bob", "Charlie", "David"]
    return render_template("index5.html", name_list=name_list)






if __name__ == '__main__':
    my_app.run(debug=True, use_reloader=True)
