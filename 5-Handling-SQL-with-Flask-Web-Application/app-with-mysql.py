# Import modules
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
# Create an object named app
app = Flask(__name__)

# Initialize boto3 and get db password


# Configure mysql database
app.config['MYSQL_DATABASE_HOST'] = ' '
app.config['MYSQL_DATABASE_USER'] = ' '
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE'] = 'clarusway'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql = MySQL()
mysql.init_app(app)
connection = mysql.connect()
connection.autocommit(True)
cursor = connection.cursor()

# Create users table within MySQL db and populate with sample data
# Execute the code below only once.
# Write sql code for initializing users table..
drop_table = 'DROP TABLE if EXISTS users;'
users_table = """ 
CREATE_TABLE users (
    username varchar(50) NOT NULL,
    email varchar(50),
    PRIMARY KEY (username)
)   ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=etf8mb4_unicode_ci;
"""
data = """
INSERT INTO clarusway.users
VALUES
    ("jack", "jack@amazon.com")
"""



# Write a function named `find_emails` which find emails using keyword from the user table in the db,
# and returns result as tuples `(name, email)`.


# Write a function named `insert_email` which adds new email to users table the db.

# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')

# Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')

# Add a statement to run the Flask application which can be reached from any host on port 80.
