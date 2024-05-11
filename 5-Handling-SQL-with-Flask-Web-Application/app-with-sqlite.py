# import modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# setup flask app

app = Flask (__name__)

# - configure required environmental variables for SQLite

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///email.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# create the database

db = SQLAlchemy(app)

# - Execute sql commands and commit them
drop_table = 'DROP TABLE IF EXISTS users'

users_table = """
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,
email VARCHAR);
"""

db.session.execute
# - Write a function named `find_emails` which find emails using keyword from the user table in the db,
# - and returns result as tuples `(name, email)`.


# - Write a function named `insert_email` which adds new email to users table the db.

# - Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# - using template files named `emails.html` given under `templates` folder
# - and assign to the static route of ('/')


# - Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# - using template files named `add-email.html` given under `templates` folder
# - and assign to the static route of ('/add')

# - Add a statement to run the Flask application which can be reached from any host on port 80.
