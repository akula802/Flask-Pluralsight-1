# Core library imports
pass

# 3rd-party imports
from flask import Flask

# Local app imports
pass



# Flask app name is the filename of this file
# flask --app flashcards.py --debug run
app = Flask(__name__)



# Home page
@app.route("/")
def welcome():
    from datetime import datetime
    return "Welcome! Current timestamp: " + str(datetime.now())


# About page
@app.route("/about")
def about():
    return "About"
