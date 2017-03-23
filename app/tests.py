#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------
# imports
# -------
from io import StringIO
from unittest import main, TestCase
from models import Restaurants, Locations, Food_types, Reviews
from insert_records import init_session, add_restaurant, add_location, add_food_type, add_review

session_token = init_session()

class test_db (TestCase):

    global session_token

    def test_1_restaurant_addition(self):
        add_restaurant(session_token,
                       name = "Little Italy",
                       location = 78701,
                       price = "$$",
                       rating = "3",
                       hours = "9 to 5",
                       food_type = "Italian",
                       recent_review = "1")
        assert not (session_token.query(Restaurants), None)




# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()