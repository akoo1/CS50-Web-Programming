
# An "API key" is a unique string that belongs to a specific project, and is used to request access to an API (Google map in this case), so the company knows
# who is requesting access to the platform, and that person has permission to do so.

# My API key for this project on Google: key=AIzaSyBO9nhKgdrp0DGivjtPwfVDOJSPxk2QpI8

from flask import Flask

my_app = Flask(__name__)


@my_app.route('/')
def homepage():
    return "This is a Google Map flask app"



@my_app.route('/smu')
def smu_page():
    return """ <h1> Hello, SMU </h1>
               <img src="https://maps.googleapis.com/maps/api/staticmap?size=700x400&zoom=15&markers=smu&key=AIzaSyBO9nhKgdrp0DGivjtPwfVDOJSPxk2QpI8">
               <img src="https://maps.googleapis.com/maps/api/streetview?size=700x400&location=Southern+Methodist+University+library&key=AIzaSyBO9nhKgdrp0DGivjtPwfVDOJSPxk2QpI8"> """

# 3 "request parameters" are passed into this URL/API_call to...
# - size, markers, key (Google Static Map API)
# - size, location, key (Google Static Street View API)

# And it will return a map image with a marker placed at the location entered.
# In a URL, all parameters are separated by the ampersand (&) character.



@my_app.route('/<location>')
def anywhere_page(location):
    return f""" <h1> Hello, {location} </h1>
               <img src=https://maps.googleapis.com/maps/api/staticmap?size=700x400&zoom=15&markers={location}&key=AIzaSyBO9nhKgdrp0DGivjtPwfVDOJSPxk2QpI8>
               <img src=https://maps.googleapis.com/maps/api/streetview?size=700x400&location={location}&key=AIzaSyBO9nhKgdrp0DGivjtPwfVDOJSPxk2QpI8> """






if __name__ == '__main__':
    my_app.run(debug=True, use_reloader=True)


