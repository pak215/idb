from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
# Model Views

@app.route('/Restaurants')
def Restaurants():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "Gato", "img": "gato.jpg"},\
            {"name" : "Stack Burgerz", "img": "stack.jpg"},\
            {"name" : "Little Italy", "img": "italy.jpg"}
        ])


@app.route('/Locations')
def Locations():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "78701", "img": "temp_image.png"},\
            {"name" : "78702", "img": "temp_image.png"},\
            {"name" : "78703", "img": "temp_image.png"}
        ])


@app.route('/Food_Types')
def Food_types():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "Italian", "img": "temp_image.png"},\
            {"name" : "American", "img": "temp_image.png"},\
            {"name" : "Spanish", "img": "temp_image.png"}
        ])


@app.route('/Reviews')
def Reviews():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "Gato - John", "img": "temp_image.png"},\
            {"name" : "Stack Burgerz - Roney", "img": "temp_image.png"},\
            {"name" : "Little Italy - Tom", "img": "temp_image.png"}
        ])



# Model Elements Views
# the route will be dynamic in the future.
@app.route('/restaurant1')
def restaurant():
    # return render_template(blah)
    return "single Restaurant Instance Page"
