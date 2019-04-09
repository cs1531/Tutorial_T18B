from flask import Flask
from menu_system import MenuSystem



app = Flask(__name__)

menu_system = MenuSystem()
menu_system.add_to_menu('kebab', 'comes with cheese')
menu_system.add_to_menu('cheese','comes with kebab')
