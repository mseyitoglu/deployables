from flask import Flask

app = Flask(__name__)

@app.route("/")

def simpleapp():
    return "<h1>Start as a programmer</h1>"

@app.route("/second")

def second():
    return "<h2>This is the second page</h2>"

@app.route('/third/subthird')

def third():
    return "This is the subpage of the third page"

@app.route("/fourth/<string:id>")

def fourth(id):
    
    if id.isdigit():
        return f"the id of this page is {id}"
    else:
        return f"Not a valild id!"
#run the flask app


app.run(debug=False)

