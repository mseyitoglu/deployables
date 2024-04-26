from flask import Flask, render_template

app = Flask (__name__)

#path resource

@app.route("/")

def head():
    return render_template("index.html", number1=10,  number2=20)

#sending dynamic variables (user-inputs)

#path ms

@app.route("/ms/<string:num1>/<string:num2>")

def custom(num1, num2):
    if num1.isdigit and num2.isdigit():
        return render_template("index.html", number1=num1, number2=num2)
    else: 
        return "Invalid numbers"

#path sum    
    
@app.route("/sum/<string:a>/<string:b>")

def number(a, b):
    if a.isdigit and b.isdigit():
        total = int(a)+int(b)
        return render_template("body.html", num1=a, num2=b, sum=total)
    else: 
        return "Invalid numbers"
  
app.run(debug=True)