from flask import render_template, Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index')
def index():
    return render_template("index.html")
# Model Views

@views.route('/Restaurants')
def Restaurants():
    return render_template(
        "restaurants.html",\
        model_elements = [
            {"name" : "Gato", "img": "gato.jpg"},\
            {"name" : "Stack Burgerz", "img": "stack.jpg"},\
            {"name" : "Little Italy", "img": "italy.jpg"}
        ])


@views.route('/Locations')
def Locations():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "78701", "img": "temp_image.png"},\
            {"name" : "78702", "img": "temp_image.png"},\
            {"name" : "78703", "img": "temp_image.png"}
        ])


@views.route('/Food_Types')
def Food_types():
    return render_template(
        "grid.html",\
        model_elements = [
            {"name" : "Italian", "img": "temp_image.png"},\
            {"name" : "American", "img": "temp_image.png"},\
            {"name" : "Spanish", "img": "temp_image.png"}
        ])


@views.route('/Reviews')
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
@views.route('/Little_Italy')
def restaurant():
    return render_template(
	"restaurant_instance.html", \
        instance = 
            {"name" : "Little Italy", "img": "italy.jpeg", \
	    "last review" : "Excellent Garlic Bread", \
	    "location" : "1215 S Congress", \
	    "zip" : "78701", \
	    "price" : "$$", \
	    "hours": "11:00am to 11:00pm", \
	    "food type": "Italian Food", \
	    "rating": "4.5"}
	)
