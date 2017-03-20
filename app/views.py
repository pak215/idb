from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/restaurants')
def Restaurants():
    return render_template("grid.html", restaurants = [{"name" : "Gato", "img": "gato.jpg"}, {"name" : "Stack Burgerz", "img": "stack.jpg"}, {"name" : "Little Italy", "img": "italy.jpg"}])

# the route will be dynamic in the future.
@app.route('/restaurant1')
def restaurant():
    # return render_template(blah)
    return "single Restaurant Instance Page"
