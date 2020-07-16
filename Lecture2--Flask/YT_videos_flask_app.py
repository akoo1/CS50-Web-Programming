

from flask import Flask
import requests

my_app = Flask(__name__)



# The <iframe> tag embeds another HTML page into the current webpage
@my_app.route('/')
def homepage():
    return """ <h1> This is a Youtube video player </h1>
               <a href="https://youtu.be/YQHsXMglC9A"> </a>
               <iframe src="https://www.youtube.com/embed/kTlv5_Bs8aw" width="650" height="380" frameborder="0" allowfullscreen> <iframe> """



# This view function takes a YouTube video unique ID as part of the path, and embed that video in the webpage
@my_app.route('/video/<vid>')
def video_page(vid):
    url = f"https://youtu.be/{vid}"
    if is_url_valid(url):
        return f""" <h2> 
                    Youtube video link: 
                    <a href="https://youtu.be/{vid}"> {vid} </a>
                    </h2>
                    <iframe src="https://www.youtube.com/embed/{vid}" width="650" height="380" frameborder="0" allowfullscreen> <iframe> """
    else:
        # In a given view function, you can manually specify the status code of the response by return a second value.
        # (note that we don't have to specify 200 for the OK case, because the status code is 200 by default)
        return " <h3> YouTube video DOES NOT exist </h3> ", 404




# This helper function checks if the YouTube URL HTTP response's status code is ok, to know whether a URL exists or not
# The requests module's get function can get the status code of a URL
def is_url_valid(url):
    print('The URL is:', url)
    resp = requests.get(url)
    print('The HTTP status code of this YouTube URL is:', resp.status_code)
    return resp.status_code == 200





if __name__ == '__main__':
    my_app.run(debug=True, use_reloader=True)

