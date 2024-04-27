# Import Flask modules
from flask import Flask, render_template, redirect, url_for, request
# Create an object named app

app = Flask(__name__) 
# Create welcome page with main.html file and assing it to the root path
@app.route("/")
def main():
    return render_template("main.html", name="Zach")

# Write a function named `greet` which uses template file named `greet.html` given under 
# `templates` folder. it takes parameters from query string on URL, assign that parameter 
# to the 'user' variable and sent that user name into the html file. If it doesn't have any parameter, warning massage is raised

# Write a function named `login` which uses `GET` and `POST` methods, 
# and template files named `login.html` and `secure.html` given under `templates` folder 
# and assign to the static route of ('login')
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        pw= request.form.get("password")
        
        if username == "..." and pw == "...":
            return render_template("secure.html", user=username )
        else:
            return render_template("login.html", user=username, control=True)
    else:
        return render_template("login.html", control=False) 

# Add a statement to run the Flask application which can be reached from any host.


if __name__ == "__main__":

    app.run(debug=False, port= 5001, host ="0.0.0.0")