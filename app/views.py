from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Splash Screen"


@app.route('/Restaurants')
def Restaurants():
    # return render_template(blah)
    return "Restaurants Table Page"

# the route will be dynamic in the future.
@app.route('/restaurant1')
def restaurant():
    # return render_template(blah)
    return "single Restaurant Instance Page"
