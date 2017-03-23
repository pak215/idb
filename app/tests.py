#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2017
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------
from io import StringIO
from unittest import main, TestCase
from models.py import Restaurants, Locations, Food_types, Reviews, Base
from insert_records.py import init_session, add_restaurant, add_location, add_food_type, add_review

class test_db (TestCase):






# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()