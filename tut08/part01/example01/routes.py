from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=='POST':
        try:
            name = request.form['name']
            zid = request.form['zID']
            desc = request.form['desc']
        except KeyError:
            return 'Please submit the form'
        user_input[zid] = (name, desc)
        return redirect(url_for('hello', zidpass=zid))

    return render_template("index.html")

@app.route("/Hello")
def hello():

    try:
        zID = request.args['zidpass']
        (name, desc) = user_input[zID]
    except KeyError:
        return redirect(url_for('index'))
        

    return render_template("hello.html", name=name, id=zID, desc=desc)
