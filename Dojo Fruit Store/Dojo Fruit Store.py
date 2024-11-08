from flask import Flask, render_template, request, redirect
import datetime


app = Flask(__name__)

@app.route("/")
def store():
    return render_template("dojo_fruit.html")

@app.route("/checkout", methods=["POST"])
def summary():
    name=request.form["name"]
    student_id=request.form["student_id"]
    strawberries=request.form["strawberries"]
    raspberries=request.form["raspberries"]
    apples=request.form["apples"]
    count= int(strawberries)+int(raspberries)+int(apples)
    now=datetime.datetime.now()
    timestamp=now.strftime("%B %d %Y %I:%M %p")
    print(request.form)
    return render_template("checkout.html", strawberries=strawberries, raspberries=raspberries, apples=apples, count=count, timestamp=timestamp, name=name, student_id=student_id)

   
if __name__=="__main__":
    
    app.run(debug=True) 