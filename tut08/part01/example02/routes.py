from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input

def valid_time(time):
    return time > 0

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        desc = request.form["desc"]
        user_input.append([name, zID, desc])
        return redirect(url_for('users'))
    return render_template("index.html")

@app.route("/all_users")
def users():
    return render_template('users.html', all_users=user_input)

@app.route('/interest', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        time = float(request.form.get('time'))
        if not valid_time(time):
            message = 'Error: The time you entered was invalid'
        else:
            initial = float(request.form.get('invested'))
            rate = float(request.form.get('rate'))
            total = initial * rate/100 * time
            message = 'If you invest ${} at {}% for {} year(s) you will get ${} worth of interest'.format(initial, rate, time, total)
        return render_template('interest_form.html', calc_total=True, message=message)
    return render_template('interest_form.html', calc_total=True)
