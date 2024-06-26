# Import Flask modules

from flask import Flask, render_template

# Create an object named app 

app = Flask(__name__)

# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 

@app.route("/")
def head():
    first = "This will be the example of conditions in an ndex file"
    return render_template("index.html", message=first)
# and assign to the route of ('/')



# Create a function named header which prints numbers elements of list one by one in `body.html` 
# and assign to the route of ('/mylist')

@app.route("/mylist")
def header():
    names = ["ms", "altaz", "banu", "kamil"]
    return render_template("body.html", object = names)
# run this app in debug mode on your local.

if __name__ == "__main__":
    app.run(debug=True)

