
class MenuSystem():

    def __init__(self):
        self._menu = []

    def get_menu(self):
        return self._menu

    def add_to_menu(self, name, details):
        item = Item(name, details)
        self._menu.append(item)

class Item():

    def __init__(self, name, details):
        self._name = name
        self._details = details

    def get_name(self):
        return self._name

    def get_details(self):
        return self._details

    def __str__(self):
        return self._name + ' ' + self._details


