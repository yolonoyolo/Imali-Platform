from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route("/")
def homeroute():
    return render_template("index.html")

@app.route("/index.html")
def homeroute2():
    return render_template("index.html")

@app.route("/left-sidebar.html")
def leftbar():
    return render_template("left-sidebar.html")

@app.route("/right-sidebar.html")
def rightbar():
    return render_template("right-sidebar.html")

    
