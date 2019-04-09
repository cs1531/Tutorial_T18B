from server import app, menu_system
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    menu = menu_system.get_menu()
    if request.method == 'POST':
        name = request.form['food_name']
        detail = request.form['food_details']
        menu_system.add_to_menu(name, detail)

    return render_template('index.html', my_menu=menu)
