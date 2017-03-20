import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurants(Base):
    __tablename__ = 'restaurants'

    # columns
    # We need a surrogate key because name is not a unique key
    # and location is not convenient for a unique key
    # location and name could be a primary key.

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    price  = Column(Integer, nullable=False)
    rating  = Column(Integer, nullable=False)
    hours = Column(String(250), nullable=False)

    food_type = Column(String(250), ForeignKey('food_types.food_type'))
    # connects to Food_types
    food_type = relationship("Food_types")

    Recent_Review = Column(String(250), ForeignKey('reviews.review_id'))
    # Connects to Reviews
    review = relationship("Reviews")

    #url to images? image id's on a folder perhaps, tbd
    #images = Column(String(250), nullable=False)

class Locations(Base):
    __tablename__ = 'locations'

    # columns
    # a location object (row) on this table, will be a zipcode
    zipcode = Column(Integer, primary_key=True)
    # overall average cost for that area's restaurants
    average_price  = Column(Integer, nullable=False)
    # most common food type found in area

    popular_food_type  = Column(String(250), ForeignKey('food_types.food_type'))
    # connects to Food_types
    food_type = relationship("Food_types")

    # can't use name to identify single restaurant
    highest_rated_restaurant = Column(Integer, ForeignKey('restaurants.id'))
    lowest_rated_restaurant = Column(Integer, ForeignKey('restaurants.id'))
    # connects to Restaurants
    restaurant = relationship("Restaurants")

    # why don't we have an average restaurant rating per zip??

class Food_types(Base):
    __tablename__ = 'food_types'

    food_type = Column(String(250), primary_key=True)
    average_price  = Column(Integer, nullable=False)
    average_rating  = Column(Integer, nullable=False)

    highest_rated_restaurant = Column(Integer, ForeignKey('restaurants.id'))
    # connects to Restaurants
    restaurant = relationship("Restaurants")

    best_location = Column(Integer, ForeignKey('locations.zipcode'))
    # connects to Locations
    location = relationship("Locations")

class Reviews(Base):
    __tablename__ = 'reviews'

    # Unless we have both a name and a time of publication (to the minute) 
    # we have to use another surrogate key
    review_id = Column(Integer, primary_key=True)
    date = Column(String(250), nullable = False)
    rating = Column(Integer, nullable = False)
    username = Column(String(250), nullable = False)

    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    # connects to Restaurants
    restaurant = relationship("Restaurants")

    zipcode = Column(Integer, nullable = False)
    # connects to Locations
    location = relationship("Locations")

# create an engine that stores data in the local directory's db file
absolute_path = 'sqlite:////home/pablo/git/idb/'
db_name = 'alchemy_test_1'
engine = create_engine(absolute_path + db_name)

# Create all tables in the engine. Equivalent to Create Table in sql
Base.metadata.create_all(engine)
