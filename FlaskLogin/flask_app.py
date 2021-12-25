from flask import Flask, render_template, redirect, url_for, request, session
from functions import *

app = Flask(__name__)
app.secret_key = "any random string"

@app.route('/', methods=["GET","POST"])
def hello_world():
    if (request.method == "POST"):
        #do something
        session["username"] = request.form["username"]

        if (check_pw(request.form["username"],request.form["password"])):
            return redirect("logged_in")
        else:
            return "You are dumb as fuck"
    else:
        return render_template("index.html")

@app.route('/logged_in')
def logged_in():
    if (session["username"] in CheckUserList()):
        return render_template("logged_in.html")
    return "Log in to see this page"

@app.route('/log_out')
def log_out():
    session.pop("username",None)
    return redirect("/")

@app.route('/register', methods=["GET","POST"])
def register():
    if (request.method == "POST"):
        if (request.form["username"] not in CheckUserList()):
            save_user(request.form["username"],request.form["password"])
            return "Succesfully registered. Try to log in now."
        else:
            return "This username is already in use by some idiot"

    return render_template("register.html")

app.run()

