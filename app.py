from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route("/")
def homeroute():
    return render_template("index.html")

@app.route("/about")
def about_route():
    return render_template("about.html")

@app.route("/events")
def events_route():
    return render_template("events.html")

@app.route("/partners")
def partners_route():
    return render_template("partners.html")

@app.route("/donate")
def donate_route():
    return render_template("donate.html")


    
