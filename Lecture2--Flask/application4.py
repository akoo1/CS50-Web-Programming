
# if/else

import datetime
from flask import Flask, render_template

my_app = Flask(__name__)


@my_app.route("/")
def homepage():
    curr_date = datetime.datetime.now()

    is_new_year = False
    if curr_date.month == 1 and curr_date.day == 1:
        is_new_year = True

    #is_new_year = True

    return render_template("index4.html", new_year=is_new_year)




if __name__ == '__main__':
    my_app.run(debug=True, use_reloader=True)
