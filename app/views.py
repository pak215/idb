from flask import render_template, Blueprint, render_template
spoof_db =[
    {"name" : "Little Italy",\
     "img": "italy.jpeg", \
    "last review" : "Excellent Garlic Bread. -Tom", \
    "location" : "1215 S Congress", \
    "zip" : "78701", \
    "price" : "$$", \
    "hours": "11:00am to 11:00pm", \
    "food type": "Italian Food", \
    "rating": "3.4",\
    "img": "italy.jpg",\
    "id" : "1"
    },
    {"name" : "Gato",\
     "img": "gato.jpg", \
    "last review" : "They actually don't serve cat 1/10. -Tom", \
    "location" : "5568 N Lamar Blvd", \
    "zip" : "78702", \
    "price" : "$$$", \
    "hours": "11:00am to 9:00pm", \
    "food type": "Mediterranean Food", \
    "rating": "4",\
    "id" : "2"
    }, 
    {"name" : "Stack Burgers",\
    "img": "stack.jpg", \
    "last review" : "I tried their waffles, not impressed. -Jen", \
    "location" : "1231 Wells Branch Pwy", \
    "zip" : "78703", \
    "price" : "$", \
    "hours": "11:00am to 11:00am", \
    "food type": "American Food", \
    "rating": "5",\
    "id" : "3"
    },
    {"name" : "Biryani Pot",\
    "img": "biryani.jpg", \
    "last review" : "Try their Chicken Dum Biryani! It's absolutely heavenly. -Jeff", \
    "location" : "12407 N Mopac Expy", \
    "zip" : "78704", \
    "price" : "$$", \
    "hours": "11:00am to 10:00am", \
    "food type": "Indian", \
    "rating": "5",\
    "id" : "4"
    },
    {"name" : "Ho Ho Chinese BBQ",\
    "img": "hoho.jpg", \
    "last review" : "I loved their bbq pork fried rice. -Nathan", \
    "location" : "12407 N Mopac Expy", \
    "zip" : "78705", \
    "price" : "$$", \
    "hours": "11:00am to 9:30am", \
    "food type": "Chinese", \
    "rating": "5",\
    "id" : "5"
    }]

Location_db=[
    {"zipcode": "78701",
    "average_price": "$$",
    "popular_food_type": "Italian",
    "highest_rated_restaurant": "Little Italy",
    "Lowest_rated_restaurant": "Little Italia"
    },
    {"zipcode": "78702", 
    "average_price": "$$$",
    "popular_food_type": "Mediterranean",
    "highest_rated_restaurant": "Gato",
    "Lowest_rated_restaurant": "Kitty"
    },
    {"zipcode": "78703", 
    "average_price": "$",
    "popular_food_type": "American",
    "highest_rated_restaurant": "Stack Burgers",
    "Lowest_rated_restaurant": "Piled Sandwiches"
    },
    {"zipcode": "78704", 
    "average_price": "$$",
    "popular_food_type": "Indian",
    "highest_rated_restaurant": "Biryani",
    "Lowest_rated_restaurant": "Mcdonalds"
    },
    {"zipcode": "78705", 
    "average_price": "$",
    "popular_food_type": "Chinese",
    "highest_rated_restaurant": "Ho ho Chinese BBQ",
    "Lowest_rated_restaurant": "Panda Express"
    }]
food_type_db=[
    {"food type": "Chinese",
     "average price": "$",
     "average rating": "3",
     "highest_rated_restaurant": "Ho Ho chinese BBQ",
     "best_location": "78705"
    },
    {"food type": "Mediterranean",
     "average price": "$$$",
     "average rating": "4.2",
     "highest_rated_restaurant": "Gato",
     "best_location": "78702"
     },
    {"food type": "Italian",
     "average price": "$$$",
     "average rating": "4.8",
     "highest_rated_restaurant": "Little Italy",
     "best_location": "78701"
     },
    {"food type": "Indian",
     "average price": "$$",
     "average rating": "3.8",
     "highest_rated_restaurant": "Biryani",
     "best_location": "78704"
     },
    {"food type": "American",
     "average price": "$",
     "average rating": "3.1",
     "highest_rated_restaurant": "Stack Burgers",
     "best_location": "78703"
     },
]
review_db =[
    {"review id": "1",
     "date": "1/10/2014",
     "rating": "4",
     "username": "Federico",
     "restaurant id": "1"
    },
    {"review id": "2",
     "date": "2/11/2015",
     "rating": "3",
     "username": "Chuck",
     "restaurant id": "2"
     },
    {"review id": "3",
     "date": "1/4/2017",
     "rating": "5",
     "username": "Gabriel",
     "restaurant id": "3"
     },
    {"review id": "4",
     "date": "1/10/2017",
     "rating": "4",
     "username": "Dominique",
     "restaurant id": "4"
     },
    {"review id": "5",
     "date": "1/11/2004",
     "rating": "4",
     "username": "Maggie",
     "restaurant id": "5"
     }]

views = Blueprint('views', __name__)

# Splash Screen
@views.route('/')
@views.route('/index')
def index():
    return render_template("index.html")
# Model Views
@views.route('/Restaurants')
def Restaurants():
    global spoof_db
    return render_template("restaurants.html", model_elements = spoof_db)

@views.route('/Locations')
def Locations():
    return render_template(
        "locations.html", model_elements = location_db)

@views.route('/Food_Types')
def Food_types():
    return render_template(
        "foodtype.html",\
        model_elements = [
            {"type" : "Italian", "img": "temp_image.png"},\
            {"type" : "American", "img": "temp_image.png"},\
            {"type" : "Spanish", "img": "temp_image.png"},\
            {"type" : "Mexican", "img": "temp_image.png"},\
            {"type" : "Greek", "img": "temp_image.png"}
        ])

@views.route('/Reviews')
def Reviews():
    return render_template(
        "reviews.html",\
        model_elements = [
            {"name" : "Gato - John", "img": "temp_image.png"},\
            {"name" : "Stack Burgerz - Roney", "img": "temp_image.png"},\
            {"name" : "Little Italy - Tom", "img": "temp_image.png"}
        ])

@views.route('/About')
def About():
    return render_template("about.html")

# Model Elements Views

# RESTAURANTS

@views.route('/Restaurants/<pk>')
def restaurant(pk):
    global spoof_db
    for d in spoof_db:
        if d["id"] == pk:
            return render_template("restaurant_instance.html",instance=d)

# FOOD TYPES

@views.route('/Restaurants/Type/<pk>')
def restaurantType(pk):
    global spoof_db
    return render_template("food_type_instance.html", model_elements = spoof_db)

# LOCATIONS

@views.route('/Restaurants/Location/<pk>')
def restaurantLocation(pk):
    global location_db
    for d in location_db:
        if d["zip"] == pk:
            return render_template("restaurant_instance.html",instance=d)

# REVIEWS

@views.route('/Restaurants/Review/<pk>')
def restaurantReview(pk):
    global review_db
    for d in location_db:
        if d["review id"] == pk:
            return render_template("restaurant_instance.html",instance=d)

