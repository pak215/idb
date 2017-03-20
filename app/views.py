from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", restaurants = [{"name" : "test1"}, {"name" : "test2"}, {"name" : "test3"}])


@app.route('/Restaurants')
def Restaurants():
    # return render_template(blah)
    return "Restaurants Table Page"

# the route will be dynamic in the future.
@app.route('/restaurant1')
def restaurant():
    # return render_template(blah)
    return "single Restaurant Instance Page"
