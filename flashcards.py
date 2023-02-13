# Core library imports
from datetime import datetime

# 3rd-party imports
from flask import Flask, render_template

# Local app imports
from model import db



# Flask app name is the filename of this file
# flask --app flashcards.py --debug run
app = Flask(__name__)



# Home page
@app.route("/")
def welcome():
    hello_world_string = "Welcome! Current timestamp: " + str(datetime.now())
    #return hello_world_string
    return render_template(
        "welcome.html",
        message=hello_world_string,
    )
    


# About page
@app.route("/about")
def about():
    return "About"



# View to explore the model layer
@app.route("/card")
def view_card():
    card = db[1]
    return render_template(
        "view_card.html",
        card=card,
    )
